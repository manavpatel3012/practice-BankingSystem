import pytest

from src.bank_account import BankAccount


def test_constructor_stores_holder_name_and_balance():
    account = BankAccount("Alice", 100)

    assert account.account_holder == "Alice"
    assert account.get_balance() == 100


def test_constructor_rejects_negative_initial_balance():
    with pytest.raises(ValueError, match="Initial balance cannot be negative"):
        BankAccount("Alice", -50)


def test_constructor_rejects_empty_account_holder():
    with pytest.raises(ValueError, match="Account holder name cannot be empty"):
        BankAccount("", 50)


def test_deposit_increases_balance_for_positive_amount():
    account = BankAccount("Alice", 50)

    account.deposit(25)

    assert account.get_balance() == 75


def test_deposit_rejects_non_positive_amount_and_keeps_balance():
    account = BankAccount("Alice", 50)

    with pytest.raises(ValueError, match="Deposit amount must be positive"):
        account.deposit(0)

    assert account.get_balance() == 50


def test_withdraw_decreases_balance_for_valid_amount():
    account = BankAccount("Alice", 100)

    account.withdraw(40)

    assert account.get_balance() == 60


def test_withdraw_rejects_non_positive_amount_and_keeps_balance():
    account = BankAccount("Alice", 100)

    with pytest.raises(ValueError, match="Withdrawal amount must be positive"):
        account.withdraw(0)

    assert account.get_balance() == 100


def test_withdraw_rejects_insufficient_funds_and_keeps_balance():
    account = BankAccount("Alice", 30)

    with pytest.raises(ValueError, match="Insufficient funds"):
        account.withdraw(50)

    assert account.get_balance() == 30


def test_deposit_rejects_non_numeric_amount():
    account = BankAccount("Alice", 50)

    with pytest.raises(ValueError, match="Deposit amount must be a number"):
        account.deposit("not-a-number")


def test_withdraw_rejects_non_numeric_amount():
    account = BankAccount("Alice", 50)

    with pytest.raises(ValueError, match="Withdrawal amount must be a number"):
        account.withdraw(None)


def test_deposit_rejects_nan():
    import math
    account = BankAccount("Alice", 50)

    with pytest.raises(ValueError, match="valid number"):
        account.deposit(math.nan)


def test_withdraw_rejects_nan():
    import math
    account = BankAccount("Alice", 50)

    with pytest.raises(ValueError, match="valid number"):
        account.withdraw(math.nan)
