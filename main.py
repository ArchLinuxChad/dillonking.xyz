#!/usr/bin/env python

## IMPORTS ##
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import vars
import functions

## SETUP PAGE ##
st.set_page_config(page_title=vars.page_title, layout="wide", page_icon="👾")
lottie_file = functions.get_lottie("https://lottie.host/49b218dd-1b8d-4b7c-b94e-5945a7e12655/tdeRf2NRwn.json")
webform = '''
<form action="https://api.web3forms.com/submit" method="POST">
    <!-- Replace with your Access Key -->
    <input type="hidden" name="access_key" value="342ec0e3-ba9a-48dc-a3ef-c35d5ddfad3c">
    <!-- Form Inputs. Each input must have a name="" attribute -->
    <h2>Name:</h2>
    <input type="text" name="name" required>
    <h2>Email:</h2>
    <input type="email" name="email" required>
    <h2>Message:</h2>
    <textarea name="message" required></textarea>
    <!-- Honeypot Spam Protection -->
    <input type="checkbox" name="botcheck" class="hidden" style="display: none;">
    <!-- Custom Confirmation / Success Page -->
    <!-- <input type="hidden" name="redirect" value="https://mywebsite.com/thanks.html"> -->
    <button type="submit">Submit Form</button>
</form>
'''

functions.load_css(vars.css)

## MENU ##
selected = option_menu(
    menu_title = None,
    options = ["Home", "Contact", "Projects"],
    icons = ["house", "input-cursor-text", "person-workspace"],
    orientation="horizontal"
)

if selected == "Home":
    ## PAGE TITLE ##
    with st.container():
        st.header("Hi, I'm Dillon 🤖")
        st.title("A Computer Nerd that loves Python and Linux")
        st.write("I am passionate about making fun, intiutive and good looking web apps in python. I am also a proud linux user and passionatley use Emacs.")

    st.write("---")

    ## BODY ##
    with st.container():
        col_text, col_image = st.columns(2)
        with col_text:
            st.header("My Skills")
            st.write('''
            - Python
            - Linux
            - Streamlit
            - Bash
            ''')
        with col_image:
            st_lottie(lottie_file, height=500)
elif selected == "Contact":
   st.markdown(webform, unsafe_allow_html=True)
elif selected == "Projects":
    st.title("Coming Soon...")
