import streamlit as st
import os
# import lightgbm as lgbm
import numpy as np
import pandas as pd
from contextlib import contextmanager
from time import time
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import classification_report, log_loss, accuracy_score
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split
# import random
import pickle
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Use the loaded model for predictions or other tasks


# data0=pd.read_csv('Airlines2.csv')
# data1=pd.get_dummies(data0.copy())
# n=len(data1)
# print(n)
# N=list(range(n))
# random.seed(2022)
# random.shuffle(N)
# target=['Delay']
# dataY = data1[target]
# dataX = data1.drop(target+['id'],axis=1)
# trainX=dataX.iloc[N[0:(n//5)*4]]
# trainY=dataY.iloc[N[0:(n//5)*4]]

# testX=dataX.iloc[N[(n//5)*4:]]
# testY=dataY.iloc[N[(n//5)*4:]]
# model = lgbm.LGBMClassifier(learning_rate=0.09,max_depth=-5,random_state=42)
# model.fit(trainX,trainY)

st.title("Flight Information")

# Create input fields with descriptive labels
airline_name = st.text_input("Enter Name of Airline (must be operating in the U.S., please input ICAO code.)")
flight_number = st.number_input("Enter Flight Number", value=1, step=1)  # Initial value and step of 1
airport_from = st.text_input("Enter Source Airport (must be U.S. airport)")
airport_to = st.text_input("Enter Destination Airport (must be U.S. airport)")
day_of_week = st.number_input("Enter Day of Week in number", min_value = 1, step = 1)
time = st.number_input("Enter Time in 0000 format",min_value=0, step=1) 
length = st.number_input("Enter Length", min_value=1, step=1) 

st.write("**Entered Information:**")
st.write("Airline Name:", airline_name)
st.write("Flight Number:", flight_number)
st.write("Airport From:", airport_from)
st.write("Airport To:", airport_to)
st.write("Day of Week:", day_of_week)
st.write("Time:", time)
st.write("Length:", length)
# Access the entered values
if st.button("Submit"):
    # Create a dictionary to hold the input data
    data0 = {
        "Airline": airline_name,
        "Flight": int(flight_number),
        "AirportFrom": airport_from,
        "AirportTo": airport_to,
        "DayOfWeek": int(day_of_week),
        "Time": int(time),
        "Length": int(length) 
    }
    df = pd.DataFrame(data0, index=[0])  # Create a single-row DataFrame
    #st.write(df)  # Display the DataFrame
    dum1 = pd.read_csv('Airlines2.csv')
    dum2=pd.get_dummies(dum1.copy())
    target=['Delay']
    dum3 = dum2.drop(target+['id'],axis=1)
    data_D1=pd.get_dummies(df)
    data_D2 =  data_D1.reindex(columns = dum3.columns, fill_value=0)
    y_preds = model.predict(data_D2)
    st.title('Is your flight going to be delayed?')
    st.write('(1 means "YES" (unfortunately)')
    st.write(y_preds)


  

