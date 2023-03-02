import streamlit as st
import time
import numpy as np
import pandas as pd


def main():
    pi1 = pd.read_csv('dashboard/data_dir/pi1.csv')
    pi1_g = pi1[['h_m', 'temperature']]



    st.set_page_config(page_title="Plotting Demo", page_icon="📈")

    st.markdown("# Plotting Demo")
    st.sidebar.header("Plotting Demo")
    st.write(
        """This demo illustrates a combination of plotting and animation with
    Streamlit. We're generating a bunch of random numbers in a loop for around
    5 seconds. Enjoy!"""
    )


    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.empty()
    last_rows = pd.DataFrame({'h_m':[20190103, 20190222, 20190531],
                             'temperature':['Kim', 'Lee', 'Jeong']})
    chart = st.line_chart(last_rows, x='h_m', y='temperature')

    for i in range(1, len(pi1)):
        new_rows = last_rows + pi1_g.loc[i]
        status_text.text("%i%% Complete" % i)
        chart.add_rows(new_rows)
        progress_bar.progress(i)
        last_rows = new_rows
        time.sleep(0.05)

    progress_bar.empty()

    # Streamlit widgets automatically run the script from top to bottom. Since
    # this button is not connected to any other logic, it just causes a plain
    # rerun.
    st.button("Re-run")


if __name__ == '__main__':
    main()