import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import time


def main():
    pi1 = pd.read_csv('data_dir/pi1.csv')
    pi2 = pd.read_csv('data_dir/pi2.csv')
    pi3 = pd.read_csv('data_dir/pi3.csv')
    pi4 = pd.read_csv('data_dir/pi4.csv')



    # with st.container():
    col1, col2 , col3= st.columns(3)
    with col1:
        st.line_chart(pi1, x='created_at', y='temperature', height=100)
    with col2:
        st.line_chart(pi1, x='created_at', y='humidity', height=100)
    with col3:
        st.line_chart(pi1,  x='created_at', y='lux', height=100)
    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            st.line_chart(pi2, x='created_at', y='temperature', height=100)
        with col2:
            st.line_chart(pi2, x='created_at', y='humidity', height=100)
        with col3:
            st.line_chart(pi2,  x='created_at', y='lux', height=100)
    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            st.line_chart(pi3, x='created_at', y='temperature', height=100)
        with col2:
            st.line_chart(pi3, x='created_at', y='humidity', height=100)
        with col3:
            st.line_chart(pi3,  x='created_at', y='lux', height=100)
    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            st.line_chart(pi4, x='created_at', y='temperature', height=100)
        with col2:
            st.line_chart(pi4, x='created_at', y='humidity', height=100)
        with col3:
            st.line_chart(pi4,  x='created_at', y='lux', height=100)

    with st.sidebar:

        with st.echo():
            st.write("This code will be printed to the sidebar.")
            st.write("humid")

        with st.spinner("Loading..."):
            time.sleep(5)
        st.success("Done!")




if __name__ == '__main__':
    main()
