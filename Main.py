# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 23:47:32 2023

@author: ELCOT
"""

import streamlit as st
from streamlit_option_menu import option_menu
import floral_welcome,floral_data_hub,Visualization,floral_entry_form

st.set_page_config(page_title="Iris Flower Classification", page_icon="🌺", layout="wide")
selected = option_menu(
                        menu_title="Iris Flower",
                        options=["Floral Welcome","Floral Data Dive", "Floral Insights","Floral Entry Form"],
                        icons=["house-gear-fill","database-down","pie-chart","pencil"],
                        menu_icon="flower1",
                        default_index=0,
                        orientation="horizontal"
                    )


if selected == "Floral Welcome":
    floral_welcome.iris_home()
if selected == "Floral Data Dive":
    floral_data_hub.dataset()
if selected == "Floral Insights":
    Visualization.iris_visualization()
if selected == "Floral Entry Form":
    floral_entry_form.app()
