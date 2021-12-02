from brownie import FundMe
from scripts.helpful_scripts import get_account


def fund():
    fund_me = FundMe[-1]  # ostatni zdeployowany kontrakt FundMe
    account = (
        get_account()
    )  # ustawia konto w zależności od środowiska (local, testnet etc.)
    entrance_fee = fund_me.getEntranceFee()
    print(entrance_fee)
    print(f"The current entry fee is {entrance_fee}")
    print("Funding")
    fund_me.fund({"from": account, "value": entrance_fee * 2})


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})
    print("Withdrew full balance.")


def main():
    fund()
    withdraw()
