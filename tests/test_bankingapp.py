import builtins

import pytest

from src.bank_account import BankAccount, BankingApp


def test_init_stores_account():
    account = BankAccount("Alice", 100)
    app = BankingApp(account)

    assert app.account is account


def test_show_menu_prints_options(capsys):
    app = BankingApp(BankAccount("Alice", 100))

    app.show_menu()

    captured = capsys.readouterr()
    assert "Banking App Menu:" in captured.out
    assert "1. View Balance" in captured.out
    assert "4. Exit" in captured.out


def test_get_amount_input_parses_numeric_value(monkeypatch):
    app = BankingApp(BankAccount("Alice", 100))
    monkeypatch.setattr(builtins, "input", lambda prompt="": "42.5")

    amount = app.get_amount_input("Enter amount: ")

    assert amount == 42.5


def test_get_amount_input_returns_none_on_invalid_input(monkeypatch, capsys):
    app = BankingApp(BankAccount("Alice", 100))
    monkeypatch.setattr(builtins, "input", lambda prompt="": "not-a-number")

    amount = app.get_amount_input("Enter amount: ")

    assert amount is None
    assert "Invalid input. Please enter a numeric value." in capsys.readouterr().out


def test_run_processes_deposit_withdraw_and_exit(monkeypatch, capsys):
    account = BankAccount("Alice", 100)
    app = BankingApp(account)

    inputs = iter(["2", "50", "3", "25", "4"])
    monkeypatch.setattr(builtins, "input", lambda prompt="": next(inputs))

    app.run()

    captured = capsys.readouterr()
    assert "Deposit successful." in captured.out
    assert "Withdrawal successful." in captured.out
    assert account.get_balance() == 125


def test_run_handles_invalid_numeric_deposit(monkeypatch, capsys):
    account = BankAccount("Alice", 100)
    app = BankingApp(account)

    inputs = iter(["2", "-5", "4"])
    monkeypatch.setattr(builtins, "input", lambda prompt="": next(inputs))

    app.run()

    captured = capsys.readouterr()
    assert "Deposit amount must be positive." in captured.out
    assert account.get_balance() == 100
