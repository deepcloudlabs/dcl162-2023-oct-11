import pytest
from banking.account import AccountStatus, CheckingAccount, InsufficientBalanceError

test_failure_amounts = [
    (0.0), (-0.1), (-1)
]
test_failure_overdraft_amounts = [
    (1200.1), (1201), (1300)
]
test_success_amounts = [
    (1000, 0.0), (1, 999.0), (1001, -1), (1200, -200)
]


@pytest.fixture
def an_active_checking_account():
    print("Creating a checking account for unit test...")
    return CheckingAccount("TR1", 1000, AccountStatus.ACTIVE, 200)


@pytest.mark.parametrize("amount", test_failure_amounts)
def test_withdraw_illegal_amount_should_raise_error(an_active_checking_account, amount):
    with pytest.raises(ValueError):
        an_active_checking_account.withdraw(amount)


@pytest.mark.parametrize("amount", test_failure_overdraft_amounts)
def test_withdraw_over_limit_should_raise_error(an_active_checking_account, amount):
    with pytest.raises(InsufficientBalanceError):
        an_active_checking_account.withdraw(amount)


@pytest.mark.parametrize("amount,expected", test_success_amounts)
def test_withdraw_within_limits_should_success(an_active_checking_account, amount, expected):
    an_active_checking_account.withdraw(amount)
    assert an_active_checking_account.balance == expected