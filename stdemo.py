import streamlit as st
import pandas as pd
import sklearn
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go
import geopandas as gpd
from geopy.geocoders import Nominatim
import matplotlib.pyplot as plt
import numpy as np
import folium
from folium import plugins
from streamlit.components.v1 import html

st.title("Myanmar's 2012 Civil Aviation Analysis")

st.title("Myanmar Airports")
html("https://github.com/Ye-Min-Ag/SimboloDSProject/raw/main/my_map.html")

st.title("Myanmar Flight Routes")
html("https://github.com/Ye-Min-Ag/SimboloDSProject/raw/main/my_map1.html")  # For a large title
st.markdown("**Some Source airports are marked with green color.**")  # For a smaller descriptive text
