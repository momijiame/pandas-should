# -*- coding: utf-8 -*-

import pandas as pd
from pandas.util.testing import assert_frame_equal


class EqualAccessorMixin(object):

    def equal(self, other_df):
        try:
            assert_frame_equal(self.df_, other_df)
        except AssertionError:
            return False
        return True

    # alias
    be_equal_to = be_equals_to = be_eq_to = eq = equal

    def not_equal(self, other_df):
        return not self.equal(other_df)

    # alias
    be_not_equal_to = be_not_equals_to = be_neq_to = neq = not_equal

    def have_same_length(self, other_df, *args):
        if len(args) < 1:
            return len(self.df_) == len(other_df)

        total_length = sum(len(df) for df in args)
        total_length += len(other_df)
        return len(self.df_) == total_length

    def have_same_width(self, other_df, *args):
        if len(args) < 0:
            return len(self.df_.columns) == len(other_df.columns)

        total_width = sum(len(df.columns) for df in args)
        total_width += len(other_df.columns)
        return len(self.df_.columns) == total_width


class NullAccessorMixin(object):

    def have_null(self, count=False):
        have_null_ = self.df_.isnull().any(axis=None)

        if not count:
            return have_null_

        count = dict(self.df_.isnull().sum())

        return have_null_, count

    def have_not_null(self):
        have_null_ = self.df_.isnull().any(axis=None)
        return not have_null_

    # alias
    havent_null = have_not_null


class ShapeAccessorMixin(object):

    def be_shaped_like(self, rows=None, columns=None):
        if isinstance(rows, pd.DataFrame):
            return self.df_.shape == rows.shape

        if isinstance(rows, tuple):
            return self.df_.shape == rows

        if rows is not None and columns is not None:
            return self.df_.shape == (rows, columns)

        if rows is not None:
            return self.df_.shape[0] == rows

        if columns is not None:
            return self.df_.shape[1] == columns

        raise ValueError('need \'rows\' or \'columns\'')

    # alias
    shape = be_shaped_like

    def have_width(self, expect):
        column_len = self.df_.shape[1]
        return column_len == expect

    # alias
    columns = columns_len = have_length_of_columns = have_width

    def have_length(self, expect):
        row_len = self.df_.shape[0]
        return row_len == expect

    # alias
    rows = rows_len = have_length_of_rows = have_length


class ValueRangeAccessorMixin(object):

    def fall_within_range(self, range_min, range_max):
        if (self.df_ < range_min).any(axis=None):
            return False

        if (self.df_ > range_max).any(axis=None):
            return False

        return True

    # alias
    value_range = fall_within_range

    def greater_than(self, min_value):
        if (self.df_ <= min_value).any(axis=None):
            return False

        return True

    # alias
    gt = greater_than

    def greater_than_or_equal(self, min_value):
        if (self.df_ < min_value).any(axis=None):
            return False

        return True

    # alias
    gte = greater_than_or_equal

    def less_than(self, max_value):
        if (self.df_ >= max_value).any(axis=None):
            return False

        return True

    # alias
    lt = less_than

    def less_than_or_equal(self, max_value):
        if (self.df_ > max_value).any(axis=None):
            return False

        return True

    # alias
    lte = less_than_or_equal


@pd.api.extensions.register_dataframe_accessor('should')
class ShouldDataFrameAccessor(EqualAccessorMixin,
                              NullAccessorMixin,
                              ShapeAccessorMixin,
                              ValueRangeAccessorMixin):

    def __init__(self, df):
        self.df_ = df
