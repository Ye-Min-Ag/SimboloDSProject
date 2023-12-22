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

st.write("Myanmar Airports")

path_to_html = "my_map.html" 

# Read file and keep in variable
with open(path_to_html,'r') as f: 
    html_data = f.read()

## Show in webpage
with st.container():
    st.components.v1.html(html_data, width=600, height=500)
    # Adjust width and height as needed

st.write("Myanmar Total Flight Routes")
path_to_html_1 = "my_map1.html" 

# Read file and keep in variable
with open(path_to_html_1,'r') as f: 
    html_data_1 = f.read()

## Show in webpage
with st.container():
    st.components.v1.html(html_data_1, width=1200, height=600)
    # Adjust width and height as needed
st.markdown("**Some Source airports are marked with green color.**")# For a smaller descriptive text
image0 = Image.open('pie_chart2.png')    
st.image(image0) 
image1 = Image.open('pie_chart1.png')    
st.image(image1) 
image2 = Image.open('pie_chart.png')    
st.image(image2) 
