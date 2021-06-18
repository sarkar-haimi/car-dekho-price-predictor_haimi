import streamlit as st
import pandas as pd
import numpy as np
import datetime
import helper

df = pd.read_csv('data/covid_19_india.csv')

# preprocessing
df = df[df['State/UnionTerritory'] != 'Unassigned']
df = df[df['State/UnionTerritory'] != 'Cases being reassigned to states']

states_list = np.sort(df['State/UnionTerritory'].unique())
states_list = np.insert(states_list,0,'All India')

selected_state = st.sidebar.selectbox(
    "Select a State",
    states_list
)

start_date = st.sidebar.date_input("Start Date",datetime.date(2020, 1, 30))
end_date = st.sidebar.date_input("End Date",datetime.date(2021, 5, 16))

# total cases
total_cases = helper.return_total_cases(df,start_date,end_date,selected_state,'Confirmed')
total_deaths = helper.return_total_cases(df,start_date,end_date,selected_state,'Deaths')

col1, col2, col3, col4 = st.beta_columns(4)

with col1:
    st.title('Total Cases')
    st.header(total_cases)
with col2:
    st.title('Total Deaths')
    st.header(total_deaths)