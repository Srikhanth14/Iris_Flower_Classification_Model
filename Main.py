# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 23:47:32 2023

@author: ELCOT
"""

import streamlit as st
from streamlit_option_menu import option_menu
import floral_welcome, floral_story, floral_data_hub, floral_entry_form

st.set_page_config(page_title="Iris Flower Classification", page_icon="🌺", layout="wide")
selected=option_menu(menu_title="Iris Flower",
                    options=["Floral Welcome", "Floral Story", "Floral Data Dive", "Floral Entry Form"],
                    icons=["house-fill","book","bar-chart-fill", "card-list"],
                    menu_icon="menu-up",
                    default_index=0,
                    orientation="horizontal"
                    )


    

if selected=="Floral Welcome":
  floral_welcome.iris_home()
if selected=="Floral Story":
  floral_story.iris_about()
if selected=="Floral Data Dive":
  floral_data_hub.dataset()
if selected=="Floral Entry Form":
  floral_entry_form.app()
