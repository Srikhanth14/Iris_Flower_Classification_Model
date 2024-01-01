# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 15:26:59 2024

@author: ELCOT
"""

import streamlit as st
from PIL import Image

def iris_visualization():
    # Page Title
    st.title("Visualizations")

    # Introduction
    st.write("Explore visualizations highlighting patterns and insights from Iris flower data.")

    # Image 1: Distribution of Species
    st.header("1. Distribution of Species")
    image1 = Image.open("Distribution.png")  # Replace with your image file
    st.image(image1, caption="Species Distribution", use_column_width=True)

    # Image 2: Pairplot
    st.header("2. Pairplot")
    image2 = Image.open("pairplot.png")  # Replace with your image file
    st.image(image2, caption="Pairplot", use_column_width=True)

    # Image 3: Boxen plot (subplots 2x2 each sepal length, sepal width, petal length, petal width by species)
    st.header("3. Boxen Plot (Subplots 2x2)")
    image3 = Image.open("boxen.png")  # Replace with your image file
    st.image(image3, caption="Boxen Plots", use_column_width=True)

    # Image 4: Violin plot (subplots 2x2 each sepal length, sepal width, petal length, petal width by species)
    st.header("4. Violin Plot (Subplots 2x2)")
    image4 = Image.open("violin.png")  # Replace with your image file
    st.image(image4, caption="Violin Plots", use_column_width=True)

    # Image 5: Correlation Heatmap
    st.header("5. Correlation Heatmap")
    image5 = Image.open("correlation.png")  # Replace with your image file
    st.image(image5, caption="Correlation Heatmap", use_column_width=True)

    # Call to Action
    st.write("Ready to explore more insights? Head to the **Dataset** and **Input Form** pages for a deeper dive into Iris flower data.")
