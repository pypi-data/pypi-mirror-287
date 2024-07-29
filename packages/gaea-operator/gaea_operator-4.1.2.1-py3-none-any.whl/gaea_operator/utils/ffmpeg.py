#! /usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
Created on Thu Jul 23 13:45:41 2020

@author: luonairui
"""

from __future__ import annotations

import asyncio, io, json, os, subprocess, sys, typing as tp
import numpy as nt


Arguments   : tp.TypeAlias = tp.Sequence[str] | tp.Mapping[str, tp.Any]
BinaryIO    : tp.TypeAlias = io.RawIOBase | io.BufferedIOBase
FormatValue : tp.TypeAlias = str | int | tuple[int, ...]
FormatSpec  : tp.TypeAlias = tp.Mapping[str, FormatValue]


def try_cast(val: tp.Any, *types: type) -> tp.Any:
    r"""
    尝试将给定值转换为指定类型，如果无法转换则返回原值。
    
    Args:
        val (tp.Any): 需要进行类型转换的值。
        *types (type, optional): 可变参数，需要转换成的类型列表，默认为空。
    
    Returns:
        tp.Any: 如果能够转换成任意一种类型，则返回该类型的值；否则返回原始值。
    """

    for type_ in types:
        try: return type_(val)
        except (TypeError, ValueError): pass
    return val


def to_args(args: Arguments) -> list[str]:
    r"""convert Arguments to command arguments"""

    if isinstance(args, tp.Sequence): return list(args)
    return sum((['-' + k] if v is None else ['-' + k, str(v)] for k, v in args.items()), [])


def check_error(
    retcode: int, error: bytes,
    stderr: io.TextIOBase | int = subprocess.DEVNULL,
    raises: type[Exception] = OSError,
    prefix: str = "FFMPEG: ",
):
    r"""check FFMPEG return code and redirect `error` to `stderr`"""

    if retcode == 0: return
    if not isinstance(stderr, int):
        for line in error.decode().split('\n'):
            stderr.write(prefix)
            stderr.write(line)
            stderr.write('\n')
        stderr.flush()
    raise raises(retcode)


async def ffformats(
        program: str = 'ffmpeg',
        *args: str,
        stderr: io.TextIOBase | int = subprocess.DEVNULL,
        **kwds) -> dict[str, FormatSpec]:
    r"""get FFMPEG pixel formats spec by name"""

    proc: asyncio.subprocess.Process = await asyncio.create_subprocess_exec(
        program,
        '-pix_fmts',
        *args,
        stdout=subprocess.PIPE,
        stderr=(stderr if isinstance(stderr, int) else subprocess.PIPE),
        **kwds)
    output, error = await proc.communicate()
    check_error(proc.returncode, error, stderr=stderr, prefix=f'{program}: ')

    key: str = "NAME"
    started: bool = False
    ret = dict[str, FormatSpec]()
    for line in output.decode().split('\n'):
        tokens: list[str] = line.split()
        if not started:
            if key in tokens:
                started = True
                fields: list[str] = tokens
            continue
        if len(tokens) != len(fields): continue
        spec = dict[str, FormatValue](zip(fields, tokens))
        spec["NB_COMPONENTS"] = int(spec["NB_COMPONENTS"])
        spec["BITS_PER_PIXEL"] = int(spec["BITS_PER_PIXEL"])
        if "BIT_DEPTHS" in spec:
            spec["BIT_DEPTHS"] = tuple(int(s) for s in spec["BIT_DEPTHS"].split('-'))
        ret[spec[key]] = spec
    return ret


async def ffprobe(
        path_or_stream: os.PathLike | BinaryIO,
        /, *args: str,
        stream: tp.Optional[int] = 0,
        program: str = 'ffprobe', stderr: io.TextIOBase | int = sys.stderr,
        **kwds) -> dict[str, tp.Any]:
    r"""run `ffprobe` on `path_or_stream`, get the media info"""

    arguments: list[str] = ['-hide_banner', '-of', 'json']

    if stream is None:
        arguments += ['-show_format']
    else:
        arguments += ['-show_streams', '-select_streams', str(stream)]

    if isinstance(path_or_stream, BinaryIO):
        proc: asyncio.subprocess.Process = await asyncio.create_subprocess_exec(
            program,
            *arguments, *args, '-i', '-',
            stdin=path_or_stream, stdout=subprocess.PIPE,
            stderr=(stderr if isinstance(stderr, int) else subprocess.PIPE),
            **kwds)
    else:
        proc: asyncio.subprocess.Process = await asyncio.create_subprocess_exec(
            program,
            *arguments, *args, '-i', str(path_or_stream),
            stdout=subprocess.PIPE,
            stderr=(stderr if isinstance(stderr, int) else subprocess.PIPE),
            **kwds)

    output, error = await proc.communicate()
    check_error(proc.returncode, error, stderr=stderr, prefix=f'{program}: ')

    ret: dict[str, tp.Any] = json.loads(output)
    ret = ret['format'] if stream is None else ret['streams'][0]
    return {k: try_cast(v, int, float) for k, v in ret.items()}


async def ffmpeg(
        inp_paths_or_stream: os.PathLike | list[os.PathLike] | BinaryIO | int = subprocess.PIPE,
        out_path_or_stream: os.PathLike | BinaryIO | int = subprocess.PIPE,
        inp_args: Arguments = tuple(),
        out_args: Arguments = tuple(),
        *args: str,
        overwrite: bool = True, stream: tp.Optional[int] = 0,
        threads: int = 1, loglevel: str = "warning",
        program: str = 'ffmpeg', stderr: tp.Optional[BinaryIO | int] = subprocess.DEVNULL,
        **kwds):
    r"""
        run `ffmpeg` as `asyncio.subprocess.Process` 
        resolved to:
            ffmpeg \
                args... \
                inp_args... \
                -i inp_paths_or_stream -i inp_paths_or_stream... \
                out_args ... \
                out_path_or_stream
    """

    arguments: list[str] = [
        '-hide_banner',
        '-threads', str(threads),
        '-loglevel', loglevel,
    ] + list(args)

    if overwrite:
        arguments += ['-y']

    arguments += to_args(inp_args)
    if isinstance(inp_paths_or_stream, (BinaryIO, int)):
        arguments += ['-i', '-']
        stdin: tp.Optional[BinaryIO | int] = inp_paths_or_stream
    else:
        if isinstance(inp_paths_or_stream, (list, tuple)):
            for path in inp_paths_or_stream:
                arguments += ['-i', str(path)]
        else:
            arguments += ['-i', str(inp_paths_or_stream)]
        stdin: tp.Optional[BinaryIO | int] = None

    if stream is not None:
        arguments += ['-an', '-map', f'{stream}:v:0']

    arguments += to_args(out_args)
    if isinstance(out_path_or_stream, (BinaryIO, int)):
        arguments += ['-']
        stdout: tp.Optional[BinaryIO | int] = out_path_or_stream
    else:
        arguments += [str(out_path_or_stream)]
        stdout: tp.Optional[BinaryIO | int] = None

    proc: asyncio.subprocess.Process = await asyncio.create_subprocess_exec(
        program,
        *arguments,
        stdin=stdin, stdout=stdout, stderr=stderr,
        **kwds)

    return proc


def format2numpy(format_: FormatSpec):
    r"""get (dtype, nchannels) from `format_`"""

    c: int = format_["NB_COMPONENTS"]
    d: int = format_["BITS_PER_PIXEL"]
    b: int = format_.get("BIT_DEPTHS", [d // c] * c)
    assert c > 0 and d > 0 and d % 8 == 0, f'Unsupported format: {format_["NAME"]}'

    b_: int = d // c
    if all(i == b_ for i in b):
        dtype = nt.dtype(f'uint{b_}')
    else:
        dtype = nt.dtype(f'uint{d}')
        c = 1

    return (dtype, c)


if __name__ == '__main__':
    formats = asyncio.run(ffformats())
    print(formats)

    video_path = '/tmp/input.mp4'
    video_meta = asyncio.run(ffprobe(open(video_path, "rb")))
    print(video_meta)

    async def demo():
        """
            使用ffmpeg将视频转换为mp4格式，并保存到指定路径。
        该函数是一个异步函数，需要在asyncio的事件循环中调用。
        
        Args:
            None
        
        Returns:
            None
        
        Raises:
            None
        
        Side Effects:
            1. 将视频文件转换为mp4格式，并保存到/tmp/output.mp4。
            2. 如果出现任何错误，将被抛出。
        """
        proc = await ffmpeg(open(video_path, "rb"), '/tmp/output.mp4', out_args=dict(c='copy'))
        await proc.wait()

    asyncio.run(demo())
