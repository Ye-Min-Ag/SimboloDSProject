import os
import numpy as np
import pandas as pd
import random
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import seaborn as sns
from contextlib import contextmanager
from time import time
from tqdm import tqdm
import lightgbm as lgbm
import category_encoders as ce
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import classification_report, log_loss, accuracy_score
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import KFold

data0 = pd.read_csv('airlines2.csv')
data1=pd.get_dummies(data0.copy())
n=len(data1)
print(n)
N=list(range(n))
random.seed(2022)
random.shuffle(N)
target=['Delay']
dataY = data1[target]
dataX = data1.drop(target+['id'],axis=1)

trainX=dataX.iloc[N[0:(n//5)*4]]
trainY=dataY.iloc[N[0:(n//5)*4]]

testX=dataX.iloc[N[(n//5)*4:]]
testY=dataY.iloc[N[(n//5)*4:]]
model = lgbm.LGBMClassifier(learning_rate=0.09,max_depth=-5,random_state=42)
model.fit(trainX,trainY)

