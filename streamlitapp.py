# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 06:12:53 2020

@author: Administrator
"""


import streamlit as st
import numpy as np
import pandas as pd


st.title('Position Size BankNifty')
# #st.write("Here's my first attempt at writing some text")
path_string_1=
file_string_1='positionsummary.csv'
df_position=pd.read_csv(file_string_1)
# file_string_2="Strategy.csv"
# df_strategy=pd.read_csv(file_string_2)
# df_position_1=pd.read_csv('Positions.csv')
# df_position=pd.concat([df_position,df_position_1])
# #df_position=df_position.merge(df_strategy,left_on='Strategy',right_on='Strategy')
# #cols=['ID','Strategy','Position','Trade Price','Trade Time','Eval Time','Status']
# #df_position=df_position[cols]
#
# add_selectbox = st.sidebar.selectbox(
#     'Position in timeframe?',
#     ('5 min', '15 min', '30 min','60 min','Daily','5Paisa','Total')
# )
# if add_selectbox=='5 min':
#     st.write(add_selectbox)
#     df_filter=df_position[df_position['Strategy'].str[0:2]== 'N5']
# elif add_selectbox=='15 min':
#     st.write(add_selectbox)
#     df_filter=df_position[df_position['Strategy'].str[0:3]== 'N15']
# elif add_selectbox=='30 min':
#     st.write(add_selectbox)
#     df_filter=df_position[df_position['Strategy'].str[0:3]== 'N30']
# elif add_selectbox=='60 min':
#     st.write(add_selectbox)
#     df_filter=df_position[df_position['Strategy'].str[0:3]== 'N60']
# elif add_selectbox=='Daily':
#     st.write(add_selectbox)
#     df_filter=df_position[df_position['Strategy'].str[0:2]== 'ND']
# elif add_selectbox=='5Paisa':
#     st.write(add_selectbox)
#     df_filter=df_position[df_position['Strategy'].str[0:2]== 'P5']
#
# elif add_selectbox=='Total':
#     df_filter=df_position[df_position['Strategy'].str[0]!='F']
# total_position=df_filter['Position'].sum()
#
# st.write('Total Bank Nifty Position Size is '+str(total_position))
# st.write(df_filter)
# df_position_summary=pd.read_csv('positionsummary.csv')
# total_m2m=df_position_summary['M2M'].sum()
# st.write(df_position_summary)
# st.write('Total M2M for day:'+str(total_m2m))

