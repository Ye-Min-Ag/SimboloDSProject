import os
import numpy as np
import pandas as pd
import pickle
from contextlib import contextmanager
from time import time
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import classification_report, log_loss, accuracy_score
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Use the loaded model for predictions or other tasks
rfmodel= st.sidebar.checkbox('Prediction')

# if rfmodel:
    
#     with st.form("my_form1"):
        
#         st.title('Classify the airlines')        
#         st.subheader("Please choose the airline")

#         st.write("You selected:", "Age:" + agegp + "Student:" + student)    
#         submitted = st.form_submit_button("Submit")
#         if submitted:
#             #st.write("slider", slider_val, "checkbox", checkbox_val)
#             inputdata = {'age': agegp,
#                         'studen': student, 
#                         'income': income,
#                         'credit rating': credit_rating}
#             features = pd.DataFrame(inputdata, index=[0])
#             features_dummy = pd.get_dummies(features)
#             #st.write(features)
