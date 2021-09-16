from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

def print_coin(coin):
    print(coin['symbol'], "--- current price: ", coin['current_price'], "$")

def sort_by_cap(e):
    return e['market_cap_rank']

while True:
    n = int(input("Enter number to filter: "))
    coin_list = cg.get_coins_markets("usd")[:n]
    coin_list.sort(key=sort_by_cap)
    for coin in coin_list:
        print_coin(coin)