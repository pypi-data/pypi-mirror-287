# Rightpad
Right pad a string in Python. 
Created to try out making a `pip` package and uploading it to the [Python Package Index (PyPI)](https://pypi.org/).

# Install
`pip install rightpad`

# Usage
```python
from rightpad import right_pad

right_pad("foo", 5)
// => "foo  "

right_pad("foobar", 6)
// => "foobar"

right_pad(1, 2, '0')
// => "10"

right_pad(17, 5, 0)
// => "17000"
```

## Testing
Run `python -m doctest rightpad.py`.