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
    
    st.markdown("# Bloom with Iris Magic!")
    st.markdown("Welcome to the Blooming Iris Web App! Predict the enchanting species of Iris flowers and uncover the secrets hidden in their petals.")
    st.markdown("### Embrace the Floral Adventure:")
    st.markdown("🌿 **Discover Iris Species:** Immerse yourself in the world of Iris flowers and predict their species with a touch of magic.")
    st.markdown("🌈 **Petals of Possibilities:** Explore the characteristics of sepal and petal dimensions, and witness the power of predictive analytics.")
    st.markdown("🌟 **Magical Predictions:** Use our easy-to-use sliders to input flower details and watch as the app unveils the mystical prediction of the Iris species.")
    st.markdown("### What Awaits You:")
    st.markdown("🔍 **Dataset Dive:** Delve into the Iris dataset, a treasure trove of floral insights. Uncover the unique traits that define each Iris species.")
    st.markdown("📜 **Model Magic:** Learn about the spellbinding machine learning model that brings this floral adventure to life. Understand the wizardry behind the predictions.")
    st.markdown("🌌 **Floral Symphony:** Each species has its own tune. Listen closely as the app reveals the Iris species, accompanied by beautiful visuals.")
    st.markdown("### Ready to Bloom?")
    
    st.markdown("""🌸 **Navigate the Blooms:** Click through the petals of our web app.
                    Explore the Input Form to make predictions, visit the About page to understand the magic, and gaze upon the dataset for floral revelations.""")
    st.markdown("🎉 **Embark on the Floral Journey:** Ready to embark on a journey through the iris garden? Click, predict, and let the magic unfold!")
    st.markdown("### Bloom with Us! 🌼")
    
    
    
    