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
airline_name = st.text_input("Name of Airline")
flight_number = st.number_input("Flight Number", value=1, step=1)  # Initial value and step of 1
airport_from = st.text_input("Airport From")
airport_to = st.text_input("Airport To")
day_of_week = st.number_input("Day of Week in number", min_value = 1, step = 1)
time = st.number_input("Time",min_value=0, step=1) 
length = st.number_input("Length", min_value=1, step=1) 

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
        "Airline Name": airline_name,
        "Flight Number": int(flight_number),
        "Airport From": airport_from,
        "Airport To": airport_to,
        "Day of Week": int(day_of_week),
        "Time": int(time),
        "Length": int(length) 
    }
    df = pd.DataFrame(data0, index=[0])  # Create a single-row DataFrame
    st.write(df)  # Display the DataFrame
    # data_D1=pd.get_dummies(df)
    # data_D2 =  data_D1.reindex(columns = dataX.columns, fill_value=0)
    # y_preds = model.predict(data_D2)
    # st.write('Predicted delay:', y_preds)


  

