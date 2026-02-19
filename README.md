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

| Category | Count | Tools That Catch It |
|-------------|-------|---------------------|
| LINTING | 2 | flake8 |
| SYNTAX | 2 | pytest (import/parse) |
| LOGIC | 3 | pytest (assertion) |
| TYPE_ERROR | 2 | mypy |
| IMPORT | 2 | pytest (ImportError) |
| INDENTATION | 2 | pytest (IndentationError) |
| **Total** | **14** | |

---

## Project Structure

```
├── src/
│   ├── __init__.py
│   ├── utils.py          # 3 bugs
│   ├── validator.py      # 3 bugs
│   ├── calculator.py     # 4 bugs
│   └── data_loader.py    # 4 bugs
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
- `src/data_loader.py`: `F401` unused import `re`, `W291` trailing whitespace

### mypy
- `src/calculator.py`: incompatible return type (annotated `int`, returns `float`)
- `src/data_loader.py`: incompatible parameter type (annotated `int`, used as `str`)

### pytest
- **ImportError** in `src/validator.py` — `from src.nonexistent import helper`
- **SyntaxError** in `src/validator.py` — missing colon on `def validate_age(age)`
- **SyntaxError** in `src/calculator.py` — `retrun` typo
- **IndentationError** in `src/calculator.py` — mixed tabs/spaces in `subtract`
- **IndentationError** in `src/data_loader.py` — block misalignment in `load_records`
- **AssertionError** in `test_utils.py` — `flatten_list` logic is inverted
- **AssertionError** in `test_calculator.py` — `multiply` returns sum instead of product
- **AssertionError** in `test_validator.py` — `validate_email` returns inverted result

---

## CI/CD Pipeline

The GitHub Actions workflow (`.github/workflows/ci.yml`) runs three jobs:

1. **Lint** — `flake8 src/`
2. **Type Check** — `mypy src/`
3. **Test** — `pytest tests/ -v`

All three jobs **will fail** on the initial commit. The pipeline passes only after all 14 bugs are fixed.

---

## License

This repository is created for hackathon evaluation purposes only.
