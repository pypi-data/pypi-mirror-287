# refdatatypes

Pyton basic datatypes as a references. Solve problems with static class immutable datatypes.

## Installation
```python
pip3 install refdatatypes
```

## Problem

```python
class A:
    static = 1


class B(A):
    pass


print(f"int {A.static}")  # get 1 correctly
print(f"int {B.static}")  # get 1 correctly

A.static = 5
print(f"int {A.static}")  # get 5 correctly
print(f"int {B.static}")  # get 5 correctly

B.static = 6
print(f"int {A.static}")  # expected 6, but get 5 incorrectly
print(f"int {B.static}")  # get 6 correctly

A.static = 7
print(f"int {A.static}")  # get 7 correctly
print(f"int {B.static}")  # expected 7, but get unchanged 6, incorrectly
```

## Solution
```python
from refdatatypes.refint import RefInt


class AAA:
    static = RefInt(1)


class BBB(AAA):
    pass


print(f"refint {AAA.static.value}")  # get 1 correctly
print(f"refint {BBB.static.value}")  # get 1 correctly

AAA.static.value = 5
print(f"refint {AAA.static.value}")  # get 5 correctly
print(f"refint {BBB.static.value}")  # get 5 correctly

BBB.static.value = 6
print(f"refint {AAA.static.value}")  # get 6 correctly
print(f"refint {BBB.static.value}")  # get 6 correctly

AAA.static.value = 7
print(f"refint {AAA.static.value}")  # get 7 correctly
print(f"refint {BBB.static.value}")  # get 7 correctly
```

More details you can find in included examples [static_class_attribute_problem.py](https://gitlab.com/alda78/refdatatypes/-/blob/main/examples/static_class_attribute_problem.py) 
and [static_class_attribute_solution.py](https://gitlab.com/alda78/refdatatypes/-/blob/main/examples/static_class_attribute_solution.py) .

## Safe datatypes
`safedatatypes` is simple set of function and classes which enables
you to work safely with base python datatypes without error falls during
convert or item access.

### example
```python
from refdatatypes.safedatatypes import safe_int

my_int = safe_int("None")  # no error
print(my_int)  # prints: `0`
```

### example 2
```python
from refdatatypes.safedatatypes import SafeDict

my_dict = SafeDict()
my_dict["a"] = 1

print(my_dict["a"])  # prints: `1` 
print(my_dict["b"])  # prints: `None` with no error
print(my_dict)  # prints: `{'a': 1}`

my_dict = SafeDict({"a": 1}, default_value=-1, autoset=True)
print(my_dict["a"])  # prints: `1` 
print(my_dict["b"])  # prints: `-1` with no error
print(my_dict)  # prints: `{'a': 1, 'b': -1}`
```

### example 3
```python
# expected dict structure
my_dict = {"a": 1, "b": {"bb": 2}}
# but structure like this occured
my_dict = {"a": 1, "b": None}
# safe handle of this structure
result = my_dict.get("b") or {}
result = result.get("bb") or 0
print(result)  # prints: `0` with no error
```
Solution with SafeDict

```python
from refdatatypes.safedatatypes import SafeDict

# expected dict structure
my_dict = SafeDict({"a": 1, "b": {"bb": 2}})
# but structure like this occured
my_dict = SafeDict({"a": 1, "b": None})
# safe handle of this structure
result = my_dict.get("b", SafeDict(), if_none=True).get("bb", 0)
print(result)  # prints: `0` with no error
```

## Utils
### dict_item_must_be_list
This utility checks if item in combined structure of lists and dicts is realy list. If not, it converts it to list.
This utility is useful when you are working with `xmltodict` library.
You expect list in some dict structure place, but if there is only one item, it is converted to dict not into list, 
because for `xmltodict` is not possible know it should be list.
```python
from refdatatypes.utils import dict_item_must_be_list

d = {
    "a": 1,
    "b": {
        "bb": [
            {"ccc": {"ddd": 4}},
            {"ccc": [{"ddd": 4}, {"ddd": 4}]},
            {"ccc": 4},
            {"ccc": None},
            {"ccc": [1, 2, [11, 22]]},
        ]
    },
}
dict_item_must_be_list(d, "b.bb.ccc")
print(d)
```
```python
{
    'a': 1,
    'b': {
        'bb': [
            {'ccc': [{'ddd': 4}]},
            {'ccc': [{'ddd': 4}, {'ddd': 4}]},
            {'ccc': [4]},
            {'ccc': []},
            {'ccc': [1, 2, [11, 22]]}
        ]
    }
}
```