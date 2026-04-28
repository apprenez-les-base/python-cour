````md
# Python: Tuples, Sets and Dictionaries

## Commented Lines

In Python, the `#` symbol is used to comment a line.  
A commented line is not executed.

---

## Example 1: Tuple

```python
nombres = (1, 2, 3, 4, 5)

print(nombres.count(3))
````

### Explanation

* `(1, 2, 3, 4, 5)` is a **tuple**
* A tuple is a collection that **cannot be modified**
* `count(3)` counts how many times the number `3` appears

### Output

```python
1
```

---

## Example 2: Set

```python
nombre = {1, 3, 5, 4, 2}

nombre.remove(3)

nombre.add(6)

print(nombre)
```

### Explanation

* `{}` can represent a **set**
* A set:

  * does not allow duplicates
  * has no fixed order

### Methods Used

* `remove(3)` removes the value `3`
* `add(6)` adds the value `6`

### Possible Output

```python
{1, 2, 4, 5, 6}
```

> The order may change because sets are unordered.

---

## Example 3: Difference Between Sets

```python
set_1 = {0, 1, 2}
set_2 = {2, 3, 4}

print(set_1.difference(set_2))
```

### Explanation

`difference()` returns values that exist in `set_1` but not in `set_2`

### Comparison

* `set_1 = {0,1,2}`
* `set_2 = {2,3,4}`

The number `2` exists in both sets.

### Output

```python
{0, 1}
```

---

## Example 4: dir()

```python
print(dir(set_2))
```

### Explanation

`dir()` shows all available methods for an object.

For a set, examples include:

```python
add
remove
clear
copy
difference
intersection
union
pop
update
```

Useful for discovering object methods.

---

## Example 5: Dictionary

```python
nombre = {"un": 1, "deux": 2, "trois": 3}
```

### Explanation

This is a **dictionary** (`dict`)

It stores:

* a **key**
* a **value**

Examples:

* `"un"` → `1`
* `"deux"` → `2`

---

## Example 6: Remove an Item

```python
nombre.pop("trois")
```

### Explanation

Removes the key `"trois"` and its value.

### Before

```python
{
 "un":1,
 "deux":2,
 "trois":3
}
```

### After

```python
{
 "un":1,
 "deux":2
}
```

---

## Example 7: Show Values

```python
print(nombre.values())
```

### Output

```python
dict_values([1, 2])
```

Displays only the dictionary values.

---

# Quick Summary

| Python Type | Example   | Description           |
| ----------- | --------- | --------------------- |
| Tuple       | `(1,2,3)` | Immutable collection  |
| List        | `[1,2,3]` | Modifiable collection |
| Set         | `{1,2,3}` | No duplicates         |
| Dictionary  | `{"a":1}` | Key / Value pairs     |

---

# Full Working Code

```python
nombres = (1, 2, 3, 4, 5)
print(nombres.count(3))

nombre = {1, 3, 5, 4, 2}
nombre.remove(3)
nombre.add(6)
print(nombre)

set_1 = {0, 1, 2}
set_2 = {2, 3, 4}
print(set_1.difference(set_2))

nombre = {"un": 1, "deux": 2, "trois": 3}
nombre.pop("trois")
print(nombre.values())
```

```
```
