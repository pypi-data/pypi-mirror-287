#! /usr/bin/env python
# -*- coding: utf-8 -*-
r"""
Created on Tue Aug 18 15:03:29 2020

@author: luonairui
"""

from __future__ import absolute_import, division, unicode_literals

import glob, json, os, typing as tp
import pandas as pf


FIELD_SEP = '__'


def try_cast(series, dtype):
    r"""
    尝试将 pandas Series 转换为指定类型，如果失败则返回原始 Series。

    Args:
        series (pandas.Series): 需要转换的 pandas Series。
        dtype (str or numpy.dtype): 目标类型，可以是字符串或 NumPy 数据类型。

    Returns:
        pandas.Series: 转换后的 pandas Series，如果转换失败则返回原始 Series。
    """

    try: return series.astype(dtype) # throw ValueError
    except (ValueError, ): return series


def as_nullable_int(series, ref_type_name):
    r"""
    将 pandas Series 转换为可空整数类型，支持 int、uint 和其他类型。

    Args:
        series (pandas.Series): 需要转换的 pandas Series。
        ref_type_name (str): 参考类型名称，可以是 'int'、'uint'、'float' 等类型。

    Returns:
        pandas.Series: 返回一个与输入 series 具有相同索引和元素值但类型可能不同的新 Series。
            - 如果 ref_type_name 以 'int' 或 'uint' 开头，则返回一个可空整数类型；
            - 否则返回一个可空指定类型的 Series。

    Raises:
        None
    """

    ref_type_name = ref_type_name.lower()
    if ref_type_name.startswith('int'): return series.astype('I' + ref_type_name[1:])
    if ref_type_name.startswith('uint'): return series.astype('UI' + ref_type_name[2:])
    return series.astype(ref_type_name)


def elevate_fields(
    s,
    direct=False,
):
    r"""
    rename fields with dot in the expression `s` to more program-friendly symbols

    >>> elevate_fields('a.b.c')
    'a__b__c'
    """

    if direct: return s.replace('.', FIELD_SEP)

    import re

    return re.sub(r'\b([A-Za-z]\w*)\.(?=[A-Za-z]\w*)\b', r'\1' + FIELD_SEP, s)


def elevate_dict(d):
    r"""
    elevate nested dicts to top level

    >>> elevate_dict({'a': {'b': {'c': 1}}, 'x': 2})
    {'a__b__c': 1, 'x': 2}
    """

    ret = (type(d) if isinstance(d, tp.MutableMapping) else dict)()
    for base_k, base_v in d.items():
        if isinstance(base_v, tp.Mapping):
            sub_d = elevate_dict(base_v)
            for sub_k, sub_v in sub_d.items():
                ret[base_k + FIELD_SEP + sub_k] = sub_v
            continue
        ret[base_k] = base_v
    return ret


def elevate_df(df):
    r"""
    elevate nested dict series to top level

    >>> df = pf.DataFrame({'a': [{'b': 1, 'c': 2}, {'c': 3}], 'x': [8, 9]})
    >>> df
                      a  x
    0  {'b': 1, 'c': 2}  8
    1          {'c': 3}  9

    >>> elevate_df(df)
       a__b  a__c  x
    0   1.0   2.0  8
    1   NaN   3.0  9

    """

    ret = pf.DataFrame(index=df.index)
    for base_col, base_s in df.items():
        base_s = base_s.dropna()
        if not base_s.empty and pf.api.types.is_dict_like(base_s.iloc[0]):
            sub_f = base_s.apply(pf.Series)
            sub_f = elevate_df(sub_f)
            sub_f = sub_f.rename(columns=(lambda c: base_col + FIELD_SEP + c))
            ret = ret.join(sub_f) # combine_first
            for ret_col, sub_s in sub_f.items():
                ret[ret_col] = as_nullable_int(ret[ret_col], sub_s.dtype.name)
            continue
        ret[base_col] = base_s
    return ret


PreparedExplodedSeries = tp.NamedTuple(
    'PreparedExplodedSeries', [
        ('has_list', bool),
        ('vals', list),
        ('locs', list),
        ('idxs', list),
    ],
)


def prepare_exploded_series(
    series,
    empty_as_na=False,
):
    r"""
    将一个 pandas Series 中的元素展开为多个值，并返回一个 PreparedExplodedSeries 对象。

    如果一个元素是可迭代类型（比如 list、tuple），则会将其展开成多个值。否则，该元素会被视为单个值。

    如果 `empty_as_na` 参数设置为 True，那么空列表或者 tuple 会被视为 None 而不是空列表。默认情况下，空列表会被视为空列表。

    Args:
        series (pandas.Series): 需要处理的 pandas Series。
        empty_as_na (bool, optional): 如果为 True，则空列表或者 tuple 会被视为 None 而不是空列表。默认为 False。

    Returns:
        PreparedExplodedSeries: 包含以下属性的 PreparedExplodedSeries 对象：
            - has_list (bool) : 是否有任何元素是可迭代类型（比如 list、tuple）。
            - vals (List[Any]): 展开后的所有值。
            - locs (List[int]): 每个值在原始 Series 中的位置。
            - idxs (List[int]): 每个值在展开后的序列中的位置。
    """

    has_list = False
    vals = []
    locs = []
    idxs = []
    if empty_as_na:
        def process_list(loc, val, num):
            if num == 0:
                vals.append(None)
                locs.append(loc)
                idxs.append(0)
            else:
                vals.extend(val)
                locs.extend([loc] * num)
                idxs.extend(list(range(num)))
    else:
        def process_list(loc, val, num):
            vals.extend(val)
            locs.extend([loc] * num)
            idxs.extend(list(range(num)))
    for loc, val in enumerate(series):
        if pf.api.types.is_list_like(val) and not pf.api.types.is_dict_like(val):
            has_list = True
            process_list(loc, val, len(val))
        else:
            vals.append(val)
            locs.append(loc)
            idxs.append(0)
    return PreparedExplodedSeries(has_list=has_list, vals=vals, locs=locs, idxs=idxs)


def explode_df(
        df, col,
        **kwds):
    r"""
    like `pandas.DataFrame.explode` but process null and empty better

    >>> df = pf.DataFrame({
    ...     'a': [['x', 'y'], [], None, ['z']],
    ...     'b': [[0], [1, 2], [3, 4, 5], []],
    ...     'c': [0, 1, 2, 3],
    ... })
    >>> df
            a          b  c
    0  [x, y]        [0]  0
    1      []     [1, 2]  1
    2    None  [3, 4, 5]  2
    3     [z]         []  3

    >>> explode_df(df, 'a')
       @a     a          b  c
    0   0     x        [0]  0
    0   1     y        [0]  0
    2   0  None  [3, 4, 5]  2
    3   0     z         []  3

    >>> explode_df(df, 'b') # NOTE: numeric sequences wouldn't be exploded
            a          b  c
    0  [x, y]        [0]  0
    1      []     [1, 2]  1
    2    None  [3, 4, 5]  2
    3     [z]         []  3

    """

    has_list, vals, locs, idxs = prepare_exploded_series(df[col], **kwds)
    if not has_list: return df
    exploded_s = pf.Series(data=vals)
    ## NOTE: pure numeric sequence is not indexable, skip it
    if pf.api.types.is_numeric_dtype(exploded_s): return df
    ret = df.iloc[locs].copy()
    ret[col] = exploded_s.values
    loc = df.columns.get_loc(col)
    ret.insert(loc, '@' + col, idxs)
    return ret


def encode_dummy_df(df, col):
    r"""
    encode a multi-options field in dataframe to dummy(onehot code) columns

    # suppose the multi-options column a has options {'x', 'y', 'z'}
    >>> df = pf.DataFrame({'a': [['x', 'y'], [], None, {'z'}], 'b': [0, 1, 2, 3]})
    >>> df
            a  b
    0  [x, y]  0
    1      []  1
    2    None  2
    3     {z}  3

    >>> encode_dummy_df(df, 'a')
         #a   a__x   a__y   a__z  b
    0     2   True   True  False  0
    1     0  False  False  False  1
    2  <NA>   <NA>   <NA>   <NA>  2
    3     1  False  False   True  3

    """

    prepared = prepare_exploded_series(df[col])
    exploded_s = pf.Series(data=prepared.vals, index=prepared.locs)
    exploded_dummy_f = pf.get_dummies(exploded_s, prefix=col, prefix_sep=FIELD_SEP)
    dummy_f = exploded_dummy_f.groupby(level=0).sum().astype("boolean")
    count_s = dummy_f.sum(axis="columns").astype("UInt64")
    count_s.name = '#' + col
    df_ = df.reset_index(drop=True)
    loc = df_.columns.get_loc(col)
    df_ = df_.iloc[:, :loc].join(count_s).join(dummy_f).join(df_.iloc[:, (loc + 1):])
    as_zero_s = pf.isna(df_[count_s.name])
    as_null_s = df_[count_s.name].eq(0) & ~as_zero_s
    df_.loc[as_zero_s, count_s.name] = 0
    df_.loc[as_zero_s, dummy_f.columns] = False
    df_.loc[as_null_s, [count_s.name] + list(dummy_f.columns)] = None # pf.NA
    return df_.set_index(df.index)


def flatten_df(df):
    r"""
    explode all nested series to make the dataframe flat
    all combinations of nested series will be enumerated

    >>> df = pf.DataFrame({
    ...    'a': [['x', 'y'], ['z', 'w']],
    ...    'b': [['x'], ['y', 'z']],
    ...    'c': [0, 1],
    ... })
    >>> df
            a       b  c
    0  [x, y]     [x]  0
    1  [z, w]  [y, z]  1

    >>> flatten_df(df)
       @a  a  @b  b  c
    0   0  x   0  x  0
    0   1  y   0  x  0
    1   0  z   0  y  1
    1   0  z   1  z  1
    1   1  w   0  y  1
    1   1  w   1  z  1

    """

    for base_col in list(df.columns):
        df = explode_df(df, base_col, empty_as_na=True)
        df_ = df.reset_index(drop=True)
        base_s = df_.pop(base_col).dropna()
        if not base_s.empty and pf.api.types.is_dict_like(base_s.iloc[0]):
            sub_f = base_s.apply(pf.Series)
            sub_f = flatten_df(sub_f)
            sub_f = sub_f.rename(columns=(lambda c: base_col + FIELD_SEP + c))
            res_f = df_.join(sub_f) # combine_first
            for ret_col, sub_s in sub_f.items():
                res_f[ret_col] = as_nullable_int(res_f[ret_col], sub_s.dtype.name)
            df = res_f.set_index(df.index[res_f.index])
    return df


class Deduplicates(object):
    r"""
    deduplicate records in streaming batches by given expressions
    similar to 'SELECT DISTINCT' in SQL
    args:
        exprs: list of expressions to deduplicate with,
            record will be dropped when all expressions are evaluated
            to be equal with any previous records
        window: window size of __call__ calls to deduplicate within, -1 for no limit
        capacity: max number of unique records to keep after the __call__ call, -1 for no limit

    >>> dedup = Deduplicates(['a', 'abs(b - 2)'])
    >>> l = [1, 2, 3, 4]
    >>> df = pf.DataFrame({'a': [i % 2 for i in l], 'b': l, 'c': l})
    >>> df['the value of abs(b - 2)'] = (df.b - 2).abs()
    >>> df
       a  b  c  the value of abs(b - 2)
    0  1  1  1                        1
    1  0  2  2                        0
    2  1  3  3                        1
    3  0  4  4                        2

    >>> dedup(df)
       a  b  c  the value of abs(b - 2)
    0  1  1  1                        1
    1  0  2  2                        0
    3  0  4  4                        2

    >>> df = pf.DataFrame({'a': [3, 1, 0, 0], 'b': [2, 1, 1, 3]})
    >>> df
       a  b
    0  3  2
    1  1  1
    2  0  1
    3  0  3

    >>> dedup(df)
       a  b
    0  3  2
    2  0  1

    """

    def __init__(self, exprs,
                 window=-1, capacity=-1):
        """
            Initializes the HitCounter class.
        
        Args:
            exprs (list[str]): A list of expressions to be counted.
            window (int, optional): The time window in seconds for counting hits. Defaults to -1.
            capacity (int, optional): The maximum number of elements to store. Defaults to -1.
        
        Raises:
            TypeError: If `exprs` is not a list of strings.
            ValueError: If `window` or `capacity` is negative.
        """
        self.exprs = exprs
        self.window = window
        self.capacity = capacity
        self.hit_s = pf.Series(dtype="int")

    def __repr__(self):
        """
            Return a string representation of the object.
        
        Returns:
            str: A string containing the type name and the hit history.
        """
        return '%s histories:\n%r' % (type(self).__name__, self.hit_s)

    def __call__(self, df):
        """
            对传入的 DataFrame 进行处理，并返回新的 DataFrame。
        该方法会将传入的 DataFrame 中的数据类型转换为简单类型（"object"），然后使用 NumExpr 库计算表达式列表中的每个表达式，并将结果存储在一个新的 Series 中。
        接下来，会检查这些值是否重复或者已经被识别过，如果是，则从 Series 中删除；最后，根据窗口大小和容量限制，更新 self.hit_s 属性。
        返回的新的 DataFrame 包含了没有重复且未被识别过的行。
        
        Args:
            df (pandas.DataFrame): 需要处理的 DataFrame。
        
        Returns:
            pandas.DataFrame: 返回一个新的 DataFrame，其中包含了没有重复且未被识别过的行。
        """
        df = df.astype("object").infer_objects() # cast to simple types for NumExpr
        key_f = pf.DataFrame()
        for i, expr in enumerate(self.exprs):
            key_f[i] = df.eval(expr)
        key_s = pf.Series(data=key_f.itertuples(index=False), index=key_f.index)
        dup_s = key_s.duplicated()
        hit_s = key_s.isin(self.hit_s.index)
        new_s = ~(hit_s | dup_s)
        self.hit_s = pf.concat([
            pf.Series(data=0, index=key_s.loc[~dup_s], dtype="int"),
            self.hit_s[self.hit_s.index.difference(key_s)] + 1,
        ])
        if self.window > 0: self.hit_s = self.hit_s.loc[self.hit_s.lt(self.window)]
        if self.capacity > 0: self.hit_s = self.hit_s.iloc[:self.capacity]
        return df.loc[new_s]


def load_json_labels(filepath, flatten=True):
    r"""load SDK JSON results"""

    df = pf.read_csv(filepath, sep=' ', names=['filename', 'label'], index_col=0)
    assert not df.empty, 'label file %r is empty' % (filepath, )

    df = df.label.apply(json.loads).apply(pf.Series)
    if flatten: df = flatten_df(df)
    return df


def load_txt_labels(dirpath):
    r"""
    load SDK TXT results
    columns:
        category.c_str(), int(object->is_truncated), int(object->is_occluded),
        object->alpha, object->bbox[0], object->bbox[1], object->bbox[2], object->bbox[3],
        object->size[2], object->size[1], object->size[0]
    """

    names = [
        "category", "is_truncated", "is_occluded",
        "alpha", "left", "top", "right", "bottom",
        "height", "width", "length",
    ]
    col2name = dict(enumerate(names))
    col2name[15] = "max_sub_type_prob"
    df = pf.concat([
        pf.read_csv(p,
            sep=' ', usecols=list(col2name.keys()), names=list(col2name.values()),
        ).assign(filename=os.path.basename(p)) for p in glob.glob(dirpath + '/*.txt')])

    return df.reset_index().set_index("filename")


def joint_predicate(df, conditions):
    r"""
    test dataframe `df` by joint `conditions` within each same index
    return a bool series indicating whether current record matches any condition
    if not all conditions is matched among the same index,
    the whole index is considered not matched

    >>> df = pf.DataFrame({'a': [1, 2, 1, 2, 3], 'b': [3, 4, 5, 7, 9]}, index=[1, 1, 2, 2, 2])
    >>> df
       a  b
    1  1  3
    1  2  4
    2  1  5
    2  2  7
    2  3  9

    >>> joint_predicate(df, ['a == 1', 'a != 1 and b % a'])
    1    False
    1    False
    2     True
    2     True
    2    False
    dtype: bool

    """

    df = df.astype("object").infer_objects() # cast to simple types for NumExpr
    index = df.index.unique()
    mask_s = pf.Series(data=False, index=df.index)
    for condition in conditions:
        while True:
            try:
                pred_s = df.eval(condition).fillna(False).astype("bool") # throw NameError
            except (NameError, ) as e:
                msg, = e.args
                tokens = msg.split("'")
                if len(tokens) != 3: raise # not expected format

                import warnings

                warnings.warn(
                    '%s, '
                    'this warning indicates that such an error is ignored, '
                    'and you should be awared' % (msg, ),
                    category=UserWarning, stacklevel=2,
                )
                key = tokens[1]
                df[key] = None # pf.NA # set dummy value and retry
            else:
                break # success

        index = index.intersection(df.index[pred_s]).unique() #
        mask_s |= pred_s
    return mask_s & mask_s.index.isin(index)


def render_json_detections(
    df, images_dir,
    color=(80, 80, 240), thickness=2, font=None,
    label='{modelName}.{id}={typeName}: {confidence:.1f}',
):
    r"""yield (filename, rendered_image, box_f)"""

    import cv2 as cv

    font = cv.FONT_HERSHEY_SIMPLEX if font is None else font
    box_cols = [
        'box__topLeft__x', 'box__topLeft__y',
        'box__buttonRight__x', 'box__buttonRight__y',
    ]
    if 'boxs' in df:
        for filename, box, box_is_na in zip(df.index, df.boxs, pf.isna(df.boxs)):
            image = cv.imread(os.path.join(images_dir, filename))
            assert image is not None
            if box_is_na or not box:
                yield (filename, image, None)
                continue
            box_f = elevate_df(pf.DataFrame.from_records(box))
            for row in box_f.dropna(subset=box_cols).itertuples(index=False):
                l, t = int(row.box__topLeft__x), int(row.box__topLeft__y + .5)
                r, b = int(row.box__buttonRight__x), int(row.box__buttonRight__y + .5)
                cv.rectangle(image, (l, t), (r, b), color, thickness=thickness)
                if not row.get("attrs"): continue
                lines = [label.format(**a) for a in row["attrs"]]
                scale = 1.
                spacing = thickness * 2
                width, height = 0, spacing * len(lines)
                for text in lines:
                    (w, h), _ = cv.getTextSize(text, font, scale, thickness)
                    width, height = max(width, w), height + h
                scale = max(.5, min(scale, (r - l) / width, (b - t) / height))
                for text, y in zip(lines, range(t - spacing, 0, -height // len(lines))):
                    cv.putText(image, text, (l, y), font, scale, color, thickness=thickness)
            yield (filename, image, box_f)
    else:
        label = label.replace('{', '{boxs__attrs__')
        box_cols = ['boxs__' + k for k in box_cols]
        for filename, box_f in df.groupby(by=df.index):
            image = cv.imread(os.path.join(images_dir, filename))
            assert image is not None
            for _, attr_f in box_f.dropna(subset=box_cols).groupby(by="@boxs"):
                l = int(attr_f.boxs__box__topLeft__x.unique().item())
                t = int(attr_f.boxs__box__topLeft__y.unique().item())
                r = int(attr_f.boxs__box__buttonRight__x.unique().item() + .5)
                b = int(attr_f.boxs__box__buttonRight__y.unique().item() + .5)
                cv.rectangle(image, (l, t), (r, b), color, thickness=thickness)
                if "boxs__@attrs" not in attr_f: continue
                lines = [
                    label.format(**row)
                    for _, row in attr_f.groupby(by="boxs__@attrs").first().iterrows()
                ]
                if not lines: continue
                scale = 1.
                spacing = thickness * 2
                width, height = 0, spacing * len(lines)
                for text in lines:
                    (w, h), _ = cv.getTextSize(text, font, scale, thickness)
                    width, height = max(width, w), height + h
                scale = max(.5, min(scale, (r - l) / width, (b - t) / height))
                for text, y in zip(lines, range(t - spacing, 0, -height // len(lines))):
                    cv.putText(image, text, (l, y), font, scale, color, thickness=thickness)
            yield (filename, image, box_f)


def render_txt_detections(
    df, image_files,
    color=(80, 80, 240), thickness=2, font=None,
    label='{category}: {max_sub_type_prob:.1f}',
):
    r"""yield (filename, rendered_image, box_f)"""

    import cv2 as cv

    font = cv.FONT_HERSHEY_SIMPLEX if font is None else font
    for filename, box_f in df.groupby(df.index):
        filepath = image_files[int(os.path.splitext(filename)[0])]
        image = cv.imread(filepath)
        assert image is not None
        for row in box_f.itertuples(index=False):
            l, t = int(row.left), int(row.top + .5)
            r, b = int(row.right), int(row.bottom + .5)
            cv.rectangle(image, (l, t), (r, b), color, thickness=thickness)
            scale = 1.
            text = label.format(**row._asdict())
            (w, h), _ = cv.getTextSize(text, font, scale, thickness)
            scale = max(.5, min(scale, (r - l) / w, (b - t) / h))
            cv.putText(
                image, text, (l, t - thickness * 2), font, scale, color,
                thickness=thickness,
            )
        yield (os.path.basename(filepath), image, box_f)


def crop_json_images(df, images_dir):
    r"""yield ((filename, box_i), cropped_image, attr_f)"""

    import cv2 as cv

    box_cols = [
        'box__topLeft__x', 'box__topLeft__y',
        'box__buttonRight__x', 'box__buttonRight__y',
    ]
    if 'boxs' in df:
        for filename, box, box_is_na in zip(df.index, df.boxs, pf.isna(df.boxs)):
            if box_is_na or not box: continue
            image = cv.imread(os.path.join(images_dir, filename))
            assert image is not None
            box_f = elevate_df(pf.DataFrame.from_records(box))
            for idx, row in box_f.dropna(subset=box_cols).reset_index().iterrows():
                l, t = int(row.box__topLeft__x), int(row.box__topLeft__y + .5)
                r, b = int(row.box__buttonRight__x), int(row.box__buttonRight__y + .5)
                attr_f = elevate_df(pf.DataFrame.from_records(row["attrs"]))
                yield ((filename, idx), image[t:b, l:r], attr_f)
    else:
        box_cols = ['boxs__' + k for k in box_cols]
        for filename, box_f in df.groupby(by=df.index):
            image = cv.imread(os.path.join(images_dir, filename))
            assert image is not None
            for idx, attr_f in box_f.dropna(subset=box_cols).groupby(by="@boxs"):
                l = int(attr_f.boxs__box__topLeft__x.unique().item())
                t = int(attr_f.boxs__box__topLeft__y.unique().item())
                r = int(attr_f.boxs__box__buttonRight__x.unique().item() + .5)
                b = int(attr_f.boxs__box__buttonRight__y.unique().item() + .5)
                yield ((filename, idx), image[t:b, l:r], attr_f)


def crop_txt_images(df, image_files):
    r"""yield ((filename, box_i), cropped_image, box_r)"""

    import cv2 as cv

    for filename, box_f in df.reset_index().groupby(df.index):
        filepath = image_files[int(os.path.splitext(filename)[0])]
        image = cv.imread(filepath)
        assert image is not None
        for idx, row in box_f.iterrows():
            l, t = int(row.left), int(row.top + .5)
            r, b = int(row.right), int(row.bottom + .5)
            yield ((os.path.basename(filepath), idx), image[t:b, l:r], row)


if __name__ == '__main__':
    import sys

    helpstr = r"""
Usage:
    python3 label_process.py NonVehicleStructure.txt \
        'attrs.typeName == "不载人" and attrs.confidence > 0.5' \
        'attrs.typeName == "无雨棚"' \
        ...
    python2 label_process.py NonVehicleStructure.txt \
        'attrs.id == "zairen" and attrs.typeId == 1 and attrs.confidence > 0.5' \
        'attrs.id == "rainshade" and attrs.typeId == 1' \
        ...
    条件1：attrs.typeName == "不载人" and attrs.confidence > 0.5
    条件2：attrs.typeName == "无雨棚"
    ...
    过滤 包含 条件1 且 包含 条件2 的文件
    输出文件名
    """

    if len(sys.argv) < 3:
        sys.stderr.write(helpstr)
        sys.exit(0)

    filepath, = sys.argv[1:2]
    conditions = sys.argv[2:]
    df = load_json_labels(filepath)
    pred_s = joint_predicate(df, list(map(elevate_fields, conditions)))
    for i in pred_s.index[pred_s].unique():
        print(i)
