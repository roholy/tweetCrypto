import shrimpy
import plotly.graph_objects as go
from config import publicKey, secretKey

#https://morioh.com/p/665bb1d42d40 here is the artivle this program structure is based on
#to use vs code github just commit then type git push in command line.
#https://plotly.com/python/candlestick-charts/ learn how to plot candlesticks
# shrimpy api use https://blog.shrimpy.io/blog/historical-crypto-exchange-trade-data
#https://medium.com/analytics-vidhya/recognizing-over-50-candlestick-patterns-with-python-4f02a1822cb5
#how to read candlstick data


# insert your public and secret keys here Shrimpy


# insert your public and secret keys here

# def waxy(ticker_symbol):
#     # create the client
#     client = shrimpy.ShrimpyApiClient(publicKey, secretKey)

#     #veiw available credits
#     credits = client.get_credits()
#     nugget = credits
#     print(nugget)

#     instruments = client.get_historical_instruments()

#     # get the candles
#     candles = client.get_candles(   
#             # an exchange is a trading platform
#             #USDC will track the us dollar

#         'kucoin',  # exchange
#         ticker_symbol,      # base_trading_symbol
#         'usdc',      # quote_trading_symbol
#         '1m'       # interval
        
#     )


# #stuck at the part where i need to create a variable that uses the complex data recieved from candles, and makes it into a readable format
# #I can do this using plotly but i do not want to use it 

# print(candles)
# waxy("doge")


# Graph the candlestick chart

def graph(ticker_symbol):
    # create the client
    client = shrimpy.ShrimpyApiClient(publicKey, secretKey)

    #veiw available credits
    credits = client.get_credits()
    nugget = credits
    print(nugget)

    instruments = client.get_historical_instruments()

    # get the candles
    candles = client.get_candles(   
            # an exchange is a trading platform
            #USDC will track the us dollar

        'kucoin',  # exchange
        ticker_symbol,      # base_trading_symbol
        'usdc',      # quote_trading_symbol
        '1m',       # interval
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

    # add labels

    fig.update_layout(
        title=ticker_symbol,
        yaxis_title='Price',
        # shapes = [dict(
        #     x0='2016-12-09', x1='2016-12-09', y0=0, y1=1, xref='x', yref='paper',
        #     line_width=2)],
        # annotations=[dict(
        #     x='2016-12-09', y=0.05, xref='x', yref='paper',
        #     showarrow=False, xanchor='left', text='Increase Period Begins')]
    )
    # display our graph
    fig.show()


graph("doge")
