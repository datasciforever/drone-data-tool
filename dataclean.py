import streamlit as st
import pandas as pd

st.set_page_config(page_title="Drone Data Expert", page_icon="🚀")
st.title("🚁 Smart Drone Data Cleaner")
st.write("Escape the manual work. Upload your CSV and get it cleaned instantly.")

file = st.file_uploader("Upload Drone CSV", type=['csv'])

if file:
    data = pd.read_csv(file)
    st.subheader("Raw Data View")
    st.write(data.head(10))
    
    # Cleaning the data automatically
    clean_data = data.dropna() 
    
    st.subheader("Cleaned Data (Ready for Report)")
    st.write(clean_data.head(10))
    
    # Download Button
    csv_out = clean_data.to_csv(index=False).encode('utf-8')
    st.download_button("Download Cleaned File", data=csv_out, file_name="cleaned_data.csv")
    st.success("Value created! You just saved 30 minutes of work.")
