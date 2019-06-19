import bitfinex
import datetime
import time
# Create api instance of the v2 API
api_v2 = bitfinex.bitfinex_v2.api_v2()

result = api_v2.candles()


# Define query parameters
pair = 'BTCUSD' # Currency pair of interest
bin_size = '5m' # This will return minute data
limit = 1000    # We want the maximum of 1000 data points
# Define the start date
t_start = datetime.datetime(2018, 4, 1, 0, 0)
t_start = time.mktime(t_start.timetuple()) * 1000
# Define the end date
t_stop = datetime.datetime(2018, 4, 2, 0, 0)
t_stop = time.mktime(t_stop.timetuple()) * 1000
result = api_v2.candles(symbol=pair, interval=bin_size,
                     limit=limit, start=t_start, end=t_stop)

print(result)
