from locale import currency
from urllib import response
import requests
coinsList = None
currency = "pln"
def getCoinsList():
    global coinsList
    response = requests.get("https://api.coingecko.com/api/v3/coins/list?include_platform=true")
    if response.ok == True:
        print("response ok")
        data = response.json()
        print(data[0])
        print("Ilość kryptowalut:" + str(len(data)))
        coinsList = data

def findCoinBySymbol(symbol):
    symbol = symbol.lower().strip()
    for coin in coinsList:
        if coin["symbol"] == symbol:
            return coin
    else:
        return None

def getCoinLastMarketData(coinId):
    #{'bitcoin': {'pln': 107722, 'pln_24h_vol': 204580683180.28757, 'pln_24h_change': -10.870849737076933, 'last_updated_at': 1655112433}}#
    response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids="+coinId+"&vs_currencies="+currency+"&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true")
    if response.ok == True:
        data = response.json()
        return data
    else:
        return None

def getCoinPriceInCurrency(coinId, currency):
    currency = currency.lower().strip()
    marketData = getCoinLastMarketData(coinId)
    return marketData[coinId][currency]







getCoinsList()   
btcData = findCoinBySymbol("btc")
print(btcData)
marketData = getCoinLastMarketData(btcData["id"])
print("marketData:", marketData)
coinPrice = getCoinPriceInCurrency(btcData["id"], currency)
print("Coin price in" + currency, coinPrice)


print("\n Witamy w crypto exchange")
while True:
    cryptoSymbolToBuy = input("Wybierz symbol krypto do kupienia np btc lub exit aby zakończyć: ")
    if cryptoSymbolToBuy == "exit":
        break
    coinData = findCoinBySymbol(cryptoSymbolToBuy)
    if coinData == None:
        print("Nie ma takiej kryptowaluty")
        continue
    coinPrice = getCoinPriceInCurrency(coinData["id"], currency)
    print("Cena" + str(coinData["id"])  ,coinPrice, currency)

    moneyToBuyCrypto = float(input("Ile chcesz przeznaczyć na zakup: "))
    boughtCrypto = moneyToBuyCrypto / coinPrice
    print("\n Gratulacje kupiłeś " + str(boughtCrypto) + " " + cryptoSymbolToBuy)

