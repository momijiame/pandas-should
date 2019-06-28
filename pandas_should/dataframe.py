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

    def have_length_of_columns(self, expect):
        column_len = self.df_.shape[1]
        return column_len == expect

    # alias
    columns = columns_len = have_length_of_columns

    def have_length_of_rows(self, expect):
        row_len = self.df_.shape[0]
        return row_len == expect

    # alias
    rows = rows_len = have_length_of_rows


class ValueRangeAccessorMixin(object):

    def fall_within_the_range(self, min_, max_):
        if (self.df_ < min_).any(axis=None):
            return False

        if (self.df_ > max_).any(axis=None):
            return False

        return True

    # alias
    value_range = fall_within_the_range


@pd.api.extensions.register_dataframe_accessor('should')
class ShouldDataFrameAccessor(EqualAccessorMixin,
                              NullAccessorMixin,
                              ShapeAccessorMixin,
                              ValueRangeAccessorMixin):

    def __init__(self, df):
        self.df_ = df
