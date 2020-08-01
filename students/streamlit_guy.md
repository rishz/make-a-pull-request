## this is about using streamlit for data science
import streamlit as st
st.title("Streamlit application")


st.markdown("Crashes data from nyc")
import pandas as pd
import numpy as np
datal = ("/home/rhyme/Desktop/Project/a.csv")

@st.cache(persist=True)
def take_data(nrows):
    data  =  pd.read_csv(datal,nrows=nrows,parse_dates=[["CRASH_DATE","CRASH_TIME"]])
    data.dropna(subset= ['LATITUDE','LONGITUDE'],inplace =True)
    lowercase = lambda x:str(x).lower()
    data.rename(lowercase,axis="columns",inplace= True)
    data.rename(columns = {'crash_date_crash_time':'data/time'},inplace=True)
    return data
data  = take_data(100000)
st.header("Place of accident")
patients = st.slider("numfber of patients",0,19)
st.map(data.query("injured_persons>= @patients")[['latitude','longitude']].dropna(how = "any"))

st.header("at what time")
hour = st.selectbox("hours",range(0,24),1)
st.markdown("between %i:00 %i:00 "%(hour,hour+1))
data = data[data['data/time'].dt.hour==hour]
import pydeck as pdk
midpoint = (np.average(data['latitude']),np.average(data['longitude']))
st.write(pdk.Deck(
    map_style= 'mapbox://styles/mapbox/light-v9',
    initial_view_state={
        'latitude': midpoint[0],
        'longitude':midpoint[1],
        'zoom': 13,
        'pitch ': 80,

    },
    layers = [pdk.Layer(
        "HexagonLayer",
        data = data[['data/time','latitude','longitude']],
        get_position = ['longitude','latitude'],
        radius =100,
        extruded = True,
        pickable = True,
        elevation_scale=4,
        elevation_range=[0,1000],
   ),
    ],
))
import plotly.express as px
st.header("accident time")
filtered = data[(data['data/time'].dt.hour>=hour)&(data['data/time'].dt.hour<hour+1)]
hist = np.histogram(filtered['data/time'].dt.minute,bins =60,range=(0,60))[0]
chart_data = pd.DataFrame({'minute':range(60),"crashes":hist})
fig= px.bar(chart_data,x='minute',y='crashes',hover_data=['minute','crashes'])

st.write(fig)
if st.checkbox("how",False):
    st.subheader("show")
    st.write(data)

