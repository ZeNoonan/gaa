import pandas as pd
import numpy as np
import streamlit as st
import altair as alt
from PIL import Image
# from vega_datasets import data
# from altair.expr import datum, if_

st.set_page_config(layout="wide")

# odds_pts_listing = pd.read_excel("C:/Users/Darragh/Documents/Python/gaa/gaa_football_2024.xlsx",sheet_name='odds_pts_listing',parse_dates=['Date'])

# pd.read_excel("C:/Users/Darragh/Documents/Python/gaa/gaa_football_2024.xlsx",sheet_name='odds_pts_listing',parse_dates=['Date']).\
#     to_parquet('C:/Users/Darragh/Documents/Python/gaa/odds_pts_listing.parq')
# odds_pts_listing=pd.read_parquet('C:/Users/Darragh/Documents/Python/gaa/odds_pts_listing.parq')
odds_pts_listing=pd.read_parquet('https://raw.githubusercontent.com/ZeNoonan/gaa/master/odds_pts_listing.parq')

# pd.read_excel("C:/Users/Darragh/Documents/Python/gaa/gaa_football_2024.xlsx",sheet_name='week_1').\
#     to_parquet('C:/Users/Darragh/Documents/Python/gaa/week_1.parq')
# pd.read_excel("C:/Users/Darragh/Documents/Python/gaa/gaa_football_2024.xlsx",sheet_name='week_2').\
#     to_parquet('C:/Users/Darragh/Documents/Python/gaa/week_2.parq')
# pd.read_excel("C:/Users/Darragh/Documents/Python/gaa/gaa_football_2024.xlsx",sheet_name='week_3').\
#     to_parquet('C:/Users/Darragh/Documents/Python/gaa/week_3.parq')
# pd.read_excel("C:/Users/Darragh/Documents/Python/gaa/gaa_football_2024.xlsx",sheet_name='week_4').\
#     to_parquet('C:/Users/Darragh/Documents/Python/gaa/week_4.parq')
# pd.read_excel("C:/Users/Darragh/Documents/Python/gaa/gaa_football_2024.xlsx",sheet_name='week_5').\
#     to_parquet('C:/Users/Darragh/Documents/Python/gaa/week_5.parq')
# pd.read_excel("C:/Users/Darragh/Documents/Python/gaa/gaa_football_2024.xlsx",sheet_name='check_totals').\
#     to_parquet('C:/Users/Darragh/Documents/Python/gaa/check_totals.parq')

# week_1 = pd.read_excel("C:/Users/Darragh/Documents/Python/gaa/gaa_football_2024.xlsx",sheet_name='week_1')
# week_2 = pd.read_excel("C:/Users/Darragh/Documents/Python/gaa/gaa_football_2024.xlsx",sheet_name='week_2')
# week_3 = pd.read_excel("C:/Users/Darragh/Documents/Python/gaa/gaa_football_2024.xlsx",sheet_name='week_3')
# week_4 = pd.read_excel("C:/Users/Darragh/Documents/Python/gaa/gaa_football_2024.xlsx",sheet_name='week_4')
# week_5 = pd.read_excel("C:/Users/Darragh/Documents/Python/gaa/gaa_football_2024.xlsx",sheet_name='week_5')
# check_totals=pd.read_excel("C:/Users/Darragh/Documents/Python/gaa/gaa_football_2024.xlsx",sheet_name='check_totals')

# week_1 = pd.read_parquet("C:/Users/Darragh/Documents/Python/gaa/week_1.parq")
# week_2 = pd.read_parquet("C:/Users/Darragh/Documents/Python/gaa/week_2.parq")
# week_3 = pd.read_parquet("C:/Users/Darragh/Documents/Python/gaa/week_3.parq")
# week_4 = pd.read_parquet("C:/Users/Darragh/Documents/Python/gaa/week_4.parq")
# week_5 = pd.read_parquet("C:/Users/Darragh/Documents/Python/gaa/week_5.parq")
week_1 = pd.read_parquet("https://raw.githubusercontent.com/ZeNoonan/gaa/master/week_1.parq")
week_2 = pd.read_parquet("https://raw.githubusercontent.com/ZeNoonan/gaa/master/week_2.parq")
week_3 = pd.read_parquet("https://raw.githubusercontent.com/ZeNoonan/gaa/master/week_3.parq")
week_4 = pd.read_parquet("https://raw.githubusercontent.com/ZeNoonan/gaa/master/week_4.parq")
week_5 = pd.read_parquet("https://raw.githubusercontent.com/ZeNoonan/gaa/master/week_5.parq")

# check_totals=pd.read_parquet("C:/Users/Darragh/Documents/Python/gaa/check_totals.parq")
check_totals=pd.read_parquet("https://raw.githubusercontent.com/ZeNoonan/gaa/master/check_totals.parq")
# st.write('week 1 before',week_1.dtypes)
# st.write(week_1)
# check_totals=pd.read_excel("C:/Users/Darragh/Documents/Python/gaa/gaa_football_2024_prov.xlsx",sheet_name='check_totals')
# football_results=pd.read_excel("C:/Users/Darragh/Documents/Python/gaa/GAA Elo ratings - Football 5_feb_24.xlsx",sheet_name='2024',header=0)\
#     .loc[:,['Date','Grade','Team 1','Sc','Team 2','Sc.1']].dropna(subset=['Date']).rename(columns={'Team 1':'Home Team','Team 2':'Away Team'})
# football_results=pd.read_excel("C:/Users/Darragh/Documents/Python/gaa/GAA Elo ratings - Football_2024.xlsx",sheet_name='2024',header=0)\
#     .loc[:,['Date','Grade','Team 1','Sc','Team 2','Sc.1']].dropna(subset=['Date']).rename(columns={'Team 1':'Home Team','Team 2':'Away Team'})
# football_results.to_parquet('C:/Users/Darragh/Documents/Python/gaa/football_results.parq')
# football_results=pd.read_parquet('C:/Users/Darragh/Documents/Python/gaa/football_results.parq')
football_results=pd.read_parquet('https://raw.githubusercontent.com/ZeNoonan/gaa/master/football_results.parq')
# football_results=pd.read_excel("C:/Users/Darragh/Documents/Python/gaa/GAA Elo ratings - Football_2024_prov.xlsx",sheet_name='2024',header=0)\
#     .loc[:,['Date','Grade','Team 1','Sc','Team 2','Sc.1']].dropna(subset=['Date']).rename(columns={'Team 1':'Home Team','Team 2':'Away Team'})

football_results['home_win']=np.where(football_results['Sc']>football_results['Sc.1'],1,np.where(football_results['Sc']<football_results['Sc.1'],-1,0))

week_1=pd.melt(week_1,id_vars=['Week','Name'],var_name='match_ID',value_name='pick_selection')
# st.write(week_1)
week_2=pd.melt(week_2,id_vars=['Week','Name'],var_name='match_ID',value_name='pick_selection')
week_3=pd.melt(week_3,id_vars=['Week','Name'],var_name='match_ID',value_name='pick_selection')
week_4=pd.melt(week_4,id_vars=['Week','Name'],var_name='match_ID',value_name='pick_selection')
week_5=pd.melt(week_5,id_vars=['Week','Name'],var_name='match_ID',value_name='pick_selection')
# st.write('week 1',week_1.dtypes)
all_weeks_picks_made=pd.concat([week_1,week_2,week_3,week_4,week_5])
all_weeks_picks_made['match_ID']=all_weeks_picks_made['match_ID'].astype(float)

# st.write('picks listing',all_weeks_picks_made)
# st.write(odds_pts_listing.dtypes)
# st.write(football_results.dtypes)
master_listing=pd.merge(odds_pts_listing,football_results,on=['Date','Home Team','Away Team'],how='outer', indicator=True)
master_listing['betting_favourite']=np.where(master_listing['Home_odds']<master_listing['Away_odds'],1,np.where(master_listing['Away_odds']<master_listing['Home_odds'],-1,0))
master_listing['betting_favourite_name']=np.where(master_listing['Home_odds']<master_listing['Away_odds'],master_listing['Home Team'],
                                                  np.where(master_listing['Away_odds']<master_listing['Home_odds'],master_listing['Away Team'],"Pick 'em"))
master_listing['betting_underdog_name']=np.where(master_listing['Home_odds']>master_listing['Away_odds'],master_listing['Home Team'],
                                                  np.where(master_listing['Away_odds']>master_listing['Home_odds'],master_listing['Away Team'],"Pick 'em"))
# master_listing['sum_odds']=
master_listing['hold_%']=(1-((master_listing['Away_odds']-1)*(master_listing['Home_odds']/master_listing['Away_odds']))) / (1+master_listing['Home_odds']/master_listing['Away_odds'])
# st.write('combined always check the merge indicator', master_listing.sort_values(by=['Closing Spread'],key=abs,ascending=True))

# st.write(all_weeks_picks_made.dtypes)
# st.write(all_weeks_picks_made)
# st.write(master_listing.dtypes)
updated_pick_listing=pd.merge(all_weeks_picks_made,master_listing.loc[:,['Date','match_ID','Home Team','Away Team','Home_comp_pts',
                                                                         'Away_comp_pts','Draw_comp_pts','home_win','betting_favourite',
                                                                         'betting_favourite_name','betting_underdog_name']]\
                              ,on=['match_ID'],how='outer',indicator=True)


updated_pick_listing['pick_id']=np.where(updated_pick_listing['pick_selection']==updated_pick_listing['Home Team'],1,
                                         np.where(updated_pick_listing['pick_selection']==updated_pick_listing['Away Team'],-1,0))

# updated_pick_listing['pick_id_name']=np.where(updated_pick_listing['pick_selection']==updated_pick_listing['Home Team'],updated_pick_listing['Home Team'],
#                                          np.where(updated_pick_listing['pick_selection']==updated_pick_listing['Away Team'],updated_pick_listing['Away Team'],'Draw'))

updated_pick_listing['pick_result']=np.where(updated_pick_listing['pick_id']==updated_pick_listing['home_win'],1,0)
updated_pick_listing['pick_pts']=np.where(updated_pick_listing['pick_id']==1,updated_pick_listing['Home_comp_pts']*updated_pick_listing['pick_result'],
                                          np.where(updated_pick_listing['pick_id']==-1,updated_pick_listing['Away_comp_pts']*updated_pick_listing['pick_result'],
                                          updated_pick_listing['Draw_comp_pts']*updated_pick_listing['pick_result']))

draw_picked = updated_pick_listing['pick_selection']=='Draw'

# updated_pick_listing['user_betting_fav_picked'] = np.where(updated_pick_listing['betting_favourite'] == updated_pick_listing['pick_id'],1,-1)
# updated_pick_listing['user_betting_fav_picked'] = updated_pick_listing['betting_favourite'] * updated_pick_listing['pick_id']
# updated_pick_listing['user_betting_fav_picked'] = np.where(updated_pick_listing['pick_selection')
not_equal_to_draw=updated_pick_listing['pick_selection']!='Draw'
favourite_picked=updated_pick_listing['pick_selection']==updated_pick_listing['betting_favourite_name']
underdog_picked=updated_pick_listing['pick_selection']==updated_pick_listing['betting_underdog_name']
pick_em=updated_pick_listing['betting_favourite_name']=="Pick 'em"
not_pick_em=updated_pick_listing['betting_favourite_name']!="Pick 'em"
updated_pick_listing['underdog_picked']=updated_pick_listing['betting_underdog_name'].where(not_equal_to_draw & underdog_picked)
updated_pick_listing['favourite_picked']=updated_pick_listing['betting_favourite_name'].where(not_equal_to_draw & favourite_picked)
updated_pick_listing['draw_picked'] = updated_pick_listing['pick_selection'].where(draw_picked)
updated_pick_listing['pick_em']=updated_pick_listing['betting_favourite_name'].where(not_equal_to_draw & pick_em)
updated_pick_listing['dummy']=1
updated_pick_listing['underdog_picked_1']=updated_pick_listing['dummy'].where(not_equal_to_draw & underdog_picked)
updated_pick_listing['favourite_picked_1']=updated_pick_listing['dummy'].where(not_equal_to_draw & favourite_picked)
updated_pick_listing['draw_picked_1'] = updated_pick_listing['dummy'].where(draw_picked)
updated_pick_listing['pick_em_1']=updated_pick_listing['dummy'].where(not_equal_to_draw & pick_em)
updated_pick_listing['check_sum']=(updated_pick_listing.loc[:,['underdog_picked_1','favourite_picked_1','draw_picked_1','pick_em_1']].sum(axis=1))-1
# st.write('if this is True then sum all good',updated_pick_listing['check_sum'].sum()==0)
# updated_pick_listing['underdog_picked'] = 

# st.write('update', updated_pick_listing[updated_pick_listing['Name'].str.contains('Noel')])

boc_df= updated_pick_listing[ (updated_pick_listing['Name'].str.contains('Joint_Winner')) & (updated_pick_listing['Week']==4)]\
         .loc[:,['Week','Name','match_ID','pick_selection','Home Team', 'Away Team','Home_comp_pts','Away_comp_pts','home_win','pick_pts']]
thomas_df= updated_pick_listing[ (updated_pick_listing['Name'].str.contains('Winner_Joint')) & (updated_pick_listing['Week']==4)]\
         .loc[:,['match_ID','pick_selection','pick_pts']].rename(columns={'Name':'Name_person','pick_selection':'person_pick','pick_pts':'person_pts'})
merged_check=pd.merge(boc_df,thomas_df,on='match_ID',how='outer',indicator=True)
darragh_df= updated_pick_listing[ (updated_pick_listing['Name'].str.contains('Darragh')) & (updated_pick_listing['Week']==4)]\
         .loc[:,['match_ID','pick_selection','pick_pts']].rename(columns={'Name':'Darragh','pick_selection':'darragh_pick','pick_pts':'darragh_pts'})
merged_check=pd.merge(merged_check,darragh_df,on='match_ID',how='outer')
cols_to_move=['Week','match_ID','pick_selection','pick_pts','person_pick','person_pts','darragh_pick','darragh_pts','Home_comp_pts','Away_comp_pts','home_win','Home Team', 'Away Team']
cols = cols_to_move + [col for col in merged_check if col not in cols_to_move]
merged_check=merged_check[cols]
# st.write('Selection', merged_check)

# st.write('check for draws looks like it works', updated_pick_listing[updated_pick_listing['pick_id']==0])

user_results=updated_pick_listing.groupby(['Week','Name']).agg(count_winning_picks=('pick_result','sum'),sum_winning_picks=('pick_pts','sum'),
        sum_favourite_picks=('favourite_picked_1','sum'),sum_underdog_picks=('underdog_picked_1','sum'),
        sum_draw_picks=('draw_picked_1','sum'),sum_pickem_picks=('pick_em_1','sum'))\
    .sort_values(by=['Week','sum_winning_picks'],ascending=[True,False]).reset_index()
user_results=pd.merge(user_results,check_totals,how='outer',indicator=True)
user_results['check_diff']=user_results['sum_winning_picks'] - user_results['total']


# source = data.barley()
# st.write('source',source.head())

# st.altair_chart(alt.Chart(source).mark_bar().encode(
#     x='year:O',
#     y='sum(yield):Q',
#     color='year:N',
#     column='site:N'
# ))

graph_user_results=user_results.loc[:,['Week','Name','sum_favourite_picks','sum_underdog_picks','sum_draw_picks','sum_pickem_picks']]
graph_user_results=graph_user_results.melt(id_vars=['Week','Name'],value_vars=['sum_favourite_picks','sum_underdog_picks','sum_draw_picks','sum_pickem_picks'],var_name='betting',value_name='amount')
# graph_user_results=graph_user_results[~graph_user_results['Name'].str.contains('inner')]
# st.write(graph_user_results)
favourite_graph_user=graph_user_results[graph_user_results['betting']=='sum_favourite_picks']
underdog_graph_user=graph_user_results[graph_user_results['betting']=='sum_underdog_picks']
draw_graph_user=graph_user_results[graph_user_results['betting']=='sum_draw_picks']


with st.expander('Number of Correct Selections made by Entrant by Week'):

    graph_user_count_winning_picks=user_results.loc[:,['Week','Name','count_winning_picks']]
    st.altair_chart(alt.Chart(graph_user_count_winning_picks).mark_bar().encode(
        alt.X('Week:O'),
        alt.Y('count_winning_picks:Q',title='No. correct selections made'),
        alt.Column('Name:N',title='Number of correct selections picked by Week')
    ))

with st.expander('Number of Favourites picked by Entrant by Week'):

    st.altair_chart(alt.Chart(favourite_graph_user).mark_bar().encode(
        alt.X('Week:O'),
        alt.Y('amount:Q',title='No. Favourite Picks made'),
        alt.Column('Name:N',title='Number of Favourites picked by Week')
    ))

with st.expander('Number of Underdogs picked by Entrant by Week'):

    st.altair_chart(alt.Chart(underdog_graph_user).mark_bar().encode(
        alt.X('Week:O'),
        alt.Y('amount:Q',title='No. Underdog Picks made'),
        alt.Column('Name:N',title='Number of Underdogs picked by Week')
    ))

with st.expander('Number of Draws picked by Entrant by Week'):

    st.altair_chart(alt.Chart(draw_graph_user).mark_bar().encode(
        alt.X('Week:O'),
        alt.Y('amount:Q',title='No. Draw Picks made'),
        alt.Column('Name:N',title='Number of Draws picked by Week')
    ))
    # image=Image.open("C:/Users/Darragh/Documents/Python/gaa/bernie_sanders.jpg")
    image=Image.open("https://raw.githubusercontent.com/ZeNoonan/gaa/master/bernie_sanders.jpg")
    st.image(image)


with st.expander('Summary results by Entrant'):
    st.write('Summary results by Entrant ', user_results)

with st.expander('Summary results by Entrant'):
    st.write('Detailed Data Listing', updated_pick_listing)
# st.altair_chart(alt.Chart(graph_user_results).mark_bar().encode(
#     alt.X('betting:O'),
#     alt.Y('amount:Q'),
#     alt.Color('Week:N'),
#     alt.Row("Name:N"),
#     alt.Column('Name:N')
# ))



# 
# data = {'Home Team': ['Kerry', 'Dublin', 'Donegal'],
#         'Away Team': ['Derry', 'Monaghan', 'Cork'],
#         'pick_selection': ['Derry', 'Dublin', 'Cork'],
#         'pick_value': ['', '', '']
#         }
# df = pd.DataFrame(data)
# value={'Home Team':1,'Away Team':-1}
# df['pick_value'] = np.where(df['pick_selection'] == df['Home Team'], [df['Home Team']],
#                             np.where(df['pick_selection'] == df['Away Team'], [df['Away Team']], ''))
# st.write('df',df)
# # BELOW IS CHAT GPT CODE
# master_listing = pd.merge(odds_pts_listing, football_results, on=['Date', 'Home Team', 'Away Team'], how='outer', indicator=True)
# st.write('combined always check the merge indicator', master_listing)

# # Merge all_weeks_picks_made with master_listing on match_ID
# merged_df = pd.merge(all_weeks_picks_made, master_listing, on='match_ID', how='left')

# # Create a new column 'result' based on the 'home_win' column
# merged_df['result'] = np.where(merged_df['home_win'] == 1, 'Win', np.where(merged_df['home_win'] == -1, 'Loss', 'Draw'))

# # Display the final dataframe
# st.write('Merged dataframe with result', merged_df)

