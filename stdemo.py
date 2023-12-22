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
import streamlit.components.v1 as components

st.title("Myanmar's 2012 Civil Aviation Analysis")

st.title("Myanmar Airports")
st.components.v1.html("my_map.html")

st.title("Myanmar Flight Routes")
st.components.v1.html("my_map1.html")
st.markdown("**Some Source airports are marked with green color.**")  # For a smaller descriptive text
