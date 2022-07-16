from brownie import network, config, accounts, MockV3Aggregator


FORK_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]

DECIMALS = 8
STARTING_PRICE = 120000000000


def get_account():
    print(f"get_account----The active network is {network.show_active()}")
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORK_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    # print(f"deploy_mocks----The active network is {network.show_active()}")
    if len(MockV3Aggregator) <= 0:
        print("deploying Mocks...")
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})

    print("Mocks Deployed!")
