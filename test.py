import streamlit as st
import time
import numpy as np
import pandas as pd


pi1 = pd.read_csv('dashboard/data_dir/pi1.csv')
pi1_g = pi1[['h_m', 'temperature']]


df1 = pd.DataFrame(
   np.random.randn(50, 20),
   columns=('col %d' % i for i in range(20)))

print(df1)

last_rows = np.array(pi1_g['temperature'][0])


for i in range(1, len(pi1)):
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    last_rows = new_rows
    time.sleep(0.05)


