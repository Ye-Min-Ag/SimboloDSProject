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

