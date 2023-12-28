# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 00:00:30 2023

@author: ELCOT
"""
import streamlit as st
import pandas as pd
import numpy as np
import pickle
from PIL import Image

def app():
    # Load the trained model
    loaded_model = pickle.load(open('Iris_Trained_Model.sav', 'rb'))
    
    # Function for making predictions
    def iris_flower_prediction(input_data):
        
        # Convert input data to a numpy array
        input_data_np_array = np.asarray(input_data)
        
        # Reshape the numpy array as we are predicting for only one instance
        input_data_reshaped = input_data_np_array.reshape(1, -1)
        column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
        
        # Make predictions using the trained model
        input_data_reshaped_df = pd.DataFrame(input_data_reshaped,columns=column_names)
        prediction = loaded_model.predict(input_data_reshaped_df)
        
        # Display prediction result
        if prediction[0] == 0:
            st.write("The flower belongs to the 'Iris-setosa' species.")
            st.image(Image.open('iris_stetosa.jpeg'), use_column_width=True)
        elif prediction[0] == 1:
            st.write("The flower belongs to the 'Iris-versicolor' species.")
            st.image(Image.open('Iris_versicolor_1.jpeg'), use_column_width=True)
        else:
            st.write("The flower belongs to the 'Iris-virginica' species.")
            st.image(Image.open('iris_virginica.jpeg'), use_column_width=True)
        
    def main():
        st.title('Iris Flower Classification Web App')
        
        # Sliders for user input
        sepal_length = st.slider("Sepal Length", min_value=4.0, max_value=8.0, step=0.1)
        sepal_width = st.slider("Sepal Width", min_value=2.0, max_value=4.5, step=0.1)
        petal_length = st.slider("Petal Length", min_value=1.0, max_value=7.0, step=0.1)
        petal_width = st.slider("Petal Width", min_value=0.1, max_value=2.5, step=0.1)
       
        # Button to trigger prediction
        if st.button('Iris Flower Classification Result'):
            iris_flower_prediction([sepal_length, sepal_width, petal_length, petal_width])
        
    # Run the main function
    main()
    
