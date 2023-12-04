# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 06:12:53 2020

@author: Administrator
"""


import streamlit as st
import numpy as np
import pandas as pd


st.title('Position Size BankNifty')
#st.write("Here's my first attempt at writing some text")

path_string_1='./'

file_string_1=path_string_1+'strategyposition.csv'
df_position=pd.read_csv(file_string_1)
file_string_2=path_string_1+'positionsummary.csv'
# df_strategy=pd.read_csv(file_string_2)
df_position_1=pd.read_csv(path_string_1+'Positions.csv')
df_position=pd.concat([df_position,df_position_1])
#df_position=df_position.merge(df_strategy,left_on='Strategy',right_on='Strategy')
#cols=['ID','Strategy','Position','Trade Price','Trade Time','Eval Time','Status']
#df_position=df_position[cols]

add_selectbox = st.sidebar.selectbox(
    'Position in Account?',
    ('HUF', 'Samrup', 'Star','Galaxy','Neptune','Galaxy-5P','Neptune-5P','Total')
)
if add_selectbox=='HUF':
    st.write(add_selectbox)
    df_filter=df_position[df_position['Strategy'].str[-1]== 'H']
elif add_selectbox=='Samrup':
    st.write(add_selectbox)
    df_filter=df_position[df_position['Strategy'].str[-1]== 'S'] 
elif add_selectbox=='Star':
    st.write(add_selectbox)
    df_filter=df_position[df_position['Strategy'].str[-1]== 'M']
elif add_selectbox=='Galaxy':
    st.write(add_selectbox)
    df_filter=df_position[(df_position['Strategy'].str[-1]== 'G') & (df_position['Strategy'].str[0]=='N')]
elif add_selectbox=='Neptune':
    st.write(add_selectbox)
    df_filter=df_position[(df_position['Strategy'].str[0]== 'N') & (df_position['Strategy'].str[-1]=='N')]
elif add_selectbox=='Galaxy-5P':
    st.write(add_selectbox)
    df_filter=df_position[(df_position['Strategy'].str[0:2]== 'P5') & (df_position['Strategy'].str[-1]=='G')]
elif add_selectbox=='Neptune-5P':
    st.write(add_selectbox)
    df_filter=df_position[(df_position['Strategy'].str[0:2]== 'P5') & (df_position['Strategy'].str[-1]=='N')]   
elif add_selectbox=='Total':
    df_filter=df_position.copy()
total_position=df_position['Position'].sum()

st.write('Total Bank Nifty Position Size is '+str(total_position))
st.write(df_filter)
df_position_summary=pd.read_csv(file_string_2)
total_m2m=df_position_summary['M2M'].sum()
total_margin_available=df_position_summary['Margin Available'].sum()
total_bn_futures=df_position_summary['BN Futures'].sum()

st.write(df_position_summary)
st.write('Total M2M for day: '+str(total_m2m))
st.write('Total Margin Available: '+str(total_margin_available))
st.write('Actual BN Futures: '+str(total_bn_futures))
st.write('Theoretical BN Position: '+str(total_position))
