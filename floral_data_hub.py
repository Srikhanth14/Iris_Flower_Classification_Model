# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 23:57:01 2023
@author: ELCOT
"""
import streamlit as st
import pandas as pd
def dataset():
    st.markdown("# Iris Dataset Exploration")
    st.markdown("Here dataset holds the secrets of Iris flowers, and we invite you to unravel the mysteries within.")
    st.markdown("### Dataset Overview:")
    st.markdown("🌸 **Source:** The Iris dataset is a gem sourced from nature, providing detailed information about the characteristics of Iris flowers.")
    st.markdown("🎨 **Data Cleaning:** The dataset has been meticulously cleaned, ensuring accuracy and reliability in every petal's detail.")
    st.markdown("📊 **Exploratory Data Analysis (EDA):** Embark on a visual journey through the dataset. Summaries and visualizations have been crafted to unveil the patterns within.")
    st.markdown("### Sample Floral Insights:")
    st.markdown("Here is a glimpse of the dataset, showcasing a few rows:")
    
    data=pd.read_csv("IRIS.csv")
    st.dataframe(data)
    
    st.markdown("### Download Floral Knowledge:")
    st.markdown("You can download the full Iris dataset for further exploration and to witness the diversity of Iris flowers:")
    def data_read(data):
        return data.to_csv().encode('utf-8')
    
    csv=data_read(data)
    
    st.download_button(
            label='Download Sample Data',
            data=csv,
            file_name='iris.csv',
            mime='text/csv'
    )
    st.markdown("### Dig Deeper:")
    st.markdown("Explore our GitHub repository for detailed information, project code, and additional insights into the world of Iris flowers.")
    st.markdown("[GitHub Repository](https://github.com//Srikhanth14//CODSOFT//blob//main//Project_3_Iris_Flower_Classification.ipynb)")
    st.markdown("Feel free to immerse yourself in the dataset, uncover patterns, and delve into the analysis conducted during the project.")
    st.markdown("### Blossom with Knowledge! 🌼")
