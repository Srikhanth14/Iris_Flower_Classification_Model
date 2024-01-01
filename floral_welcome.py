# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 23:50:09 2023

@author: ELCOT
"""
import streamlit as st
from PIL import Image

def iris_home():
    
    image=Image.open('iris_flower.jpeg')
    st.image(image,use_column_width=True)
    
   
    # Introduction
    st.header("Welcome to the Blooming Iris Web App!")
    st.write('''Immerse yourself in the enchanting world of Iris flowers. Predict the species and uncover the magic hidden in their petals.''')

    # Key Features
    st.subheader("Key Features:")
    st.write('''1. **Species Prediction:**
    Explore the predictions of Iris flower species with the touch of magic. The model considers sepal and petal dimensions to reveal the floral secrets.''')

    st.write('''2. **User-Friendly Interface:**
    Navigate effortlessly through the app. Use our easy-to-use sliders to input flower details and witness the mystical predictions of Iris species.''')

    st.write('''3. **Floral Insights:**
    Delve into the characteristics of sepal and petal dimensions. Visualize the patterns and understand the unique traits defining each Iris species.''')

    # About the Project
    st.subheader("About the Project:")
    st.write('''The Blooming Iris project combines the beauty of flowers with modern data science techniques. Join us in exploring the features that define each Iris species.''')

    # About Me
    st.subheader("About Me:")
    st.write('''Curious about the mind behind the predictions? I'm [Your Name], a dedicated data scientist passionate about unraveling insights from nature.''')
    st.write('''Feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/srikhanth-r) or explore more projects on my [portfolio](datascienceportfol.io/srikhanth_r). Let's dive deep into the world of data science together!''')

    # Call to Action
    st.write('''Ready to explore the blooming Iris garden? Click through the petals of our web app. Explore the Input Form to make predictions and understand the magic behind each species.''')

