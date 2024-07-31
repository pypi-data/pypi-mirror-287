# JsonEx

In this library, the creation of JSON has been improved where it previously returned errors.

From now on, attempting to save `list`, `dicts`, `set`, and custom objects to JSON should not cause any problems. For objects that cannot be formatted into JSON, 
the following value will be returned:

```python
f"[custom type: {type(value).__name__}]"
```

## Custom data auto convert:
```text
pandas DataFrame => dict
numpy ndarray => list
```

## Encode json
```python
from jsonex import JsonEx

JsonEx.dump({})
```

## Decode json
```python
from jsonex import JsonEx

json = JsonEx.dump({})

JsonEx.load(json)
```

## Example
```python
from jsonex import JsonEx
import numpy as np


class CustomObject:
    a: int
    b: int

df = np.DataSource()


CustomObject.a = 42
CustomObject.b = 33

data = [
    None,  # null in JSON
    True,  # boolean true in JSON
    False,  # boolean false in JSON
    123,  # integer (int)
    45.67,  # floating-point number (float)
    "text",  # string (str)
    [1, 2, 3],  # array (list)
    {"key": "value"},  # object (dict)
    (4, 5, 6),  # tuple
    {7, 8, 9},  # set
    # Additional examples for completeness
    456,  # another int
    78.9,  # another float
    "another text",  # another str
    [4, 5, 6],  # another list
    {"another_key": "another_value", "key2": (1, 2, 3)},  # another dict
    (10, 11, 12),  # another tuple
    {10, 11, 12},  # another set
    True,  # another bool
    CustomObject(),
    df,
    {"a", "b", "c"}
]
print(JsonEx.dump(data))

```
Zwróci:
```json
[null, true, false, 123, 45.67, "text", [1, 2, 3], {"key": "value"}, [4, 5, 6], [8, 9, 7], 456, 78.9, "another text", [4, 5, 6], {"another_key": "another_value", "key2": [1, 2, 3]}, [10, 11, 12], [10, 11, 12], true, "[custom type: CustomObject]", "[custom type: DataSource]", ["a", "b", "c"]]
```