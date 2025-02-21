from okex import Pro, Otc, Wallet,OrderType, Side, Mode

def read_secrets(file_path):
    secrets = {}
    with open(file_path, 'r') as file:
        for line in file:
            key, value = line.strip().split('=')
            secrets[key] = value
    return secrets


keys = read_secrets('secrets.txt')
pro = Pro(api_key=keys.get('API_KEY'), secret_key=keys.get('SECRET_KEY'))
otc = Otc(api_key=keys.get('API_KEY'), secret_key=keys.get('SECRET_KEY'))
wallet = Wallet(api_key=keys.get('API_KEY'), secret_key=keys.get('SECRET_KEY'))
print(pro.available_coin())
# print(pro.coin_details("USDT-IRT"))
# print(pro.orderbooks("USDT-IRT"))
# print(pro.trade_history("USDT-IRT"))
# print(pro.user_open_orders())
# print(pro.user_trade_history())
# print(otc.available_otc_coin())
# print(otc.otc_coin_details("xrp"))
# print(otc.otc_estimate("USDT",1, Side.BUY, Mode.AMOUNT) )
# print(otc.otc_estimate_public("USDT",1, Side.BUY, Mode.AMOUNT) )
# print(otc.trade_otc_history(Side.BUY) )
# print(wallet.balance())
# print(wallet.get_address("USDT","TRC20"))
# print(wallet.deposit_history())
# print(wallet.withdrawal("BTC","0.001","dsadsadsa","BTC"))
# print(wallet.withdrawal_history())
# print(wallet.wallet_transfer("USDT","0.001","OTC","TRADE"))
# print(wallet.transfer_history())
