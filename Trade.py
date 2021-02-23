import shrimpy
import plotly.graph_objects as go
from config import publicKey, secretKey

# insert your public and secret keys here Shrimpy

public_key = publicKey
secret_key = secretKey

# insert your public and secret keys here


# create the client
client = shrimpy.ShrimpyApiClient(public_key, secret_key)

# get the candles
candles = client.get_candles(
    'binance',  # exchange
    'XLM',      # base_trading_symbol
    'BTC',      # quote_trading_symbol
    '15m'       # interval
)

# create lists to hold our different data elements
dates = []
open_data = []
high_data = []
low_data = []
close_data = []

# convert from the Shrimpy candlesticks to the plotly graph objects format
for candle in candles:
    dates.append(candle['time'])
    open_data.append(candle['open'])
    high_data.append(candle['high'])
    low_data.append(candle['low'])
    close_data.append(candle['close'])

# construct the figure
fig = go.Figure(data=[go.Candlestick(x=dates,
                       open=open_data, high=high_data,
                       low=low_data, close=close_data)])

# display our graph
fig.show()