import streamlit as st
import pandas as pd
st.title("streamlit app")
name = st.text_input("enter your name")
if name:
    st.write(f"HELLO {name}")

age = st.slider("enter your age:",0,100,33)
st.write(f"your age is:{age}")
options = ["python","java",'c++',"dotnet"]
choice = st.selectbox("choose your favourite language",options)
st.write(f"your language is{choice}")

data = {
    "name":["divya",'sathish','harshitha','jahnavi'],
    'age':[33,38,8,5],
    'city':['New york','japan','london','america']
}
df = pd.DataFrame(data)
df.to_csv("sample_data.csv")
st.write(df)

uploaded_file = st.file_uploader("choose a csv file",type='csv')
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)