from bloomdata.wallet import Wallet
import pytest

@pytest.fixture
def empty_wallet():
    return Wallet()

@pytest.fixture 
def wallet_20():
    return Wallet(20)



def test_empty_wallet(empty_wallet):
    assert empty_wallet.balance == 0

def test_wallet_20_spend10(wallet_20):
    assert wallet_20.spend_cash(10) == 'remaining balance is $10'
    

def test_overspend():
    assert Wallet(10).spend_cash(30) == 'Not enough money'

def test_spend_all():
    assert Wallet(10).spend_cash(10) == 'remaining balance is $0'