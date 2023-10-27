from web3 import Web3

web3 = Web3(Web3.HTTPProvider('https://sepolia.infura.io/v3/08edb8a4409e4850b41de1c792e3808a'))

# my contract info
contract_abi = [{"anonymous": False,"inputs":[{"indexed": True,"internalType":"address","name":"owner","type":"address"},{"indexed": True,"internalType":"address","name":"spender","type":"address"},{"indexed": False,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous": False,"inputs":[{"indexed": True,"internalType":"address","name":"from","type":"address"},{"indexed": True,"internalType":"address","name":"to","type":"address"},{"indexed": False,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"burn","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"mint","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"}]
contract_address = '0xC202b041D143beb4622273F718B3f7a7F07B2dD4'
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# my account
account = '0xb6e26f5a256c7fc229Dd74784C5A5bEDD0BA377e'

# testing my contract
token_balance = contract.functions.balanceOf(account).call()
print(f'my balance: {token_balance}')
print(contract.functions.name().call())

# transfer erc-20
private_key = 'secret'
nonce = web3.eth.get_transaction_count(account)
tx = contract.functions.transfer(account, 1).build_transaction({
    'gas': 2000000,
    'gasPrice': web3.eth.gas_price,
    'nonce': nonce,}
)
signed_tx = web3.eth.account.sign_transaction(tx, private_key)
tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
print(f'ERC-20 transfer tx hash: {web3.to_hex(tx_hash)}')
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
print(f'Receipt: {tx_receipt}')

# events
event = contract.events.Transfer().get_logs(fromBlock='latest')
print(f'Your event: {event}')

# subscribing to events
event_filter = contract.events.Transfer().create_filter(fromBlock='latest')
for i in event_filter.get_new_entries():
    print(f'New event: {i}')
