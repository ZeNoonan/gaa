import pandas as pd
import numpy as np
import streamlit as st
import altair as alt

st.set_page_config(layout="wide")

odds_pts_listing = pd.read_excel("C:/Users/Darragh/Documents/Python/gaa/gaa_football_2024.xlsx",sheet_name='odds_pts_listing',parse_dates=['Date'])
week_1 = pd.read_excel("C:/Users/Darragh/Documents/Python/gaa/gaa_football_2024.xlsx",sheet_name='week_1')
week_2 = pd.read_excel("C:/Users/Darragh/Documents/Python/gaa/gaa_football_2024.xlsx",sheet_name='week_2')
football_results=pd.read_excel("C:/Users/Darragh/Documents/Python/gaa/GAA Elo ratings - Football 5_feb_24.xlsx",sheet_name='2024',header=0)\
    .loc[:,['Date','Grade','Team 1','Sc','Team 2','Sc.1']].dropna(subset=['Date'])


football_results['home_win']=np.where(football_results['Sc']>football_results['Sc.1'],1,np.where(football_results['Sc']<football_results['Sc.1'],-1,0))

st.write(football_results)

week_1=pd.melt(week_1,id_vars=['Week','Name'],var_name='match_ID',value_name='pick_selection')
week_2=pd.melt(week_2,id_vars=['Week','Name'],var_name='match_ID',value_name='pick_selection')
all_weeks_picks_made=pd.concat([week_1,week_2])
st.write('picks listing',all_weeks_picks_made)
# st.write('week 1', week_1)
# st.write(pd.melt(week_1,id_vars=['Week','Name'],var_name='match_ID',value_name='pick_selection'))
# st.write('week 2', week_2)
