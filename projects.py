#!/usr/bin/env python3
import streamlit as st

def main():
    with st.container():
        st.header("Grade Reviewer")
        st.write("Visualises GSCE grades into charts to make it easier to understand.")
        st.link_button("Check it out here", "https://gradesanalyser.streamlit.app")

    st.write("---")
