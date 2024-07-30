#! /usr/bin/env python
# -*- coding: utf-8 -*-
r"""
Created on Thu Jul 23 13:45:41 2020

@author: luonairui
"""

from __future__ import absolute_import, division, unicode_literals

import itertools, json, os, re, pickle


VERSION  = 1
NAME_MAX = 240

ESCAPE_PATH_PATTERN = r'\t\n\r\$\&\*\/\?\\\|\~' # r'\t\n\r\!\#\$\&\*\/\:\;\<\=\>\?\\\|\~'
ESCAPE_NAME_PATTERN = ESCAPE_PATH_PATTERN + r'\-'
ESCAPE_PATH_REGEX   = re.compile(f'[{ESCAPE_PATH_PATTERN}]')
ESCAPE_NAME_REGEX   = re.compile(f'[{ESCAPE_NAME_PATTERN}]')



def ensure_index(index):
    r"""
    ensure tuple for sequence index type

    >>> ensure_index('index')
    'index'

    >>> ensure_index(['type', 42])
    ('type', 42)
    """

    return tuple(index) if isinstance(index, list) else index


def ensure_tuple(index):
    r"""
    ensure tuple for any index type

    >>> ensure_tuple('index')
    ('index',)

    >>> ensure_tuple(('type', 42))
    ('type', 42)
    """

    return index if isinstance(index, tuple) else (index, )


def index2name(index):
    r"""
    transform an index to a valid filename

    # Index = str
    >>> index2name('index')
    'index'

    # Index = int
    >>> index2name(42)
    '42'

    # Index = tuple[int | str, ...]
    >>> index2name(('type?', 8))
    'type_-8'
    """

    index = ensure_tuple(index)
    return '-'.join(ESCAPE_NAME_REGEX.sub('_', str(i)[:NAME_MAX]) for i in index)[:NAME_MAX]


def dict_union(base, update):
    r"""return base | update"""

    ret = base.copy()
    ret.update(update)
    return ret


def is_row_major_type(cls):
    r"""
    判断类是否为行主序列类型，即是否为list类型。

    Args:
        cls (type): 需要进行判断的类型，必须是一个类型对象。

    Returns:
        bool: 如果cls是list类型，则返回True；否则返回False。
    """

    return issubclass(cls, list)


def check_column_major_length(data):
    r"""
    check whether the length of column majored `data` is all same
    return the length
    """

    if len(data) == 0: return 0
    it = iter(data.values())
    ret = len(next(it))
    assert all(ret == len(i) for i in it)
    return ret


def tile_row_major(data, meta, overwrite=False):
    r"""tile row majored `data`"""

    if overwrite: return [dict_union(i, meta) for i in data]
    ret = []
    for item in data:
        item = item.copy()
        for key, val in meta.items():
            if key not in item: item[key] = val
        ret.append(item)
    return ret


def tile_column_major(data, meta, overwrite=False):
    r"""tile column majored `data`"""

    length = check_column_major_length(data)
    ret = data.copy()
    for key, val in meta.items():
        if not overwrite and key in ret: continue
        ret[key] = [val] * length
    return ret


def fold_row_major(data, keys=None, single=False):
    r"""fold row majored `data`"""

    if len(data) == 0 or (len(data) == 1 and not single): return (data, dict())
    it = iter(data)
    item = next(it)
    meta_ = dict(item) if keys is None else {k: item[k] for k in keys}
    for item in it:
        for key in list(meta_):
            if key not in item or meta_[key] != item[key]: meta_.pop(key)
    data_ = [{k: v for k, v in i.items() if k not in meta_} for i in data]
    return (data_, meta_)


def fold_column_major(data, keys=None, single=False):
    r"""fold column majored `data`"""

    length = check_column_major_length(data)
    if length == 0 or (length == 1 and not single): return (data, dict())
    data_, meta_ = dict(), dict()
    for key in (data.keys() if keys is None else keys):
        try: values = data[key]
        except (KeyError, ): continue
        try:
            uniques = set(values) # throw
        except (TypeError, ):
            data_[key] = values
        else:
            if len(uniques) == 1: meta_[key] = uniques.pop()
            else: data_[key] = values
    return (data_, meta_)


def with_index_meta(
    cls=None, ref=False,
    index_field='id', meta_field='meta', data_field='data',
):
    r"""
    make block data type with index and metadata:
        cls -> Wrapper(data: cls, id: Index, meta: Meta)
        obj.attr = obj.data.attr or obj.data[attr] or obj.meta[attr]
    """
    def impl(kls):
        assert isinstance(kls, type)
        tile = tile_row_major if is_row_major_type(kls) else tile_column_major
        fold = fold_row_major if is_row_major_type(kls) else fold_column_major
        class Wrapper(object):
            __doc__ = 'wrapped %s with index and metadata\n%s' % (kls.__name__, kls.__doc__)
            @classmethod
            def create(cls, data, index=tuple(), meta=None):
                r"""create new object with data, index and meta"""
                ret = cls.__new__(cls)
                setattr(ret, index_field, ensure_index(index))
                setattr(ret, meta_field, dict() if meta is None else dict(meta))
                setattr(ret, data_field, data)
                return ret
            @classmethod
            def load(cls, path, **kwds):
                r"""load from `path`"""
                root = json.load(open(path + '.meta.json'))
                version, index, meta = root["version"], root["index"], root["meta"]
                assert version <= VERSION
                data = pickle.load(open(path + '.data.pkl', "rb"), **kwds)
                return cls.create(data, index=index, meta=meta)
            @classmethod
            def cache(cls, cache_dir, capacity=16):
                r"""create cache object for this class"""
                return Cache(cls, cache_dir, capacity=capacity)
            if ref:
                def __init__(self, data, index=tuple(), meta=None):
                    setattr(self, index_field, ensure_index(index))
                    setattr(self, meta_field, dict() if meta is None else dict(meta))
                    setattr(self, data_field, data)
            else:
                def __init__(self, *args, **kwds):
                    setattr(self, index_field, ensure_index(kwds.pop("index", tuple())))
                    setattr(self, meta_field, dict(kwds.pop("meta", dict())))
                    setattr(self, data_field, kls(*args, **kwds))
            def __repr__(self):
                return repr(getattr(self, data_field))
            def __getattr__(self, attr):
                try: return super(Wrapper, self).__getattribute__(attr)
                except (AttributeError, ): pass
                meta = getattr(self, meta_field)
                try: return meta[attr]
                except (KeyError, ): pass
                try: return getattr(getattr(self, data_field), attr)
                except (AttributeError, ) as e:
                    try: return getattr(meta, attr)
                    except (AttributeError, ): pass
                    raise e
            def __getstate__(self):
                return (
                    getattr(self, data_field),
                    getattr(self, index_field),
                    getattr(self, meta_field),
                )
            def __setstate__(self, state):
                data, index, meta = state
                setattr(self, data_field, data)
                setattr(self, index_field, ensure_index(index))
                setattr(self, meta_field, meta)
            def __len__(self):
                return len(getattr(self, data_field))
            def __contains__(self, key):
                return key in getattr(self, meta_field) or key in getattr(self, data_field)
            def __getitem__(self, key):
                try: return getattr(self, meta_field)[key]
                except (TypeError, KeyError): pass
                return getattr(self, data_field)[key]
            @property
            def _(self):
                r"""
                accessor for callable attributes:
                    obj._.func() => cls(obj.data.func(), index=obj.index, meta=obj.meta)
                """
                return WrapperProxy(self)
            def get(self, key, default=None):
                r"""get value from meta or data"""
                type_error = False
                try: return getattr(self, meta_field)[key]
                except (TypeError, ): type_error = True
                except (KeyError, ): pass
                try:
                    return getattr(self, data_field)[key]
                except (TypeError, ):
                    if type_error: raise
                    else: return default
                except (KeyError, ):
                    return default
            def save(self, path, **kwds):
                r"""save to `path`"""
                pickle.dump(getattr(self, data_field), open(path + '.data.pkl', "wb"), **kwds)
                root = {
                    "version": VERSION,
                    "index": getattr(self, index_field),
                    "meta": getattr(self, meta_field),
                    "save_kwds": kwds,
                }
                json.dump(root, open(path + '.meta.json', "w"))
            def copy(self, **kwds):
                r"""copy with meta updated from `kwds`"""
                index, meta = getattr(self, index_field), getattr(self, meta_field).copy()
                meta.update(kwds)
                return self.create(getattr(self, data_field), index=index, meta=meta)
            def tile(self, keys=None, overwrite=False):
                r"""tile: broadcast meta into data"""
                index, meta = getattr(self, index_field), getattr(self, meta_field)
                rem_meta, tile_meta = dict(meta), dict()
                for key in (meta if keys is None else keys):
                    try: tile_meta[key] = rem_meta.pop(key)
                    except (KeyError, ): continue
                data = tile(getattr(self, data_field), tile_meta, overwrite=overwrite)
                return self.create(data, index=index, meta=rem_meta)
            def fold(self, keys=None, single=False):
                r"""fold: uniquely aggragate from data into meta"""
                data = getattr(self, data_field)
                if len(data) == 0 or (len(data) == 1 and not single): return self.copy()
                index, meta = getattr(self, index_field), getattr(self, meta_field)
                data, fold_meta = fold(data, keys=keys, single=single)
                return self.create(data, index=index, meta=dict_union(meta, fold_meta))
            if is_row_major_type(kls):
                def groupby(self, by):
                    r"""groupby: groupby with keys updated into meta"""
                    index, meta, data, vals, idxs, keys = self._prepare_groupby(by)
                    f = lambda i: tuple(i[k] for k in keys)
                    for vals_, grouper in itertools.groupby(sorted(data, key=f), key=f):
                        data_ = [i.copy() for i in grouper]
                        for idx, key, val in zip(idxs, keys, vals_):
                            vals[idx] = meta[key] = val
                            for item in data_: item.pop(key)
                        yield self.create(data_, index=(index + tuple(vals)), meta=meta)
            else:
                def groupby(self, by):
                    r"""groupby: groupby with keys updated into meta"""
                    index, meta, data, vals, idxs, keys = self._prepare_groupby(by)
                    indices = range(check_column_major_length(data))
                    f = lambda i: tuple(data[k][i] for k in keys)
                    for vals_, grouper in itertools.groupby(sorted(indices, key=f), key=f):
                        indices_ = list(grouper)
                        data_ = {
                            k: [v[i] for i in indices_]
                            for k, v in data.items()
                            if k not in keys
                        }
                        for idx, key, val in zip(idxs, keys, vals_): vals[idx] = meta[key] = val
                        yield self.create(data_, index=(index + tuple(vals)), meta=meta)
            def _prepare_groupby(self, by):
                index = ensure_tuple(getattr(self, index_field))
                meta = getattr(self, meta_field).copy()
                data = getattr(self, data_field)
                vals = []
                idxs = []
                keys = []
                for idx, key in enumerate(by if isinstance(by, list) else [by]):
                    if key in meta:
                        vals.append(meta[key])
                    else:
                        vals.append(None)
                        idxs.append(idx)
                        keys.append(key)
                return (index, meta, data, vals, idxs, keys)
        class WrapperMeta(type):
            r"""metaclass for wrapper type class variable getter"""
            def __getattr__(self, attr):
                try: return super(WrapperMeta, self).__getattribute__(attr)
                except (AttributeError, ): pass
                return getattr(kls, attr)
        class WrapperProxy(object):
            r"""wrap retval from data methods into wrapper type"""
            def __init__(self, obj):
                self.obj = obj
            def __getattr__(self, attr):
                item = getattr(getattr(self.obj, data_field), attr)
                if not callable(item): return item
                def wrapped(*args, **kwds):
                    data = item(*args, **kwds)
                    index, meta = getattr(self.obj, index_field), getattr(self.obj, meta_field)
                    return self.obj.create(data, index=index, meta=meta)
                return wrapped
        class Cache(object):
            __doc__ = """
            memory + disk cache for type %s
            benefits from save/load methods and index
            """ % (kls.__name__, )
            @staticmethod
            def make_name(index):
                r"""make a non-empty filename for cache"""
                return '_' + index2name(index)
            def __init__(self, cls, cache_dir, capacity=16):
                os.path.isdir(cache_dir) or os.makedirs(cache_dir)
                self.cls = cls
                self.cache_dir = cache_dir
                self.capacity = capacity
                self.cache = dict()
                self.queue = []
            def __repr__(self):
                return '<%s keys=%r>' % (type(self).__name__, self.queue)
            def __getitem__(self, index):
                return self.get(index)
            def get(self, index):
                r"""load data by index"""
                if index in self.cache:
                    data = self.cache[index]
                    self.queue.remove(index)
                    self.queue.append(index)
                else:
                    data = self.cls.load(os.path.join(self.cache_dir, self.make_name(index)))
                    self._set_cache(index, data)
                return data
            def put(self, data):
                r"""store data, indexing by index"""
                index = getattr(data, index_field)
                if index in self.cache:
                    if self.cache[index] is not data:
                        data.save(os.path.join(self.cache_dir, self.make_name(index)))
                        self.cache[index] = data
                    self.queue.remove(index)
                    self.queue.append(index)
                else:
                    data.save(os.path.join(self.cache_dir, self.make_name(index)))
                    self._set_cache(index, data)
            def _set_cache(self, index, data):
                self.cache[index] = data
                self.queue.append(index)
                if len(self.queue) > self.capacity: self.cache.pop(self.queue.pop(0))
        body = dict(Wrapper.__dict__)
        body["__slots__"] = (index_field, data_field, meta_field)
        return WrapperMeta(kls.__name__, (Wrapper, ), body)
    return impl if cls is None else impl(cls)


try:
    import pandas as pf
except (ImportError, ):
    pass
else:
    class IMDataFrame(with_index_meta(
        cls=pf.DataFrame,
        index_field='id', meta_field='meta', data_field='data',
    )):
        @classmethod
        def load(cls, path, **kwds):
            """
                从指定路径加载数据集，并返回一个实例。
            该方法会自动将文件名后缀为'.csv'的文件读取为CSV格式，并将其转换为DataFrame。
            参数：
                path (str) - 数据集所在的路径，包括文件名和后缀。
                其他可选参数（**kwds）将被传递给DataFrame.from_csv()方法。
            返回值：
                instance (cls) - 返回一个类型为cls的实例，表示加载的数据集。
            """
            return cls.from_csv(path + '.csv', **kwds)

        @classmethod
        def from_csv(cls, path, **kwds):
            r"""DataFrame.from_csv + load index & meta"""

            base_path, _ = os.path.splitext(path)
            root = json.load(open(base_path + '.json'))
            version, index, meta = root["version"], root["index"], root["meta"]
            assert version <= VERSION
            save_kwds = root["save_kwds"]
            for key in ("sep", "header", "index_col"):
                if key in save_kwds: kwds.setdefault(key, save_kwds[key])
            data = pf.read_csv(path, **kwds)
            return cls.create(data, index=index, meta=meta)

        def save(self, path, index=True, **kwds):
            """
                将DataFrame保存到指定路径，默认保存为csv格式。
            参数：
                path (str) - 保存的文件路径，不包括文件名。
                index (bool, optional) - 是否保留行索引，默认为True。
                其他关键字参数（kwds）将传递给pandas.DataFrame.to_csv方法。
            返回值：
                None
            """
            return self.to_csv(path + '.csv', index=index, **kwds)

        def to_csv(self, path, index=True, **kwds):
            """
                Save the DataFrame to a CSV file.
            
            Parameters
            ----------
            path : str
                The filename for the CSV file.
            index : bool, default True
                Write row names (index).
             * kwds
                Keyword arguments to be passed to the to_csv method of the
                pandas.DataFrame. See the pandas documentation for more details.
            
            Returns
            -------
            str
                The filename passed to write to.
            
            Raises
            ------
            OSError
                If there is an error writing to the file.
            
            Notes
            -----
            This method saves the DataFrame as a CSV file and also saves metadata
            about the DataFrame in a JSON file with the same name but with a .json
            extension. The JSON file includes information such as the version of
            this library, the id of the DataFrame, and any additional keyword
            arguments that were passed to this method.
            """
            ret = self.data.to_csv(path, index=index, **kwds)
            kwds["index_col"] = list(range(self.data.index.nlevels)) if index else None
            root = {
                "version": VERSION,
                "index": self.id,
                "meta": self.meta,
                "save_kwds": kwds,
            }
            base_path, _ = os.path.splitext(path)
            json.dump(root, open(base_path + '.json', "w"))
            return ret

        def tile(self, keys=None, overwrite=False):
            """
                将当前对象中的数据和元数据进行磁盘上的压缩并存储，返回一个新的对象。
            如果指定了keys，则只会处理这些列；如果overwrite为True，则会覆盖原有的数据。
            
            Args:
                keys (Optional[List[str]], optional): 需要处理的列名列表，默认为None，表示所有列都会被处理. Defaults to None.
                overwrite (bool, optional): 是否覆盖原有的数据，默认为False，表示不覆盖。 Defaults to False.
            
            Returns:
                DataFrame: 返回一个包含压缩后数据和元数据的DataFrame对象。
            
            Raises:
                Exception: 如果出现任何未知错误。
            """
            meta = self.meta.copy()
            data = self.data.copy()
            for column in (self.meta if keys is None else keys):
                if not overwrite and column in data: continue
                try: data[column] = meta[column]
                except (Exception, ): continue
                meta.pop(column)
            return self.create(data, index=self.id, meta=meta)

        def fold(self, keys=None, single=False):
            """
                折叠数据集，将指定的列或所有列进行去重操作，并返回一个新的数据集。如果没有指定列，则默认对所有列进行去重操作。
            如果只有一个列，可以设置参数single为True，表示只对单列进行去重操作。
            
            Args:
                keys (Optional[List[str]], optional): 需要进行去重操作的列名，默认为None，表示对所有列进行去重操作. Default to None.
                single (bool, optional): 是否只对单列进行去重操作，默认为False. Default to False.
            
            Returns:
                DataSet: 返回一个新的DataSet实例，包含去重后的数据和元信息。
            """
            if len(self.data) == 0 or (len(self.data) == 1 and not single): return self.copy()
            meta = dict()
            data = self.data.copy()
            for column in (data.columns if keys is None else keys):
                try: meta[column] = data[column].unique().item() # throw
                except (Exception, ): continue
                data.pop(column)
            return self.create(data, index=self.id, meta=dict_union(self.meta, meta))

        def groupby(self, by):
            """
                对Series或DataFrame进行分组，并返回一个迭代器。每个元素是一个新的Series或DataFrame，包含与该分组相关的数据。
            如果没有指定分组列，则返回一个只包含原始Series或DataFrame的迭代器。
            
            Args:
                by (str or list of str): 用于分组的列名或列名列表。如果为None，则使用所有列进行分组。
            
            Returns:
                Iterator[Series or DataFrame]: 迭代器，其中每个元素是一个新的Series或DataFrame，包含与该分组相关的数据。
            """
            index, meta, data, vals, idxs, keys = self._prepare_groupby(by)
            if keys:
                for vals_, data_ in data.groupby(by=keys):
                    for idx, key, val in zip(idxs, keys, ensure_tuple(vals_)):
                        try: val = val.item()
                        except (Exception, ): pass
                        vals[idx] = val
                        data_.pop(key)
                        try: meta[key] = val
                        except (TypeError, ): pass
                    yield self.create(data_, index=(index + tuple(vals)), meta=meta)
            else:
                yield self.create(self.data, index=(index + tuple(vals)), meta=meta)


if __name__ == '__main__':
    assert IMDataFrame

    df = IMDataFrame(data={'x': [1, 1, 2], 'y': ['a', 'b', 'c'], 'z': ['z'] * 3})
    print(df)
    print(df.id, df.meta, df.shape)
    df = df.fold()
    print(df)
    print(df.id, df.meta, df.shape)
    for f in df.groupby(['x', 'z']):
        print(f)
        print(f.id, f.meta, f.shape)
    df = df.tile()
    print(df)
    print(df.id, df.meta, df.shape)
    df.to_csv('/tmp/frame.csv')
    df = IMDataFrame.from_csv('/tmp/frame.csv')
    print(df)
    print(df.id, df.meta, df.shape)

    IMRecords = with_index_meta(cls=list)
    records = IMRecords(df.to_dict(orient="records"), index='records', meta={'w': 9})
    print(records)
    print(records.id, records.meta)
    records = records.fold()
    print(records)
    print(records.id, records.meta)
    for r in records.groupby(['x', 'z']):
        print(r)
        print(r.id, r.meta)
    records = records.tile()
    print(records)
    print(records.id, records.meta)
    records.save('/tmp/records')
    records = IMRecords.load('/tmp/records')
    print(records)
    print(records.id, records.meta)

    IMTable = with_index_meta(cls=dict)
    table = IMTable(df.to_dict(orient="list"), index=('table', ))
    print(table)
    print(table.id, table.meta)
    table = table.fold()
    print(table)
    print(table.id, table.meta)
    for r in table.groupby(['x', 'z']):
        print(r)
        print(r.id, r.meta)
    table = table.tile()
    print(table)
    print(table.id, table.meta)
    table.save('/tmp/table')
    table = IMTable.load('/tmp/table')
    print(table)
    print(table.id, table.meta)

    import PIL.Image as Image
    import numpy as nt

    IMImage = with_index_meta(cls=Image.Image, ref=True)
    im = IMImage(Image.new("RGB", (100, 100)), index='image', meta={"background": "black"})
    print(im)
    print(im.id, im.meta, im.size)
    im.save('/tmp/image')
    im = IMImage.load('/tmp/image')
    print(im)
    print(im.id, im.meta, im.size)

    cache = IMDataFrame.cache('/tmp', capacity=4)
    df = pf.DataFrame(data=nt.random.randint(0, high=3, size=(9, 9)), columns=list('abcdefghi'))
    df = IMDataFrame(data=df, index='random')
    cache.put(df)
    print(cache)
    keys = list('abcd')
    for f in df.groupby(keys):
        print(f.id)
        cache.put(f)
    print(cache)
    for i in df[keys].drop_duplicates(subset=keys).itertuples(index=False):
        print(i)
        print(cache[(df.id, ) + i])
