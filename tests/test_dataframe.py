#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

import pandas as pd

import pandas_should  # noqa


class TestEqualAccessorMixin(object):

    def test_equal_true(self):
        df1 = pd.DataFrame([1, 2, 3], columns=['id'])
        df2 = pd.DataFrame([1, 2, 3], columns=['id'])
        assert df1.should.equal(df2)

    def test_equal_false(self):
        df1 = pd.DataFrame([1, 2, 3], columns=['id'])
        df2 = pd.DataFrame([1, 2, 3, 4], columns=['id'])
        assert not df1.should.equal(df2)

    @pytest.mark.parametrize('alias_name', [
        'be_equal_to', 'be_equals_to', 'be_eq_to', 'eq',
    ])
    def test_qeual_aliases(self, alias_name):
        df = pd.DataFrame([1, 2, 3], columns=['id'])
        assert hasattr(df.should, alias_name)

    def test_not_equal_true(self):
        df1 = pd.DataFrame([1, 2, 3], columns=['id'])
        df2 = pd.DataFrame([1, 2, 3, 4], columns=['id'])
        assert df1.should.not_equal(df2)

    def test_not_equal_false(self):
        df1 = pd.DataFrame([1, 2, 3], columns=['id'])
        df2 = pd.DataFrame([1, 2, 3], columns=['id'])
        assert not df1.should.not_equal(df2)

    @pytest.mark.parametrize('alias_name', [
        'be_not_equal_to', 'be_not_equals_to', 'be_neq_to', 'neq',
    ])
    def test_not_qeual_aliases(self, alias_name):
        df = pd.DataFrame([1, 2, 3], columns=['id'])
        assert hasattr(df.should, alias_name)


class TestNullAccessorMixin(object):

    def test_have_null_true(self):
        data = [
            (1, 'alice', 20),
            (2, 'bob', None),
            (3, 'carol', 40),
        ]
        df = pd.DataFrame(data, columns=['id', 'name', 'age'])
        assert df.should.have_null()

    def test_have_null_false(self):
        data = [
            (1, 'alice', 20),
            (2, 'bob', 30),
            (3, 'carol', 40),
        ]
        df = pd.DataFrame(data, columns=['id', 'name', 'age'])
        assert not df.should.have_null()

    def test_have_null_count(self):
        data = [
            (1, 'alice', 20),
            (2, 'bob', None),
            (3, 'carol', 40),
        ]
        df = pd.DataFrame(data, columns=['id', 'name', 'age'])
        assert df.should.have_null(count=True) == (True, {'age': 1, 'id': 0, 'name': 0})

    def test_have_not_null_true(self):
        data = [
            (1, 'alice', 20),
            (2, 'bob', 30),
            (3, 'carol', 40),
        ]
        df = pd.DataFrame(data, columns=['id', 'name', 'age'])
        assert df.should.have_not_null()

    def test_have_not_null_false(self):
        data = [
            (1, 'alice', 20),
            (2, 'bob', None),
            (3, 'carol', 40),
        ]
        df = pd.DataFrame(data, columns=['id', 'name', 'age'])
        assert not df.should.have_not_null()

    @pytest.mark.parametrize('alias_name', ['havent_null'])
    def test_have_not_null_aliases(self, alias_name):
        df = pd.DataFrame([1, 2, 3], columns=['id'])
        assert hasattr(df.should, alias_name)


class TestShapeAccessorMixin(object):

    @pytest.mark.parametrize('df, shape', [
        (pd.DataFrame([1, 2, 3], columns=['id']), (3, 1)),
        (pd.DataFrame([(1, 'a'), (2, 'b')], columns=['id', 'name']), (2, 2)),
    ])
    def test_be_shaped_like_tuple(self, df, shape):
        assert df.should.be_shaped_like(shape)

    @pytest.mark.parametrize('df, rows, columns', [
        (pd.DataFrame([1, 2, 3], columns=['id']), 3, 1),
        (pd.DataFrame([(1, 'a'), (2, 'b')], columns=['id', 'name']), 2, 2),
    ])
    def test_be_shaped_like(self, df, rows, columns):
        assert df.should.be_shaped_like(rows, columns)

    @pytest.mark.parametrize('alias_name', ['shape'])
    def test_be_shaped_like_aliases(self, alias_name):
        df = pd.DataFrame([1, 2, 3], columns=['id'])
        assert hasattr(df.should, alias_name)

    @pytest.mark.parametrize('df, length', [
        (pd.DataFrame([1, 2, 3], columns=['id']), 1),
        (pd.DataFrame([(1, 'a'), (2, 'b')], columns=['id', 'name']), 2),
    ])
    def test_have_length_of_columns(self, df, length):
        assert df.should.have_length_of_columns(length)

    @pytest.mark.parametrize('alias_name', ['columns', 'columns_len'])
    def test_have_length_of_columns_aliases(self, alias_name):
        df = pd.DataFrame([1, 2, 3], columns=['id'])
        assert hasattr(df.should, alias_name)

    @pytest.mark.parametrize('df, length', [
        (pd.DataFrame([1, 2, 3], columns=['id']), 3),
        (pd.DataFrame([(1, 'a'), (2, 'b')], columns=['id', 'name']), 2),
    ])
    def test_have_length_of_rows(self, df, length):
        assert df.should.have_length_of_rows(length)

    @pytest.mark.parametrize('alias_name', ['rows', 'rows_len'])
    def test_have_length_of_rows_aliases(self, alias_name):
        df = pd.DataFrame([1, 2, 3], columns=['id'])
        assert hasattr(df.should, alias_name)


class TestValueRangeAccessorMixin(object):

    @pytest.mark.parametrize('min_, max_, expect', [
        (0, 5, True),
        (1, 4, True),
        (2, 4, False),
        (1, 3, False),
    ])
    def test_fall_within_the_range(self, min_, max_, expect):
        data = [
            (1, 2),
            (3, 4),
        ]
        df = pd.DataFrame(data, columns=['a', 'b'])
        assert df.should.fall_within_the_range(min_, max_) == expect

    @pytest.mark.parametrize('alias_name', ['value_range'])
    def test_fall_within_the_range_aliases(self, alias_name):
        df = pd.DataFrame([1, 2, 3], columns=['id'])
        assert hasattr(df.should, alias_name)


if __name__ == '__main__':
    pytest.main(['-v', __file__])
