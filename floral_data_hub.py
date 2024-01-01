# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 23:57:01 2023
@author: ELCOT
"""
import streamlit as st
import pandas as pd
def dataset():
    # Dataset Information
    st.header("Dataset Information:")
    st.write('''The predictive model is trained on a dataset containing information about Iris flowers, including features such as sepal length, sepal width, petal length, petal width, and species.''')

    # Data Source
    st.header("Data Source:")
    st.write('''For more details, you can explore the dataset on Kaggle: [Click Here](https://www.kaggle.com/datasets/arshid/iris-flower-dataset)''')

    # Sample Data
    st.header("Sample Data:")
    st.write("Here's a glimpse of the Iris dataset:")
    data = pd.read_csv("IRIS.csv")  # Update with the actual file name
    st.dataframe(data.head())
     
    # Display your sample data here
    st.subheader("Download Dataset")
    st.write("You can download the full Iris dataset for further exploration:")

    def data_read(data):
        return  data.to_csv().encode('utf-8')

    csv = data_read(data)

    st.download_button(
        label='Download Sample Data',
        data=csv,
        file_name='iris.csv',
        mime='text/csv'
    )

    # Input Your Data
    st.header("Input Your Data:")
    st.write("Want predictions for your specific Iris flower details? Enter your data in the input form and discover the predicted Iris species.")

    # Guidance on Data Format
    st.header("Guidance on Data Format:")
    st.write("To ensure successful predictions, enter your data with the same features as the sample data. Include columns for sepal length, sepal width, petal length, and petal width.")

    # GitHub Link
    st.header("GitHub Repository:")
    st.write("Explore the code and details of this project on my GitHub repository:")
    st.write("[Iris Flower Classification GitHub Repository](https://github.com/Srikhanth14/CODSOFT/blob/main/Project_3_Iris_Flower_Classification.ipynb)")

    # Conclusion
    st.write("Ready to predict the Iris species for your data? Input your flower details in the input form, and let the Iris Flower Classification app work its magic!")

