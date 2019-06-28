# -*- coding: utf-8 -*-

import pandas as pd
from pandas.util.testing import assert_series_equal


class EqualAccessorMixin(object):

    def equal(self, other_series):
        try:
            assert_series_equal(self.series_, other_series)
        except AssertionError:
            return False
        return True

    # alias
    be_equal_to = be_equals_to = be_eq_to = eq = equal

    def not_equal(self, other_series):
        return not self.equal(other_series)

    # alias
    be_not_equal_to = be_not_equals_to = be_neq_to = neq = not_equal


class NullAccessorMixin(object):

    def have_null(self, count=False):
        have_null_ = self.series_.isnull().any()

        if not count:
            return have_null_

        count = self.series_.isnull().sum()

        return have_null_, count

    def have_not_null(self):
        have_null_ = any(self.series_.isnull())
        return not have_null_

    # alias
    havent_null = have_not_null


class LengthAccessorMixin(object):

    def have_length(self, expect):
        length = len(self.series_)
        return length == expect

    # alias
    length = have_length


class ValueRangeAccessorMixin(object):

    def fall_within_the_range(self, min_, max_):
        if (self.series_ < min_).any():
            return False

        if (self.series_ > max_).any():
            return False

        return True

    # alias
    value_range = fall_within_the_range


class CardinalityAccessorMixin(object):

    def have_number_of_unique_values(self, size):
        number_of_unique_values = len(self.series_.unique())
        return number_of_unique_values == size

    # alias
    unique_values = have_number_of_unique_values


@pd.api.extensions.register_series_accessor('should')
class ShouldSeriesAccessor(EqualAccessorMixin,
                           NullAccessorMixin,
                           LengthAccessorMixin,
                           ValueRangeAccessorMixin,
                           CardinalityAccessorMixin):

    def __init__(self, series):
        self.series_ = series
