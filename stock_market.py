import streamlit as st
import pandas as pd
import yfinance as yf

st.title('Stock market TEST')

st.write("I'm  going top show you Apple stcok data")

user_input=st.text_input("Enter the stock market symbol" ,"AAPL")

ticker_data=yf.Ticker(user_input)

start = st.date_input("Start Date", value= pd.to_datetime("2023-05-31"))

end = st.date_input("Start Date", value= pd.to_ datetime("2024-01-01"))

hist=ticker_data.history(start=start, end=end)

st.write(hist)

col1, col2 = st.columns(2)

with col1:
   st.write("Volume")
   st.line_chart(hist.Volume)

with col2:
   st.write("Close")
   st.line_chart(hist.Close)



