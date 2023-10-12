"""
CUT: account
MUT: methods -> constructor (__init__), setter/getter, 
        business methods -> withdraw, deposit
        utility -> __str__, ...
Test Phases:
1) Fixture/Setup
2) Call exercise method (mut)
3) Verification
4) Teardown
"""
import pytest

from banking.account import Account, AccountStatus, InsufficientBalanceError

test_deposit_failure_amounts = [
    (0), (-0.1), (-1), (-100),(-1_000_000)
]


@pytest.fixture
def an_active_account() -> Account:
    return Account("tr42", 1_000, AccountStatus.ACTIVE)


@pytest.fixture
def a_closed_account() -> Account:
    return Account("tr42", 0, AccountStatus.CLOSED)


@pytest.fixture
def a_blocked_account() -> Account:
    return Account("tr42", 2_000, AccountStatus.BLOCKED)


@pytest.mark.parametrize("amount",test_deposit_failure_amounts)
def test_deposit_with_negative_amount_should_raise_value_error(an_active_account, amount):
    with pytest.raises(ValueError):
        an_active_account.deposit(amount)


def test_withdraw_with_zero_amount_should_raise_error(an_active_account):  # 1. test fixture
    with pytest.raises(ValueError):  # 3. verification
        an_active_account.withdraw(0.0)  # 2. call exercise method
    # 4. test teardown


def test_withdraw_with_over_balance_should_raise_error(an_active_account):  # 1. test fixture
    with pytest.raises(InsufficientBalanceError):  # 3. verification
        an_active_account.withdraw(1000.1)  # 2. call exercise method
    # 4. test teardown


def test_withdraw_all_balance_should_success(an_active_account):  # 1. test fixture
    an_active_account.withdraw(1000)  # 2. call exercise method
    assert an_active_account.balance == 0
    # 4. test teardown