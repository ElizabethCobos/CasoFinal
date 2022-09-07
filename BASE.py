import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px

st.title('Employees App')
st.header("using streamlit")
st.write("Dashboard (employees).")

@st.cache
def load_data(nrows):
    employee = pd.read_csv("Employees.csv", nrows=nrows)
    lowercase = lambda x: str(x).lower()
    return employee

employee_load_state = st.text('Loading employees data...')
employee = load_data(501)
employee_load_state.text("Done!")

employee_description = st.sidebar.checkbox("Data description")
if employee_description:
    st.header("Show Dataframe Overview")
    st.dataframe(employee)

hisplot_by_age= st.sidebar.checkbox("Histplot by Age")
if hisplot_by_age:
    fig, ax = plt.subplots()
    ax.hist(employee.Age)
    st.header("Histplot of employee Age")
    st.pyplot(fig)
    st.markdown("_")

employee_histplot= st.sidebar.checkbox("employees per unit")
if employee_histplot:
    fig, ax = plt.subplots()
    ax.hist(employee.Unit)
    st.header("Histplot of employees")
    st.pyplot(fig)
    st.markdown("_")

city_attrittion= st.sidebar.checkbox("City chart and Attrition rate")
if city_attrittion:
    fig, ax = plt.subplots()
    y= employee["Attrition_rate"]
    x=employee["Hometown"]
    ax.barh(x,y)
    ax.set_ylabel("City")
    ax.set_xlabel("Attrition_rate")
    st.header("Attrition_rate by city")
    st.pyplot(fig)
    st.markdown("_")

age_attrition= st.sidebar.checkbox("graphic: age and attrition rate")
if age_attrition:
    fig, ax = plt.subplots()
    y= employee["Attrition_rate"]
    x=employee["Age"]
    ax.barh(x,y)
    ax.set_ylabel("Age")
    ax.set_xlabel("Attrition rate")
    st.header("Attrition rate by age")
    st.pyplot(fig)
    st.markdown("_")

attrition_service= st.sidebar.checkbox("Graphic: attrition rate and time of service")
if attrition_service:
    fig, ax = plt.subplots()
    y= employee["Attrition_rate"]
    x=employee["Time_of_service"]
    ax.barh(x,y)
    ax.set_ylabel("Time of service")
    ax.set_xlabel("Attrition rate")
    st.header("Attrition rate and time of service")
    st.pyplot(fig)
    st.markdown("_")

@st.cache
def df_id(id):
    employee_byid=employee[employee["Employee_ID"].str.upper().str.contains(id.upper())]
    
    return employee_byid

employee_id= st.sidebar.text_input("ID de empleado")
search_by_id=st.sidebar.button("Search by ID")

if(search_by_id):
    id_filter= df_id(employee_id)
    count_row= id_filter.shape[0]
    st.write(f"Total: {count_row} resultados")

    st.dataframe(id_filter)

@st.cache
def df_hometown(hometown):
    hometown_filter=employee[employee["Hometown"].str.upper().str.contains(hometown.upper())]
    
    return hometown_filter

employees_hometown= st.sidebar.text_input("Employee's Hometown")
search_by_hometown=st.sidebar.button("Search by hometown")

if(search_by_hometown):
    hometown_filter_if= df_hometown(employees_hometown)
    count_row= hometown_filter_if.shape[0]
    st.write(f"Total: {count_row} outcome")

    st.dataframe(hometown_filter_if)

@st.cache
def df_unit(unit):
    unit_filter=employee[employee["Unit"].str.upper().str.contains(unit.upper())]
    
    return unit_filter

unit_employee= st.sidebar.text_input(" unit by employee")
search_unit=st.sidebar.button("search by unit")

if(search_unit):
    unit_filter_if= df_unit(unit_employee)
    count_row= unit_filter_if.shape[0]
    st.write(f"Total: {count_row} outcome")

    st.dataframe(unit_filter_if)

@st.cache
def df_education(education):
    filter_education=employee[employee["Education_Level"]==education]
    
    return filter_education

select_education= st.sidebar.selectbox("Select education level", employee['Education_Level'].unique())
search_education=st.sidebar.button("Search by education level")

if(search_education):
    filter_education_if= df_education(select_education)
    count_row= filter_education_if.shape[0]
    st.write(f"Total: {count_row} outcome")

    st.dataframe(filter_education_if)

@st.cache
def hometown_city(city):
    filter_city=employee[employee["Hometown"]==city]
    
    return filter_city

select_city= st.sidebar.selectbox("Select city", employee['Hometown'].unique())
search_city=st.sidebar.button("search by city")

if(search_city):
    filter_city_if= hometown_city(select_city)
    count_row= filter_city_if.shape[0]
    st.write(f"Total: {count_row} outcome")

    st.dataframe(filter_city_if)

@st.cache
def df_one(one):
    filter_one=employee[employee["Unit"]==one]
    
    return filter_one

select_one= st.sidebar.selectbox("Select a unit in box", employee['Unit'].unique())
search_one=st.sidebar.button("Search by unit in box")

if(search_one):
    filter_one_if= df_one(select_one)
    count_row= filter_one_if.shape[0]
    st.write(f"Total: {count_row} outcome")

    st.dataframe(filter_one_if)