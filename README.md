# 🧪 CI/CD Healing Agent — Test Repository

> **This repository is NOT a working project.**  
> It is a structured **test case repository** containing controlled, intentional bugs designed for evaluating an **Autonomous CI/CD Healing Agent** in a DevOps AI hackathon.

## Purpose

An autonomous AI agent will:
1. Clone this repository
2. Discover tests automatically
3. Detect failures (lint, type, syntax, logic, import, indentation)
4. Apply fixes to source code
5. Commit and re-run the CI/CD pipeline until all checks pass

All bugs are **deterministic** and **reproducible** — each has exactly one correct fix.

---

## Intentional Bug Categories

| Category | Count | File | Tools That Catch It |
|-------------|-------|------|---------------------|
| LINTING | 1 | `src/utils.py` | flake8 |
| IMPORT | 1 | `src/utils.py` | pytest (ImportError) |
| LOGIC | 1 | `src/utils.py` | pytest (assertion) |
| SYNTAX | 1 | `src/validator.py` | pytest (parse) |
| INDENTATION | 1 | `src/calculator.py` | pytest (IndentationError) |
| TYPE_ERROR | 1 | `src/calculator.py` | mypy |
| **Total** | **6** | | |

---

## Project Structure

```
├── src/
│   ├── __init__.py
│   ├── utils.py          # 3 bugs (LINTING, IMPORT, LOGIC)
│   ├── validator.py      # 1 bug  (SYNTAX)
│   ├── calculator.py     # 2 bugs (INDENTATION, TYPE_ERROR)
│   └── data_loader.py    # 0 bugs
├── tests/
│   ├── __init__.py
│   ├── test_utils.py
│   ├── test_validator.py
│   └── test_calculator.py
├── .github/workflows/
│   └── ci.yml
├── requirements.txt
└── README.md
```

---

## Run Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Linting (will fail)
flake8 src/ --max-line-length=120

# Type checking (will fail)
mypy src/ --ignore-missing-imports

# Tests (will fail)
pytest tests/ -v
```

---

## Expected Failing Behavior (Before Fixes)

### flake8
- `src/utils.py`: `F401` unused import `os`

### mypy
- `src/calculator.py`: incompatible return type (annotated `int`, returns `float`)

### pytest
- **ImportError** in `src/utils.py` — `namedtple` typo in import
- **SyntaxError** in `src/validator.py` — missing colon on `def validate_age(age)`
- **IndentationError** in `src/calculator.py` — mixed tabs/spaces in `subtract`
- **AssertionError** in `test_utils.py` — `flatten_list` logic is inverted

---

## CI/CD Pipeline

The GitHub Actions workflow (`.github/workflows/ci.yml`) runs three jobs:

1. **Lint** — `flake8 src/`
2. **Type Check** — `mypy src/`
3. **Test** — `pytest tests/ -v`

All three jobs **will fail** on the initial commit. The pipeline passes only after all 6 bugs are fixed.

---

## License

This repository is created for hackathon evaluation purposes only.
