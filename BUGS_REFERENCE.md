# 🐛 Bug Reference — Cross-Check Sheet

> Use this file to verify that each intentional bug exists and maps to one deterministic fix.
> **Rule:** Each bug category appears **exactly once** across all files — no repeated categories.

---

## Bug #1 — LINTING · `src/utils.py` line 2

**Category:** LINTING (unused import)

```python
# Buggy (line 2):
import os

# Fix: Remove the entire line. `os` is never used.
```

---

## Bug #2 — IMPORT · `src/utils.py` line 3

**Category:** IMPORT (typo in module name)

```python
# Buggy (line 3):
from collections import namedtple

# Fix: Correct the typo:
from collections import namedtuple
```

---

## Bug #3 — LOGIC · `src/utils.py` lines 19–22

**Category:** LOGIC (swapped append/extend in flatten)

```python
# Buggy (lines 19–22):
if isinstance(item, list):
    result.append(item)        # ← should extend/recurse
else:
    result.extend(flatten_list(item))  # ← should append

# Fix: Swap the branches:
if isinstance(item, list):
    result.extend(flatten_list(item))
else:
    result.append(item)
```

---

## Bug #4 — SYNTAX · `src/validator.py` line 14

**Category:** SYNTAX (missing colon)

```python
# Buggy (line 14):
def validate_age(age)

# Fix: Add the colon:
def validate_age(age):
```

---

## Bug #5 — INDENTATION · `src/calculator.py` line 9

**Category:** INDENTATION (tab character mixed with spaces)

```python
# Buggy (line 9):
⇥return result      # ← starts with a TAB character

# Fix: Replace the tab with 4 spaces:
    return result
```

---

## Bug #6 — TYPE_ERROR · `src/calculator.py` line 17

**Category:** TYPE_ERROR (wrong return type annotation)

```python
# Buggy (line 17):
def divide(a: float, b: float) -> int:

# Fix: Change return type to float:
def divide(a: float, b: float) -> float:
```

---

## Summary Table

| # | File | Line | Category | Bug | Fix |
|---|------|------|----------|-----|-----|
| 1 | `src/utils.py` | 2 | LINTING | Unused `import os` | Remove line |
| 2 | `src/utils.py` | 3 | IMPORT | `namedtple` typo | → `namedtuple` |
| 3 | `src/utils.py` | 19–22 | LOGIC | Swapped append/extend | Swap branches |
| 4 | `src/validator.py` | 14 | SYNTAX | Missing colon | Add `:` |
| 5 | `src/calculator.py` | 9 | INDENTATION | Tab mixed with spaces | Use 4 spaces |
| 6 | `src/calculator.py` | 17 | TYPE_ERROR | `-> int` on divide | → `-> float` |

### By Category

| Category | Count | Bug |
|----------|-------|-----|
| LINTING | 1 | #1 |
| IMPORT | 1 | #2 |
| LOGIC | 1 | #3 |
| SYNTAX | 1 | #4 |
| INDENTATION | 1 | #5 |
| TYPE_ERROR | 1 | #6 |
| **Total** | **6** | |

### By File

| File | Categories | Bug Count |
|------|-----------|-----------|
| `src/utils.py` | LINTING, IMPORT, LOGIC | 3 |
| `src/validator.py` | SYNTAX | 1 |
| `src/calculator.py` | INDENTATION, TYPE_ERROR | 2 |
| `src/data_loader.py` | *(none)* | 0 |
