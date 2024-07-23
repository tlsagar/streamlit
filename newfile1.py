import streamlit as st
import pandas as pd
import yfinance as yf

st.title("Stock Market App")

st.write("This is my hope of getting New dream Job!!")


ticker_symbol = st.text_input("Enter the stock ticker symbol", "AAPL")

ticker_data = yf.Ticker(ticker_symbol)

starting_date = st.date_input("Enter the starting date", value=pd.to_datetime("2021-01-01"))
ending_date = st.date_input("Enter the ending date", value=pd.to_datetime("today"))


hist = ticker_data.history(start=starting_date, end=ending_date)


st.write("I am going to show you the data of Apple stock")

# st.write(hist)

st.dataframe(hist)

st.line_chart(hist.Volume) # x-axis as the index of the dataframe, y-axis is what you provide


col1, col2 = st.columns(2)

with col1:
    st.write("This plot is for Volume of the stock")
    st.line_chart(hist.Volume) # x-axis as the index of the dataframe, y-axis is what you provide

with col2:
    st.write("This plot is for Price of the stock")
    st.line_chart(hist.Close)


import pickle

with open("lr.pkl", "wb") as f:
    pickle.dump(lr, f)


read lr.pkl back into memory

with open("lr.pkl", "rb") as f:
    lr = pickle.load(f)