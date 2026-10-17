# ASE Calculator – Automated Testing Demo

[![CI – Lint & Test](https://github.com/<YOUR_USERNAME>/<YOUR_REPO>/actions/workflows/ci.yml/badge.svg)](https://github.com/<YOUR_USERNAME>/<YOUR_REPO>/actions/workflows/ci.yml)

A simple Python calculator project that demonstrates **automated testing** and
**Continuous Integration (CI)** using GitHub Actions.

---

## Project Structure

```
ase/
├── calculator.py          # Source module – arithmetic functions
├── test_calculator.py     # Unit tests (unittest)
├── requirements.txt       # Python dependencies
├── setup.cfg              # Project metadata + flake8 config
├── pyproject.toml         # Build system config
├── .flake8                # Linter configuration
└── .github/
    └── workflows/
        └── ci.yml         # GitHub Actions CI pipeline
```

---

## Functions

| Function | Description |
|---|---|
| `add(a, b)` | Returns `a + b` |
| `subtract(a, b)` | Returns `a - b` |
| `multiply(a, b)` | Returns `a * b` |
| `divide(a, b)` | Returns `a / b` (raises `ValueError` if `b == 0`) |
| `power(base, exp)` | Returns `base ** exp` |
| `modulo(a, b)` | Returns `a % b` (raises `ValueError` if `b == 0`) |

---

## Running Tests Locally

```bash
# Install linter
pip install flake8

# Run linter
flake8 .

# Run unit tests (built-in)
python -m unittest discover -v

# Run with pytest (richer output)
pip install pytest pytest-cov
pytest test_calculator.py -v --cov=calculator --cov-report=term-missing
```

---

## GitHub Actions CI Pipeline

The workflow (`.github/workflows/ci.yml`) triggers on **every push** and
**pull request** to any branch. It:

1. **Checks out** the repository.
2. **Sets up Python** (3.10, 3.11, 3.12 matrix).
3. **Installs dependencies** (`flake8`, etc.).
4. **Runs flake8** linting – fails on syntax errors / undefined names.
5. **Runs unit tests** via `python -m unittest`.
6. **Runs pytest** with coverage report.

> **Replace** `<YOUR_USERNAME>/<YOUR_REPO>` in the badge URL with your actual
> GitHub username and repository name.

---

## Setup & Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit: calculator module with unit tests and CI"
git remote add origin https://github.com/<YOUR_USERNAME>/<YOUR_REPO>.git
git branch -M main
git push -u origin main
```

Once pushed, go to **Actions** tab in your GitHub repository to see the
workflow running automatically.
