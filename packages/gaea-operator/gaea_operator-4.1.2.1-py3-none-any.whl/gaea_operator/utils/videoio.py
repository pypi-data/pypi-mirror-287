#! /usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
Created on Thu Jul 23 13:45:41 2020

@author: luonairui
"""

from __future__ import annotations

import asyncio, functools, inspect, io, os, sys, typing as tp
import numpy as nt

from collections import OrderedDict

sys.path.append(os.path.dirname(__file__))

from imagededup.handlers.search.brute_force import BruteForce
from imagededup.methods.hashing import Hashing, PHash

from .ffmpeg import FormatSpec, ffformats, ffmpeg, ffprobe, format2numpy
from .imdata import VERSION as IMDATA_VERSION, with_index_meta


T = tp.TypeVar('T', covariant=True)
R = tp.TypeVar('R')


class BlockingQueue(tp.Generic[T]):
    def get(self) -> T:
        """
            获取当前值，如果队列为空则抛出异常。
        
        Args:
            None
        
        Returns:
            T (typing.Type[Any]): 返回当前值的类型，可以是任意类型。
        
        Raises:
            QueueEmptyError (exceptions.QueueEmptyError): 如果队列为空，将会抛出此异常。
        
        Example:
            >>> queue = Queue()
            >>> queue.put('hello')
            >>> queue.get()
            'hello'
        """
        ...

    def put(self, data: T):
        """
            将数据放入队列中，如果队列已满，则等待直到有空间。
        如果队列已关闭，则会引发RuntimeError。
        
        Args:
            data (T): 要放入队列的数据类型。
        
        Raises:
            RuntimeError: 如果队列已关闭。
        
        Returns:
            None.
        """
        ...


IterableMaybeAsync : tp.TypeAlias = tp.Iterable[T] | tp.AsyncIterable[T]
QueueMaybeAsync    : tp.TypeAlias = BlockingQueue[T] | asyncio.Queue[T]
TransformFunc      : tp.TypeAlias = tp.Callable[[T], R]
MapFunc            : tp.TypeAlias = \
    tp.Callable[[TransformFunc[T, R], tp.Iterable[T]], tp.Iterable[R]]
AsyncMapFunc       : tp.TypeAlias = \
    tp.Callable[[TransformFunc[T, R], IterableMaybeAsync[T]], tp.AsyncIterable[R]]
StreamFunc         : tp.TypeAlias = \
    tp.Callable[[tp.Iterable[T]], tp.Iterable[R]]
AsyncStreamFunc    : tp.TypeAlias = \
    tp.Callable[[IterableMaybeAsync[T]], tp.AsyncIterable[R]]
ProcessFunc        : tp.TypeAlias = \
    tp.Callable[[T], tp.Generator[R, None, None]]
AsyncProcessFunc   : tp.TypeAlias = \
    tp.Callable[[T], tp.AsyncGenerator[R, None]]
OperatorFunc       : tp.TypeAlias = \
    tp.Callable[[BlockingQueue[T | Exception], BlockingQueue[R]], tp.Any]
AsyncOperatorFunc  : tp.TypeAlias = \
    tp.Callable[[QueueMaybeAsync[T | Exception], asyncio.Queue[R]], tp.Any]


class IMData(with_index_meta(cls=nt.ndarray, ref=True)):
    r"""numpy array with index and meta"""

    PIX_FMT_TO_MODE: dict[str, str] = {
        "bgr24" : "BGR",
        "gray"  : "L",
        "rgb24" : "RGB",
        "rgba"  : "RGBA",
    }

    # @tp.override
    def save(self, path: os.PathLike):
        """
            将图像数据保存到指定路径，同时生成对应的JSON文件。
        
        Args:
            path (os.PathLike): 要保存的路径，可以是字符串或者bytes类型。
        
        Raises:
            None
        
        Returns:
            None
        """
        import PIL.Image as Image
        import json

        mode: str = self.PIX_FMT_TO_MODE.get(self.pix_fmt, "RGB")
        Image.fromarray(self.data, mode=mode).save(path)
        root: dict[str, tp.Any] = {
            "version": IMDATA_VERSION,
            "index": self.id,
            "meta": self.meta,
        }
        json.dump(root, open(os.path.splitext(path)[0] + '.json', "w"))


def retval(*args) -> tp.Any:
    """
    返回参数的第一个或者所有参数，如果没有参数则返回None。
    
    Args:
        args (tuple, optional): 可变长度参数，默认为空元组。
            - 如果只传入了一个参数，则直接返回该参数。
            - 如果传入多个参数，则返回一个元组包含这些参数。
            - 如果不传任何参数，则返回None。
    
    Returns:
        Any: 返回参数的第一个或者所有参数，如果没有参数则返回None。
    """
    if not args: return
    if len(args) == 1: return args[0]
    return args


def map_filter(
    func: TransformFunc[T, R], iterable: tp.Iterable[T],
    map_: MapFunc[T, R] = map,
) -> tp.Generator[R, None, None]:
    r"""map and filter"""

    return (i for i in map_(func, iterable) if i is not None)


async def amap(
    func: TransformFunc[T, R], iterable: IterableMaybeAsync[T],
) -> tp.AsyncGenerator[R, None]:
    r"""async map"""

    is_iter_async: bool = isinstance(iterable, tp.AsyncIterable)
    is_func_async: bool = inspect.iscoroutinefunction(func)
    assert is_iter_async or is_func_async

    if is_iter_async and is_func_async:
        async for item in iterable:
            yield await func(item)
    elif is_iter_async:
        async for item in iterable:
            yield func(item)
    else:
        for item in iterable:
            yield await func(item)


def true() -> bool:
    """
    返回一个布尔值，始终为True。
    
    Args:
        None
    
    Returns:
        bool (bool): 始终为True。
    
    Raises:
        None
    """
    return True


def iter2queue(
    iterable: tp.Iterable[T], out_queue: BlockingQueue[T | Exception],
    running: tp.Callable[[], bool] = true,
):
    """
    将一个迭代器转换为一个阻塞队列，并在后台运行。如果迭代器被关闭或者出现异常，则会将异常放入队列中。
    该函数可以在多线程环境下安全使用。
    
    Args:
        iterable (tp.Iterable[T]): 需要转换的迭代器。
        out_queue (BlockingQueue[T | Exception]): 用于存放迭代器元素或异常的阻塞队列。
        running (tp.Callable[[], bool], optional): 一个返回布尔值的函数，用于判断是否应该继续运行。默认为True。
            Defaults to true.
    
    Raises:
        TypeError: 如果out_queue不是一个BlockingQueue类型。
    """
    it: tp.Iterator[T] = iter(iterable)
    while running():
        try: item: T = next(it)
        except (Exception, ) as e: out_queue.put(e)
        else: out_queue.put(item)


async def aiter2queue(
    iterable: tp.AsyncIterable[T], out_queue: asyncio.Queue[T | Exception],
    running: tp.Callable[[], bool] = true,
):
    it: tp.AsyncIterator[T] = aiter(iterable)
    while running():
        try: item: T = await anext(it)
        except (Exception, ) as e: await out_queue.put(e)
        else: await out_queue.put(item)


def queue2iter(
    inp_queue: BlockingQueue[T | Exception],
    running: tp.Callable[[], bool] = true,
) -> tp.Generator[T, None, tp.Any]:
    """
    将一个阻塞队列转换为迭代器，并在每次获取元素时检查运行状态。如果运行状态变为False，则停止迭代。
    如果队列中的第一个元素是StopIteration类型，则返回其参数作为结果；否则，如果队列中的任何元素是Exception类型，则引发该异常。
    如果运行状态变为False，则不会再次调用inp_queue.get()。
    
    Args:
        inp_queue (BlockingQueue[T | Exception]): 需要被转换成迭代器的阻塞队列。
        running (tp.Callable[[], bool] = true, optional): 用于检查运行状态的函数，默认值为True。
            running()返回False时，迭代器将停止。
    
    Returns:
        tp.Generator[T, None, tp.Any]: 返回一个生成器，可以使用for循环或next()来迭代队列中的元素。
        如果队列中的第一个元素是StopIteration类型，则返回其参数作为结果；否则，如果队列中的任何元素是Exception类型，则引发该异常。
    
    Raises:
        Exception: 如果队列中的任何元素是Exception类型，则引发该异常。
    """
    while running():
        item: T | Exception = inp_queue.get()
        if isinstance(item, StopIteration): return retval(*item.args)
        if isinstance(item, Exception): raise item
        yield item
        inp_queue.task_done()


async def queue2aiter(
    inp_queue: asyncio.Queue[T | Exception],
    running: tp.Callable[[], bool] = true,
) -> tp.AsyncGenerator[T, None]:
    """
    将asyncio.Queue转换为异步迭代器，当队列中有新的数据时，生成器会产生一个值。
    如果队列中出现了StopIteration或者Exception，生成器就会结束。
    
    Args:
        inp_queue (asyncio.Queue[T | Exception]): 需要被转换的asyncio.Queue对象，其中T是任意类型，Exception是可能发生的异常类型。
        running (tp.Callable[[], bool] = true, optional): 用于判断生成器是否应该继续运行的函数，默认返回True。 Default value is true.
    
    Returns:
        tp.AsyncGenerator[T, None]: 异步迭代器，每次从队列中取出一个元素（包括StopIteration和Exception），并且yield出来。如果队列中没有更多元素，则生成器结束。
    
    Raises:
        Exception: 如果队列中出现了Exception，生成器会立即raise这个异常。
    """
    while running():
        item: T | Exception = await inp_queue.get()
        if isinstance(item, StopIteration): return
        if isinstance(item, Exception): raise item
        yield item
        inp_queue.task_done()


def flatmap(func: ProcessFunc[T, R], iterable: tp.Iterable[T]) -> tp.Generator[R, None, None]:
    """
    将一个迭代器中的每个元素应用给定函数，并返回一个新的生成器。
    
    Args:
        func (ProcessFunc[T, R]): 接受单个参数T，返回一个或多个元素R的函数。
        iterable (tp.Iterable[T]): 包含要应用函数的元素的可迭代对象。
    
    Returns:
        tp.Generator[R, None, None]: 返回一个新的生成器，其中包含由应用于每个元素的函数产生的结果。
        生成器没有参数、返回值和异常。
    """
    for item in iterable: yield from func(item)


def stream_operator_wrapper(
    func: StreamFunc[T, R],
    inp_queue: BlockingQueue[T], out_queue: BlockingQueue[R],
):
    """
    包装一个流操作函数，将输入队列转换为迭代器，并将结果写入输出队列。
    
    Args:
        func (StreamFunc[T, R]): 流操作函数，接受一个迭代器，返回一个迭代器。
            T (TypeVar('T')): 输入元素类型。
            R (TypeVar('R')): 输出元素类型。
        inp_queue (BlockingQueue[T]): 输入队列，用于存放输入元素。
            T (TypeVar('T')): 输入元素类型。
        out_queue (BlockingQueue[R]): 输出队列，用于存放处理后的输出元素。
            R (TypeVar('R')): 输出元素类型。
    
    Returns:
        None, 无返回值。
    """
    for item in func(queue2iter(inp_queue)): out_queue.put(item)


def stream_operator(
    func: StreamFunc[T, R] | AsyncStreamFunc[T, R],
    async_queue: bool = False,
) -> OperatorFunc[T, R] | OperatorFunc[T, R]:
    r"""convert `StreamFunc` to `OperatorFunc`"""

    if inspect.iscoroutinefunction(func) or inspect.isasyncgenfunction(func):
        async def wrapped(inp_queue, out_queue):
            is_inp_async: bool = isinstance(inp_queue, asyncio.Queue)
            is_out_async: bool = isinstance(out_queue, asyncio.Queue)
            if is_out_async and is_inp_async:
                async for item in func(queue2aiter(inp_queue)): await out_queue.put(item)
            elif is_out_async:
                async for item in func(queue2iter(inp_queue)): await out_queue.put(item)
            elif is_inp_async:
                async for item in func(queue2aiter(inp_queue)): out_queue.put(item)
            else:
                async for item in func(queue2iter(inp_queue)): out_queue.put(item)
    else:
        if async_queue:
            async def wrapped(inp_queue, out_queue):
                assert isinstance(out_queue, asyncio.Queue)

                for item in func(queue2iter(inp_queue)): await out_queue.put(item)
        else:
            wrapped: OperatorFunc[T, R] = functools.partial(stream_operator_wrapper, func)
    return wrapped


def process_operator_wrapper(
    func: ProcessFunc[T, R],
    inp_queue: BlockingQueue[T | Exception], out_queue: BlockingQueue[R],
    running: tp.Callable[[], bool] = true,
) -> tp.Any:
    """
    处理操作包装函数，将输入队列中的元素传给函数，并将函数返回的结果放入输出队列中。如果遇到异常，则抛出异常。
    如果输入队列中的元素是StopIteration类型，则返回func的retval方法的返回值。
    如果running函数返回False，则停止运行。
    
    Args:
        func (ProcessFunc[T, R]): 一个接收一个参数（T），返回一个迭代器（Iterator[R]）的函数。
        inp_queue (BlockingQueue[T | Exception]): 输入队列，元素为T或Exception。
        out_queue (BlockingQueue[R]): 输出队列，元素为R。
        running (tp.Callable[[], bool] = True, optional): 一个可调用对象，默认为True，表示运行状态。默认为True。
    
    Returns:
        tp.Any: 无返回值。
    
    Raises:
        Exception: 如果输入队列中的元素是Exception类型。
    """
    while running():
        inp_item: T = inp_queue.get()
        if isinstance(inp_item, StopIteration): return retval(*inp_item.args)
        if isinstance(inp_item, Exception): raise inp_item
        for out_item in func(inp_item): out_queue.put(out_item)
        inp_queue.task_done()


def process_operator(
    func: ProcessFunc[T, R] | AsyncProcessFunc[T, R],
    async_queue: bool = False,
) -> OperatorFunc[T, R] | AsyncOperatorFunc[T, R]:
    r"""convert `ProcessFunc` to `OperatorFunc`"""

    if inspect.iscoroutinefunction(func) or inspect.isasyncgenfunction(func):
        async def wrapped(inp_queue, out_queue, running=true):
            is_inp_async: bool = isinstance(inp_queue, asyncio.Queue)
            is_out_async: bool = isinstance(out_queue, asyncio.Queue)
            if is_out_async and is_inp_async:
                while running():
                    inp_item: T = await inp_queue.get()
                    if isinstance(inp_item, StopIteration): return retval(*inp_item.args)
                    if isinstance(inp_item, Exception): raise inp_item
                    async for out_item in func(inp_item): await out_queue.put(out_item)
                    inp_queue.task_done()
            elif is_out_async:
                while running():
                    inp_item: T = inp_queue.get()
                    if isinstance(inp_item, StopIteration): return retval(*inp_item.args)
                    if isinstance(inp_item, Exception): raise inp_item
                    async for out_item in func(inp_item): await out_queue.put(out_item)
                    inp_queue.task_done()
            elif is_inp_async:
                while running():
                    inp_item: T = await inp_queue.get()
                    if isinstance(inp_item, StopIteration): return retval(*inp_item.args)
                    if isinstance(inp_item, Exception): raise inp_item
                    async for out_item in func(inp_item): out_queue.put(out_item)
                    inp_queue.task_done()
            else:
                while running():
                    inp_item: T = inp_queue.get()
                    if isinstance(inp_item, StopIteration): return retval(*inp_item.args)
                    if isinstance(inp_item, Exception): raise inp_item
                    async for out_item in func(inp_item): out_queue.put(out_item)
                    inp_queue.task_done()
    else:
        if async_queue:
            async def wrapped(inp_queue, out_queue, running=true):
                is_inp_async: bool = isinstance(inp_queue, asyncio.Queue)
                is_out_async: bool = isinstance(out_queue, asyncio.Queue)
                assert is_inp_async or is_out_async

                if is_out_async and is_inp_async:
                    while running():
                        inp_item: T = await inp_queue.get()
                        if isinstance(inp_item, StopIteration): return retval(*inp_item.args)
                        if isinstance(inp_item, Exception): raise inp_item
                        for out_item in func(inp_item): await out_queue.put(out_item)
                        inp_queue.task_done()
                elif is_out_async:
                    while running():
                        inp_item: T = inp_queue.get()
                        if isinstance(inp_item, StopIteration): return retval(*inp_item.args)
                        if isinstance(inp_item, Exception): raise inp_item
                        for out_item in func(inp_item): await out_queue.put(out_item)
                        inp_queue.task_done()
                else:
                    while running():
                        inp_item: T = await inp_queue.get()
                        if isinstance(inp_item, StopIteration): return retval(*inp_item.args)
                        if isinstance(inp_item, Exception): raise inp_item
                        for out_item in func(inp_item): out_queue.put(out_item)
                        inp_queue.task_done()
        else:
            wrapped: OperatorFunc[T, R] = functools.partial(process_operator_wrapper, func)
    return wrapped


class Chunked(object):
    r"""split bytes into chunks"""

    def __init__(self, chunk_size: int,
                 data: bytes = b''):
        """
            初始化一个ChunkBuffer对象，用于将数据切割成指定大小的块。
        
        Args:
            chunk_size (int): 每个块的大小，单位为字节（byte）。
            data (bytes, optional): 要被切割的数据，默认为空字节串（b''）。
                Defaults to b''.
        
        Raises:
            ValueError: 当chunk_size为负值或零时会抛出此错误。
        """
        self.chunk_size: int = chunk_size
        self._buffer: list[bytes] = [data]
        self._buffered_size: int = len(data)

    def __call__(self, data: bytes) -> tp.Generator[bytes, None, None]:
        """
        将数据切分成块，每个块的大小为 chunk_size。如果数据长度小于 chunk_size，则返回一个空的生成器。
            否则，返回一个包含块的生成器，每个块都是 chunk_size 字节。最后，返回一个包含剩余数据的块的生成器。
        
            Args:
                data (bytes): 需要切分的数据，类型为 bytes。
        
            Returns:
                tp.Generator[bytes, None, None]: 一个包含切分后的块的生成器，每个块都是 chunk_size 字节。如果数据长度小于 chunk_size，则返回一个空的生成器。
                生成器中的元素类型为 bytes，没有 next() 方法和 sentinel 值。
        """
        if not data: return
        append_size: int = min(len(data), self.chunk_size - self._buffered_size)
        self._buffer.append(data[:append_size])
        self._buffered_size += append_size
        if self._buffered_size < self.chunk_size: return
        yield b''.join(self._buffer)
        data = data[append_size:]
        while len(data) >= self.chunk_size:
            yield data[:self.chunk_size]
            data = data[self.chunk_size:]
        self._buffer = [data]
        self._buffered_size = len(data)


class CatIO(io.RawIOBase):
    r"""cat"""

    def __init__(self, streams: tp.Iterable[io.RawIOBase], /):
        """
        初始化一个新的 StreamMerger 对象。
        
            Args:
                streams (tp.Iterable[io.RawIOBase]): 包含要合并的流的迭代器。
                    StreamMerger 将会从这些流中读取数据，直到其中一个流被关闭或者发生错误。
        
            Raises:
                StopIteration (StopIteration): 如果没有提供任何流。
        """
        self._it: tp.Iterator[io.RawIOBase] = iter(streams)
        try: tp.Optional[io.RawIOBase] = next(self._it)
        except (StopIteration, ): self._stream = None

    # @tp.override
    def read(self,
             size: int = -1,
             /) -> bytes:
        """
        读取指定大小的字节流，如果未指定大小则读取所有剩余字节。
        
        Args:
            size (int, optional, default=-1): 要读取的字节数，默认为-1表示读取所有剩余字节。
        
        Returns:
            bytes: 返回一个包含读取到的字节流的bytes对象。如果没有更多可读字节，则返回空bytes。
        
        Raises:
            StopIteration (BaseException): 如果迭代器已经被用完，则抛出此异常。
        """
        buffer = list[bytes]()
        buffered_size: int = 0
        while self._stream and (size < 0 or buffered_size < size):
            if data := self._stream.read(size if size < 0 else size - buffered_size):
                buffer.append(data)
                buffered_size += len(data)
            else:
                try: self._stream = next(self._it)
                except (StopIteration, ): self._stream = None
        return b''.join(buffer)


class QueueIO(io.RawIOBase):
    r"""wrap queue as stream, write supported only"""

    def __init__(self, queue: QueueMaybeAsync[bytes],
                 *,
                 chunk_size: int = 0):
        """
            Args:
            queue (QueueMaybeAsync[bytes]): The queue to write data to.
            chunk_size (int, optional): If set, the data will be written in chunks of this size. Defaults to 0.
        """
        self._queue: QueueMaybeAsync[bytes] = queue
        if chunk_size:
            self._chunked = Chunked(chunk_size)
            if isinstance(queue, asyncio.Queue):
                self.write: tp.Callable[[bytes], None] = self._write_chunked_async
            else:
                self.write: tp.Callable[[bytes], None] = self._write_chunked
        else:
            if isinstance(queue, asyncio.Queue):
                self.write: tp.Callable[[bytes], None] = self._write_async
            else:
                self.write: tp.Callable[[bytes], None] = self._write

    def _write(self, data: bytes):
        """
        将数据写入队列中，等待被处理。
        
        Args:
            data (bytes): 需要写入的字节数据，类型为bytes。
        
        Returns:
            None; 无返回值，直接将数据放入队列中。
        """
        self._queue.put(data)

    def _write_chunked(self, data: bytes):
        """
            将数据写入队列，以块的形式写入。每个块都是一个字节序列，并且最后一个块可能比其他块小。
        如果数据不能被分成大于0个字节的块，则会引发ValueError异常。
        
        Args:
            data (bytes): 要写入队列的数据，以字节序列形式表示。
        
        Raises:
            ValueError: 如果数据无法被分成大于0个字节的块。
        """
        for chunk in self._chunked(data): self._queue.put(chunk)

    async def _write_async(self, data: bytes):
        """
            异步写入数据到队列中。
        
        Args:
            data (bytes): 需要写入的字节数据。
        
        Returns:
            None; 无返回值，直接将数据添加到队列中。
        """
        await self._queue.put(data)

    async def _write_chunked_async(self, data: bytes):
        """
            将数据切分成块并写入队列中，每次最多写入一个块。如果队列已满，则等待直到有空间可用。
        如果队列被关闭或者发生错误，则引发异常。
        
        Args:
            data (bytes): 要写入的字节数组。
        
        Raises:
            asyncio.CancelledError: 如果任务被取消，则引发此异常。
            Exception: 如果队列被关闭或者发生错误，则引发此异常。
        """
        for chunk in self._chunked(data): await self._queue.put(chunk)


async def decode(
        inp_paths: tp.Iterable[os.PathLike], out_queue: QueueMaybeAsync[IMData],
        /, *args: str,
        pix_fmt: str = "rgb24", fps: float = 0,
        stderr: io.TextIOBase = sys.stderr, on_error: str = "raise",
        **kwds):
    r"""
    decode videos from `inp_paths` as `rawvideo` with FFMPEG, send frames to `out_queue`
    """

    import subprocess

    is_out_async: bool = isinstance(out_queue, asyncio.Queue)

    spec: FormatSpec = (await ffformats())[pix_fmt]
    bits_per_pixel: int = spec["BITS_PER_PIXEL"]
    assert bits_per_pixel % 8 == 0

    bytes_per_pixel: int = bits_per_pixel // 8
    dtype, nchannels = format2numpy(spec)
    is_planar: bool = False
    if nchannels > 1:
        p_pos: int | bool = 'p' in pix_fmt and pix_fmt.index('p')
        is_planar: bool = p_pos and p_pos > 0 and pix_fmt[p_pos - 1].isdigit()

    out_args = OrderedDict[str, tp.Any](f='rawvideo', pix_fmt=pix_fmt)
    if fps > 0: out_args['r'] = fps

    for inp_path in inp_paths:
        try:
            video_meta: dict[str, tp.Any] = await ffprobe(inp_path)
            bytes_per_frame: int = video_meta["width"] * video_meta["height"] * bytes_per_pixel
            if is_planar:
                shape: tuple[int, ...] = (nchannels, video_meta["height"], video_meta["width"])
            else:
                shape: tuple[int, ...] = (video_meta["height"], video_meta["width"], nchannels)
            proc: asyncio.subprocess.Process = await ffmpeg(
                inp_paths_or_stream=inp_path,
                out_args=out_args,
                *args,
                limit=bytes_per_frame, # increase limit if possible
                stderr=subprocess.PIPE,
                **kwds)

            async def transfer():
                chunked = Chunked(bytes_per_frame)
                idx: int = 0
                while True:
                    bytes_data: bytes = await proc.stdout.read(bytes_per_frame)
                    if not bytes_data: break
                    for chunk in chunked(bytes_data):
                        numpy_data: nt.ndarray = nt.frombuffer(chunk, dtype=dtype).reshape(shape)
                        index: tuple[str, int] = (inp_path, idx)
                        meta: dict[str, tp.Any] = {**video_meta, 'pix_fmt': pix_fmt}
                        if fps > 0: meta['timestamp'] = idx / fps
                        data = IMData(numpy_data, index=index, meta=meta)
                        if is_out_async: await out_queue.put(data)
                        else: out_queue.put(data)
                        idx += 1

            _, error, _ = await asyncio.gather(transfer(), proc.stderr.read(), proc.wait())
            if proc.returncode == 0: continue

            for line in error.decode().split('\n'):
                stderr.write("FFMPEG: ")
                stderr.write(line)
                stderr.write('\n')
            stderr.flush()
            raise OSError(proc.returncode)
        except (Exception, ):
            if on_error == "ignore": continue
            else: raise


class Dedup(object):
    def __init__(self,
                 hasher_factory: tp.Callable[[], Hashing] = PHash,
                 searcher_factory: tp.Callable[[tp.Mapping[tp.Hashable, str]], 'Searcher'] = \
                    functools.partial(BruteForce, distance_function=PHash.hamming_distance),
                 window_size: tp.Optional[int] = 1024,
                 **kwds):
        r"""ProcessFunc: filter deduplicated images"""

        self.hasher: Hashing = hasher_factory()
        self.encoding_map = OrderedDict[tp.Hashable, str]()
        self.searcher_factory = searcher_factory
        self.searcher: 'Searcher' = searcher_factory(self.encoding_map)
        self.window_size = window_size
        self.kwds = kwds

    def __call__(self, image: IMData) -> tp.Generator[IMData, None, None]:
        """
        对传入的图像进行处理，并返回一个包含新的图像信息的生成器。
            如果检测到重复图像，则不会返回任何结果；否则，将更新映射并返回新的图像信息。
        
        Args:
            image (IMData): 包含图像数据和其他相关信息的对象，例如ID、路径等。
        
        Returns:
            tp.Generator[IMData, None, None]: 一个包含新的图像信息的生成器，没有额外的返回值或异常信息。
        
        Raises:
            无。
        """
        encoding: str = self.hasher.encode_image(image_array=image.data) # TODO: stateless op
        if self.searcher.search(encoding, **self.kwds): return

        if self.window_size is not None and len(self.encoding_map) >= self.window_size:
            self.encoding_map.popitem()
        self.encoding_map[image.id] = encoding
        self.searcher = self.searcher_factory(self.encoding_map)
        yield image.copy(hash=encoding)


def dedup(images: tp.Iterable[IMData],
          /, **kwds) -> tp.Generator[IMData, None, None]:
    r"""StreamFunc version of Dedup"""

    return flatmap(Dedup(**kwds), images)


if __name__ == '__main__':
    import multiprocessing as mp, queue

    from multiprocessing import Pool as ProcessPool, Process
    from multiprocessing.dummy import Pool as ThreadPool, Process as Thread

    maxsize = 2
    decode_queue = asyncio.Queue(maxsize=maxsize)
    dedup_queue = asyncio.Queue(maxsize=maxsize)
    decode_queue = queue.Queue(maxsize=maxsize)
    dedup_queue = queue.Queue(maxsize=maxsize)
    decode_queue = mp.Queue(maxsize=maxsize)
    dedup_queue = mp.Queue(maxsize=maxsize)

    def sink(image):
        """
            将图像保存到磁盘，并返回一个空列表。
        参数：
            image (Image) - 需要处理的图像对象。
        返回值：
            list - 一个空列表，用于标识该函数没有返回任何有效信息。
        """
        print(type(image), image.id, image.meta, image.shape)
        image.save(f'/tmp/{image.hash}.jpg')
        return []

    async def demo():
        """
            一个示例函数，用于展示如何使用`process_operator`和`decode`来处理视频文件。
        该函数会启动两个进程：一个进程负责解码视频文件并将结果放入一个队列中，另一个进程负责从这个队列中取出结果并对其进行去重操作。
        然后，该函数会等待第一个任务完成或者被取消，并且会停止所有的进程。
        请注意，这只是一个简单的示例，在实际应用中可能需要根据你的特定需求进行修改。
        
        Returns:
            None: 无返回值，该函数主要用于演示如何使用`process_operator`和`decode`来处理视频文件。
        """
        coroutines = [
            decode(
                [
                    '/Users/wangxiao/Downloads/36D454202880D6AE66D6E7F62.jpg',
                    '/Users/wangxiao/Downloads/GPU_AVERAGE_UTILIZATION.png',
                    '/Users/wangxiao/Downloads/施工区-20210706-171833.mp4',
                ],
                decode_queue,
                fps=.4,
                threads=0,
                inp_args=dict(to=5),
            ),
            # process_operator(Dedup(), async_queue=True)(decode_queue, dedup_queue),
            # process_operator(sink, async_queue=True)(dedup_queue, dedup_queue), # dummy loop
        ]
        tasks = list(map(asyncio.create_task, coroutines))
        
        procs = [
            Process(target=process_operator(Dedup()), args=(decode_queue, dedup_queue)),
            Thread(target=process_operator(sink), args=(dedup_queue, dedup_queue)), # dummy loop
        ]
        for p in procs: p.start()

        print('wait tasks:', tasks)
        _, tasks = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
        print('cancel tasks:', tasks)
        for t in tasks: t.cancel()
        print('stop processes:', procs)
        decode_queue.put(StopIteration())
        procs[0].join()
        dedup_queue.put(StopIteration())
        procs[0].join()

    asyncio.run(demo())
