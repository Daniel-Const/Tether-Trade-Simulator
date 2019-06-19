from pycoingecko import CoinGeckoAPI
import datetime


cg = CoinGeckoAPI()
date = []
yesterday = datetime.datetime.now()

for i in range(1, 365):
    nxtDate = yesterday - datetime.timedelta(i)
    nxtDate = nxtDate.strftime('%d-%m-%Y')
    date.insert(0, nxtDate)

res = cg.get_coin_history_by_id(id = 'tether', date= date[0], localization=False, vs_currencies='usd')
prev_buy_price = res['market_data']['current_price']['usd']
startPrice = 3000
amt = startPrice / prev_buy_price
money = 0
trades = 0
prev_trades = 0
count = 1

thresh = 0.001

for dt in date:

    res = cg.get_coin_history_by_id(id = 'tether', date= dt, localization=False, vs_currencies='usd')
    if 'market_data' not in res.keys():
        continue
    price = res['market_data']['current_price']['usd']
    if (prev_buy_price <  price - thresh and amt != 0):  #sell

        money = amt * (price - (price * 0.001))
        amt = 0
        trades += 1

    if (prev_buy_price > price + thresh and amt == 0) :  #buy
        amt = ((money - (money * 0.001)) * price)
        money = 0
        prev_buy_price

    if money > 0 and trades != prev_trades:
        print("============== trade# " + str(trades) + " ==============\n")
        print("Current_wallet:  " + str(money) + "\nProfit: " + str(money - startPrice) + "\nTether_Price: " + str(price) + "\nPrices_Sampled: " + str(count))
        print("========================================\n\n")

    if trades != prev_trades :
        prev_trades += 1
    count += 1
