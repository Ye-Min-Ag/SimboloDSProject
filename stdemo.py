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
    st.components.v1.html(html_data_1, width=900, height=600)
    # Adjust width and height as needed

st.write("Myanmar's Flights Distributions")
# Load the images
image0 = Image.open('pie_chart2.png')
image1 = Image.open('pie_chart1.png')
image2 = Image.open('pie_chart.png')

# Create three columns to display the images side by side
col1, col2, col3 = st.columns(3)

# Place each image within its respective column
with col1:
    st.image(image0)
with col2:
    st.image(image1)
with col3:
    st.image(image2)

st.write("Thailand Total Flight Routes")
path_to_html_2 = "th_map.html" 

# Read file and keep in variable
with open(path_to_html_2,'r') as f: 
    html_data_2 = f.read()

st.write("Flights In ASEAN")
## Show in webpage
with st.container():
    st.components.v1.html(html_data_2, width=900, height=600)
    # Adjust width and height as needed
image3 = Image.open('plot2.png')
image4 = Image.open('plot1.png')
col1, col2 = st.columns(2)
 # Adjust dimensions
with col1:
    st.image(image3)
with col2:
    st.image(image4)

image5 = Image.open('bar_chart1.png')
image6 = Image.open('bar_chart2.png')
image7 = Image.open('final_chart.png')
st.image(image5)
st.image(image6)
st.image(image7)
