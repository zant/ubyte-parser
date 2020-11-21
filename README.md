# ubyte-reader
Over-engineered Ubyte parser

Support for directly ubyte or .gz

## Usage

```python
from ubyte imoprt *
data = []

with UByte('train-labels-idx1-ubyte.gz', 'i', 10) as u:
    data = u.data
    
print(data) # Your data in a np's 10*28*28 ndarray
```

### Constructor

```python
UByte(path, mode, read)
```

Where
- path: The path your file is
- mode: 'i' for images and 'l' for labels
- read: How much stuff you want to parse
