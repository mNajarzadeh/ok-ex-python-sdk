from okex import Pro


def read_secrets(file_path):
    secrets = {}
    with open(file_path, 'r') as file:
        for line in file:
            key, value = line.strip().split('=')
            secrets[key] = value
    return secrets


keys = read_secrets('secrets.txt')
pro = Pro(api_key=keys.get('API_KEY'), secret_key=keys.get('SECRET_KEY'))
print(pro.available_coin())
print(pro.coin_details("USDT-IRT"))
print(pro.orderbooks("USDT-IRT"))
print(pro.trade_history("USDT-IRT"))
print(pro.user_open_orders())
print(pro.user_trade_history())
