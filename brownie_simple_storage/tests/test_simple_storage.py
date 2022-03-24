from brownie import SimpleStorage, accounts


def test_deploy():
    # 1. Arrange
    account = accounts[0]
    # 2. Act
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 0
    # 3. Assert
    assert starting_value == expected


def test_updating_storage():
    # 1. Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    # 2. Act
    expected = 8
    simple_storage.store(expected, {"from": account})
    # 3. Assert
    assert expected == simple_storage.retrieve()
