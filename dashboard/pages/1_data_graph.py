import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from datetime import datetime, timedelta
import time


def main():
    pi1 = pd.read_csv('data_dir/pi1.csv')
    pi2 = pd.read_csv('data_dir/pi1.csv')
    pi3 = pd.read_csv('data_dir/pi1.csv')
    pi4 = pd.read_csv('data_dir/pi1.csv')

    pi1_graph = pi1.loc[4900:, :]
    pi2_graph = pi1.loc[4900:, :]
    pi3_graph = pi1.loc[4900:, :]
    pi4_graph = pi1.loc[4900:, :]

    ch1_day = []
    ch2_day = []
    ch3_day = []
    ch4_day = []

    pi_list = [(pi1_graph, ch1_day),
               (pi2_graph, ch2_day),
               (pi3_graph, ch3_day),
               (pi4_graph, ch4_day)]

    for i, a in pi_list:
        i['date'] = i['time'].str[:10]
        for x in i['date'].unique():
            if not x in a:
                a.append(x)

    st.set_page_config(layout="wide", page_title="Graph", page_icon="📈")
    with st.container():
        # st.title('Chamber 1')
        st.markdown(f"<h1 style='text-align: center; color: black;'>Chamber 1 </h1><span>{ch1_day[0]}</span>",
                    unsafe_allow_html=True)
    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("<h3 style='text-align: center; color: black;'>temperature</h3>",
                        unsafe_allow_html=True)
            st.line_chart(pi1_graph, x='h_m', y='temperature', height=600)
        with col2:
            st.markdown("<h3 style='text-align: center; color: black;'>humidity</h3>",
                        unsafe_allow_html=True)
            st.line_chart(pi1_graph, x='h_m', y='humidity', height=600)
        with col3:
            st.markdown("<h3 style='text-align: center; color: black;'>lux</h3>",
                        unsafe_allow_html=True)
            st.line_chart(pi1_graph, x='h_m', y='lux', height=600)
    with st.container():
        st.markdown(f"<h1 style='text-align: center; color: black;'>Chamber 2 </h1><span>{ch2_day[0]}</span>",
                    unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("<h3 style='text-align: center; color: black;'>temperature</h3>",
                        unsafe_allow_html=True)
            st.line_chart(pi2_graph, x='h_m', y='temperature', height=600)
        with col2:
            st.markdown("<h3 style='text-align: center; color: black;'>humid</h3>",
                        unsafe_allow_html=True)
            st.line_chart(pi2_graph, x='h_m', y='humidity', height=600)
        with col3:
            st.markdown("<h3 style='text-align: center; color: black;'>lux</h3>",
                        unsafe_allow_html=True)
            st.line_chart(pi2_graph, x='h_m', y='lux', height=600)
    with st.container():
        st.markdown(f"<h1 style='text-align: center; color: black;'>Chamber 3 </h1><span>{ch3_day[0]}</span>",
                    unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("<h3 style='text-align: center; color: black;'>temperature</h3>",
                        unsafe_allow_html=True)
            st.line_chart(pi3_graph, x='h_m', y='temperature', height=600)
        with col2:
            st.markdown("<h3 style='text-align: center; color: black;'>humidity</h3>",
                        unsafe_allow_html=True)
            st.line_chart(pi3_graph, x='h_m', y='humidity', height=600)
        with col3:
            st.markdown("<h3 style='text-align: center; color: black;'>lux</h3>",
                        unsafe_allow_html=True)
            st.line_chart(pi3_graph, x='h_m', y='lux', height=600)
    with st.container():
        st.markdown(f"<h1 style='text-align: center; color: black;'>Chamber 4 </h1><span>{ch4_day[0]}</span>",
                    unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("<h3 style='text-align: center; color: black;'>temperature</h3>",
                        unsafe_allow_html=True)
            st.line_chart(pi4_graph, x='h_m', y='temperature', height=600)
        with col2:
            st.markdown("<h3 style='text-align: center; color: black;'>humidity</h3>",
                        unsafe_allow_html=True)
            st.line_chart(pi4_graph, x='h_m', y='humidity', height=600)
        with col3:
            st.markdown("<h3 style='text-align: center; color: black;'>lux</h3>",
                        unsafe_allow_html=True)
            st.line_chart(pi4_graph, x='h_m', y='lux', height=600)

    with st.sidebar:

        if st.button('Graph'):
            st.write('Why hello there')


if __name__ == '__main__':
    main()
