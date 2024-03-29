#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

import pandas as pd

import pandas_should  # noqa


class TestEqualAccessorMixin(object):

    def test_equal_true(self):
        s1 = pd.Series([1, 2, 3])
        s2 = pd.Series([1, 2, 3])
        assert s1.should.equal(s2)

    def test_equal_false(self):
        s1 = pd.Series([1, 2, 3])
        s2 = pd.Series([1, 2, 3, 4])
        assert not s1.should.equal(s2)

    @pytest.mark.parametrize('alias_name', [
        'be_equal_to', 'be_equals_to', 'be_eq_to', 'eq',
    ])
    def test_qeual_aliases(self, alias_name):
        s = pd.Series([1, 2, 3])
        assert hasattr(s.should, alias_name)

    def test_not_equal_true(self):
        s1 = pd.Series([1, 2, 3])
        s2 = pd.Series([1, 2, 3, 4])
        assert s1.should.not_equal(s2)

    def test_not_equal_false(self):
        s1 = pd.Series([1, 2, 3])
        s2 = pd.Series([1, 2, 3])
        assert not s1.should.not_equal(s2)

    @pytest.mark.parametrize('alias_name', [
        'be_not_equal_to', 'be_not_equals_to', 'be_neq_to', 'neq',
    ])
    def test_not_qeual_aliases(self, alias_name):
        s = pd.Series([1, 2, 3])
        assert hasattr(s.should, alias_name)

    def test_have_same_length_true(self):
        s1 = pd.Series([1, 2, 3])
        s2 = pd.Series([1, 2, 3])
        assert s1.should.have_same_length(s2)

    def test_have_same_length_false(self):
        s1 = pd.Series([1, 2, 3])
        s2 = pd.Series([1, 2, 3, 4])
        assert not s1.should.have_same_length(s2)

    def test_have_same_length_multiple(self):
        s1 = pd.Series([1, 2, 3])
        s2 = pd.Series([1, 2])
        s3 = pd.Series([3])
        assert s1.should.have_same_length(s2, s3)


class TestNullAccessorMixin(object):

    def test_have_null_true(self):
        s = pd.Series([1, None, 3])
        assert s.should.have_null()

    def test_have_null_false(self):
        s = pd.Series([1, 2, 3])
        assert not s.should.have_null()

    def test_have_null_count(self):
        s = pd.Series([1, None, 3])
        assert s.should.have_null(count=True) == (True, 1)

    def test_have_not_null_true(self):
        s = pd.Series([1, 2, 3])
        assert s.should.have_not_null()

    def test_have_not_null_false(self):
        s = pd.Series([1, None, 3])
        assert not s.should.have_not_null()

    @pytest.mark.parametrize('alias_name', ['havent_null'])
    def test_have_not_null_aliases(self, alias_name):
        s = pd.Series([1, 2, 3])
        assert hasattr(s.should, alias_name)


class TestLengthAccessorMixin(object):

    @pytest.mark.parametrize('s, length', [
        (pd.Series([1, 2, 3]), 3),
        (pd.Series([1, 2]), 2),
    ])
    def test_have_length(self, s, length):
        assert s.should.have_length(length)

    @pytest.mark.parametrize('alias_name', ['length'])
    def test_have_length_aliases(self, alias_name):
        s = pd.Series([1, 2, 3])
        assert hasattr(s.should, alias_name)


class TestValueRangeAccessorMixin(object):

    @pytest.mark.parametrize('min_, max_, expect', [
        (0, 5, True),
        (1, 4, True),
        (2, 4, False),
        (1, 3, False),
    ])
    def test_fall_within_the_range(self, min_, max_, expect):
        data = [1, 2, 3, 4]
        s = pd.Series(data)
        assert s.should.fall_within_range(min_, max_) == expect

    @pytest.mark.parametrize('alias_name', ['value_range'])
    def test_fall_within_the_range_aliases(self, alias_name):
        s = pd.Series([1, 2, 3])
        assert hasattr(s.should, alias_name)

    def test_greater_than(self):
        s = pd.Series([1, 2, 3])

        assert s.should.greater_than(0)
        assert not s.should.greater_than(1)
        assert not s.should.greater_than(2)

    @pytest.mark.parametrize('alias_name', ['gt'])
    def test_greater_than_aliases(self, alias_name):
        s = pd.Series([1, 2, 3])
        assert hasattr(s.should, alias_name)

    def test_greater_than_or_equal(self):
        s = pd.Series([1, 2, 3])

        assert s.should.greater_than_or_equal(0)
        assert s.should.greater_than_or_equal(1)
        assert not s.should.greater_than_or_equal(2)

    @pytest.mark.parametrize('alias_name', ['gte'])
    def test_greater_than_or_equal_aliases(self, alias_name):
        s = pd.Series([1, 2, 3])
        assert hasattr(s.should, alias_name)

    def test_less_than(self):
        s = pd.Series([1, 2, 3])

        assert s.should.less_than(4)
        assert not s.should.less_than(3)
        assert not s.should.less_than(2)

    @pytest.mark.parametrize('alias_name', ['lt'])
    def test_less_than_aliases(self, alias_name):
        s = pd.Series([1, 2, 3])
        assert hasattr(s.should, alias_name)

    def test_less_than_or_equal(self):
        s = pd.Series([1, 2, 3])

        assert s.should.less_than_or_equal(4)
        assert s.should.less_than_or_equal(3)
        assert not s.should.less_than_or_equal(2)

    @pytest.mark.parametrize('alias_name', ['lte'])
    def test_less_than_or_equal_aliases(self, alias_name):
        s = pd.Series([1, 2, 3])
        assert hasattr(s.should, alias_name)


class TestCardinalityAccessorMixin(object):

    def test_have_number_of_unique_values(self):
        s = pd.Series([1, 2, 3])
        assert s.should.have_number_of_unique_values(3)
        assert not s.should.have_number_of_unique_values(2)

    @pytest.mark.parametrize('alias_name', ['unique_values'])
    def test_fall_within_the_range_aliases(self, alias_name):
        s = pd.Series([1, 2, 3])
        assert hasattr(s.should, alias_name)


if __name__ == '__main__':
    pytest.main(['-v', __file__])
