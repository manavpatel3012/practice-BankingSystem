# Basic Banking System

## Overview

This is a small, testable Python project that models a single bank account. It allows creating an account with a holder name and initial balance, checking the balance, depositing money, and withdrawing money. All operations validate inputs and reject invalid or out-of-range amounts.

## Features

- Create an account with a non-negative initial balance
- Check current balance without mutating state
- Deposit money (only positive numeric amounts)
- Withdraw money (only positive numeric amounts and when sufficient funds exist)
- Input validation and friendly error messages in the CLI app

## Project Structure

```text
practice-BankingSystem/
├── src/
│   ├── __init__.py
│   └── bank_account.py       # BankAccount class and simple CLI BankingApp
├── tests/
│   ├── __init__.py
│   ├── test_bank_account.py  # Unit tests for BankAccount
│   └── test_bankingapp.py    # Tests for the CLI flow and input parsing
└── README.md
```

## Requirements

- Python 3.8+ (3.11 used during development)
- `pytest` for running the test suite

## Running the app

From the repository root you can run the CLI banking app:

```bash
python -m src.bank_account
```

Or run the module file directly:

```bash
python src/bank_account.py
```

The CLI provides a small menu to view balance, deposit, withdraw, and exit.

## Running tests

Install pytest (if needed) and run:

```bash
pip install pytest
pytest -q
```

## Design notes

- Core behavior is implemented in the `BankAccount` class so it can be tested independently of input/output. The `BankingApp` class contains only CLI I/O and calls into `BankAccount` methods. Validation is performed in `BankAccount` and handled in `BankingApp` so errors are printed instead of crashing the app.

If you want me to add a small requirements file or CI config, say the word and I will add it.
