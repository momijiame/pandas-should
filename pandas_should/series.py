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

    def have_same_length(self, other_series, *args):
        if len(args) < 1:
            # single series
            return len(self.series_) == len(other_series)

        # multiple series
        total_length = sum(len(s) for s in args)
        total_length += len(other_series)
        return len(self.series_) == total_length


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

    def fall_within_range(self, range_min, range_max):
        if (self.series_ < range_min).any():
            return False

        if (self.series_ > range_max).any():
            return False

        return True

    # alias
    value_range = fall_within_range

    def greater_than(self, min_value):
        if (self.series_ <= min_value).any():
            return False

        return True

    # alias
    gt = greater_than

    def greater_than_or_equal(self, min_value):
        if (self.series_ < min_value).any():
            return False

        return True

    # alias
    gte = greater_than_or_equal

    def less_than(self, max_value):
        if (self.series_ >= max_value).any():
            return False

        return True

    # alias
    lt = less_than

    def less_than_or_equal(self, max_value):
        if (self.series_ > max_value).any():
            return False

        return True

    # alias
    lte = less_than_or_equal


class ValueVarietyAccessorMixin(object):

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
                           ValueVarietyAccessorMixin):

    def __init__(self, series):
        self.series_ = series
