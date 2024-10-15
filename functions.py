#!/usr/bin/env python
import streamlit as st
import requests

def load_css(file):
    with open(file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def get_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
