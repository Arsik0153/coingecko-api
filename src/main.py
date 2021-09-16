from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

def print_coin(coin):
    print(coin['symbol'], "--- current price: ", coin['current_price'], "$")

while True:
    n = int(input("Enter number to filter: "))
    coin_list = cg.get_coins_markets("usd")[:n]
    for coin in coin_list:
        print_coin(coin)