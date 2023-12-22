import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
rfmodel= st.sidebar.checkbox('Decision Trees')
data = pd.read_csv(r'airlines2.csv')


