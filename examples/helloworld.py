#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

# only by importing to use
import pandas_should  # noqa


def check_null():
    """Is there null value? (null = NaN or NaT)"""
    data = [
        (1, 'alice', 20),
        (2, 'bob', None),
        (3, 'carol', 40),
    ]
    df = pd.DataFrame(data, columns=['id', 'name', 'age'])

    # there is null
    assert df.should.have_null()  # DataFrame
    assert df.age.should.have_null()  # Series

    # fill NaN
    df = df.fillna(-1)

    # no more exist
    assert df.should.have_not_null()  # DataFrame
    assert df.age.should.have_not_null()  # Series


def check_shape():
    """What is the shape of DataFrame?"""
    data = [
        (1, 'alice', 20),
        (2, 'bob', 30),
    ]
    df = pd.DataFrame(data, columns=['id', 'name', 'age'])

    # DataFrame
    assert df.should.be_shaped_like(2, 3)  # rows: 2, columns: 3
    assert df.should.be_shaped_like((2, 3))  # tuple
    assert df.should.shape(2, 3)  # alias

    # columns only
    assert df.should.have_width(3)
    assert df.should.columns_len(3)  # alias

    # rows only
    assert df.should.have_length(2)
    assert df.should.rows_len(2)  # alias

    # Series
    assert df.id.should.have_length(2)
    assert df.id.should.length(2)  # alias


def check_equal():
    """Does DataFrames equal?"""
    df1 = pd.DataFrame([1, 2, 3], columns=['id'])
    df2 = pd.DataFrame([1, 2, 3], columns=['id'])

    # DataFrame
    assert df1.should.equal(df2)  # does look the same?
    assert df1.should.eq(df2)  # alias
    assert df1.should.be_equal_to(df2)  # alias

    # Series
    assert df1.id.should.equal(df2.id)

    # does have same shape?
    assert df1.should.have_same_length(df2)
    assert df1.should.have_same_width(df2)

    # modify counter part
    df2 = pd.DataFrame([1, 2, 3, 4], columns=['id'])

    # DataFrame
    assert df1.should.not_equal(df2)  # doesn't look the same?
    assert df1.should.neq(df2)  # alias
    assert df1.should.be_not_equal_to(df2)  # alias

    # Series
    assert df1.id.should.not_equal(df2.id)


def check_value_range():
    """Does values fall within the range?"""
    series = pd.Series([0.0, 0.5, 0.1])

    assert series.should.fall_within_range(0, 1)
    assert series.should.value_range(0, 1)


def main():
    check_null()
    check_shape()
    check_equal()
    check_value_range()


if __name__ == '__main__':
    main()
