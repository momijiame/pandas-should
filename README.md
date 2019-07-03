# pandas-should

pandas-should is pandas extension for asserting.

### Install

Install and update released version using pip:

```sh
$ pip install pandas-should
```

If you want development version:

```sh
$ pip install git+https://github.com/momijiame/pandas-should.git
```

### Quickstart

You can just to import `pandas_should` to use:

```python
import pandas_should
```

#### DataFrame

##### Length (rows)

Before:

```python
assert len(df1) == len(df2)
```

After:

```python
assert df1.should.have_same_length(df2)
```

Or

```python
assert df1.should.have_length(len(df2))
```

Before (multiple DataFrame):

```python
assert len(df1) == (len(df2) + len(df3))
```

After (multiple DataFrame)

```python
assert df1.should.have_same_length(df2, df3)
```

##### Width (columns)

Before:

```python
assert len(df1.columns) == len(df2.columns)
```

After:

```python
assert df1.should.have_same_width(df2)
```

Or

```python
assert df1.should.have_width(len(df2.columns))
```

Before (multiple DataFrame):

```python
assert len(df1.columns) == (len(df2.columns)) + len(df3.columns)))
```

After (multiple DataFrame)

```python
assert df1.should.have_same_width(df2, df3)
```

##### Equality

Before:

```python
from pandas.util.testing import assert_frame_equal
def equal(a, b):
    try:
        assert_frame_equal(a, b)
    except AssertionError:
        return False
    return True

assert equal(df1, df2)
```

After:

```python
assert df1.should.equal(df2)
```

##### Null inclusion

Before:

```python
assert df.isnull().any(axis=None)
```

After:

```python
assert df.should.have_null()
```

Or expect not to be included:

```python
assert df.should.have_not_null()
assert not df.should.have_null()
```


##### Shape

Before:

```python
assert df1.shape == df2.shape
```

After:

```python
assert df1.should.be_shaped_like(df2)
```

Or

```python
assert df1.should.be_shaped_like(df2.shape)
assert df1.should.be_shaped_like(df2.shape[0], df2.shape[1])
```

##### Value range

Before:

```python
assert (df >= range_min).any(axis=None) and (df <= range_max).any(axis=None) 
```

After:

```python
assert df.should.fall_within_range(range_min, range_max)
```

Greater than only:

```python
assert df.should.greater_than(range_min)
assert df.should.greater_than_or_equal(range_min)
```

Less than only:

```python
assert df.should.less_than(range_min)
assert df.should.less_than_or_equal(range_min)
```

#### Series

##### Length

Before:

```python
assert len(s1) == len(s2)
```

After:

```python
assert s1.should.have_same_length(s2)
```

Or:

```python
assert s1.should.have_length(len(s2))
```

Before (multiple Series):

```python
assert len(s1) == (len(s2) + len(s3))
```

After (multiple Series):

```python
assert s1.should.have_same_length(s2, s3)
```

##### Equality

Before:

```python
from pandas.util.testing import assert_series_equal
def equal(a, b):
    try:
        assert_series_equal(a, b)
    except AssertionError:
        return False
    return True

assert equal(s1, s2)
```

After:

```python
assert s1.should.equal(s2)
```

##### Null inclusion

Before:

```python
assert s.isnull().any()
```

After:

```python
assert s.should.have_null()
```

Or expect not to be included:

```python
assert s.should.have_not_null()
assert not s.should.have_null()
```

##### Value range


Before:

```python
assert (s >= range_min).any() and (s <= range_max).any() 
```

After:

```python
assert s.should.fall_within_range(range_min, range_max)
```

Greater than only:

```python
assert s.should.greater_than(range_min)
assert s.should.greater_than_or_equal(range_min)
```

Less than only:

```python
assert s.should.less_than(range_min)
assert s.should.less_than_or_equal(range_min)
```

##### Value variety

Before:

```python
assert len(s.unique()) == expect_size
```

After:

```python
assert s.should.have_number_of_unique_values(expect_size)
```