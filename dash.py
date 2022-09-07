import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px


st.title('Airbnb')
st.header("App")
st.write("Sitio que te permite analizar de form visual y concentrada los datos de airbnb")

@st.cache
def load_data(nrows):
    airbnb = pd.read_csv("airbnb_clean.csv", nrows=nrows)
    lowercase = lambda x: str(x).lower()
    return airbnb

st.sidebar.image("airbnb.jpeg")
st.sidebar.markdown("##")

loading_data = st.text('Loading airbnb data...')
airbnb = load_data(101)
loading_data.text("Done!")

data_description = st.sidebar.checkbox("Data description")
if data_description:
    st.header("Show Dataframe Overview")
    st.dataframe(airbnb)

@st.cache
def df_hometown(neighbourhood):
    neighbourhood_filter=airbnb[airbnb["neighbourhood"].str.upper().str.contains(neighbourhood.upper())]
    
    return neighbourhood_filter

neighbourhood_sb= st.sidebar.text_input("Vecindario")
search_neighbourhood=st.sidebar.button("Search by hometown")

if(search_neighbourhood):
    neighbourhood_filter_if= df_hometown(neighbourhood_sb)
    count_row= neighbourhood_filter_if.shape[0]
    st.write(f"Total: {count_row} outcome")

    st.dataframe(neighbourhood_filter_if)

#filtrar entre un rango de precios (minimo y maximo)
price_filter = st.slider('price', 0, 999998, 5000)
filtered_range = airbnb[airbnb['price'].dt.hour == price_filter]

st.subheader('Mapa de las residencias at %s' % price_filter)
st.map(filtered_range)

@st.cache
def room_clase(room_class):
    filter_room=airbnb[airbnb["room_type"]==room_class]
    
    return filter_room

select_type= st.sidebar.selectbox("Selecciona el tipo de residencia", airbnb['room_type'].unique())
search_class=st.sidebar.button("Search by education level")

if(search_class):
    filter_type_if= room_clase(select_type)
    count_row= filter_type_if.shape[0]
    st.write(f"Total: {count_row} outcome")

    st.dataframe(filter_type_if)


#GRÁFICOS
hisplot_by_price= st.sidebar.checkbox("Histograma: Distribución de precios")
if hisplot_by_price:
    fig, ax = plt.subplots()
    ax.hist(airbnb.price)
    st.header("Distribución de precios de todas las residencias")
    st.pyplot(fig)
    st.markdown("_")

typeroom_price= st.sidebar.checkbox("Relacion entre precio y tipo de residencia")
if typeroom_price:
    fig, ax = plt.subplots()
    y= airbnb["price"]
    x=airbnb["room_type"]
    ax.barh(x,y)
    ax.set_ylabel("Precio")
    ax.set_xlabel("Tipo de Residencia")
    st.header("Relacion entre tipo de residencia y precio promedio")
    st.pyplot(fig)
    st.markdown("_")

neighbourhood_price= st.sidebar.checkbox("Relacion entre precio y vecindario")
if typeroom_price:
    fig, ax = plt.subplots()
    y= airbnb["price"]
    x=airbnb["neighbourhood"]
    ax.barh(x,y)
    ax.set_ylabel("Precio")
    ax.set_xlabel("Vecindario")
    st.header("Relacion entre tipo de precio y vecindario")
    st.pyplot(fig)
    st.markdown("_")




