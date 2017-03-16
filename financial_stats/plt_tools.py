# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 14:28:27 2017

@author: 11314
"""

#Convert a dataframe to a plot quotes

def df_to_quotes(df):
    import matplotlib.dates as mdates
    qts = []
    for irows in df.iterrows():
        dt = mdates.date2num(irows[0].to_pydatetime())
        high = irows[1]['HIGH']
        low = irows[1]['LOW']
        cls = irows[1]['CLOSE']
        ope = irows[1]['OPEN']
        vlm = irows[1]['VOLUME']
        trow = (dt,ope,high,low,cls,vlm)
        qts.append(trow)
    return qts
    
#Plot the candlestick using the quotes

def plt_candle(quotes):
    import matplotlib.pyplot as plt
    import matplotlib.finance as mpf
    fig, ax = plt.subplots(1,1)
    fig.subplots_adjust(bottom=0.2)
    ax.xaxis_date()
    plt.xticks(rotation=45)
    mpf.candlestick_ohlc(ax,quotes,width=0.8,colorup='#FF6666',colordown='#99CC66')
    
