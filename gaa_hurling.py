import pandas as pd
import numpy as np
import streamlit as st
import altair as alt
import datetime as dt
from st_aggrid import AgGrid, GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, JsCode

st.set_page_config(layout="wide")


# df = pd.DataFrame({'model':np.random.randint(1,10,100), 'value':np.random.randn(100)})
# st.write(df)
# first_five = df['model'].sort_values(inplace=False).unique()[:5]
# gp = df[df['model'].isin(first_five)]
# st.write(gp)
# st.write(gp.first())


convert_excel_to_csv = pd.read_excel("C:/Users/Darragh/Documents/Python/gaa/hurling_2023.xlsx",sheet_name='Players',parse_dates=['Date'])
convert_excel_to_csv.to_csv('C:/Users/Darragh/Documents/Python/gaa/hurling_2023_players_data.csv')


df = pd.read_excel("C:/Users/Darragh/Documents/Python/gaa/gaa_hurling.xlsx",sheet_name='2022',parse_dates=['Date'])
df_2021 = pd.read_excel("C:/Users/Darragh/Documents/Python/gaa/gaa_hurling.xlsx",sheet_name='2021',parse_dates=['Date'])
df_2020 = pd.read_excel("C:/Users/Darragh/Documents/Python/gaa/gaa_hurling.xlsx",sheet_name='2020',parse_dates=['Date'])
df_2019 = pd.read_excel("C:/Users/Darragh/Documents/Python/gaa/gaa_hurling.xlsx",sheet_name='2019',parse_dates=['Date'])
elo_ratings=pd.read_excel("C:/Users/Darragh/Documents/Python/gaa/gaa_hurling.xlsx",sheet_name='Elo values')
# st.write(df)

# st.write( df[df['Grade'].isin({'Provincial','All-Ireland'})] )
def all_ireland_df(df):
    df=df.reset_index().rename(columns={'index':'unique_date_sort'})
    df=df[df['Grade'].isin({'Provincial','All-Ireland','Qualifier'})]
    df['Round']=df['Round'].fillna('provincial')
    # https://stackoverflow.com/questions/30631841/pandas-how-do-i-assign-values-based-on-multiple-conditions-for-existing-columns
    conditions = [df['Round'].eq('final'),df['Round'].eq('semi_final'),df['Round'].eq('quarter_final'),df['Round'].eq('provincial_final'),df['Round'].eq('provincial')]
    choices = [64,32,16,8,4]
    df['winner_points'] = np.select(conditions, choices, default=0)
    df['loser_points']=df['winner_points']/2
    df['home_win']=np.where(df['Sc']>df['Sc.1'],1,np.where(df['Sc']<df['Sc.1'],-1,0))
    df['team_1_points']=np.where(df['home_win']>0,df['winner_points'],np.where(df['home_win']<0,df['loser_points'],(df['winner_points']+df['loser_points'])/2))
    df['team_2_points']=np.where(df['home_win']<0,df['winner_points'],np.where(df['home_win']>0,df['loser_points'],(df['winner_points']+df['loser_points'])/2))
    df_filtered_out_crap_teams=df[ (df['Elo']>1600) & (df['Elo.1']>1600) ]
    df_crap_teams_to_check=df[~ (df['Elo']>1600) | ~(df['Elo.1']>1600) ]
    cols_to_move=['Date','Grade','Round','Team 1','Elo','Team 2','Elo.1','Sc','Sc.1','winner_points','loser_points','home_win','team_1_points','team_2_points']
    cols = cols_to_move + [col for col in df_filtered_out_crap_teams if col not in cols_to_move]
    df_filtered_out_crap_teams=df_filtered_out_crap_teams[cols].loc[:,['Date','Grade','Round','Team 1','Elo','Team 2','Elo.1','Sc','Sc.1','winner_points','loser_points',
    'home_win','team_1_points','team_2_points','G','P','G.1','P.1','unique_date_sort']]
    return df_filtered_out_crap_teams,df_crap_teams_to_check

def melt_df(df):  # sourcery skip: inline-immediately-returned-variable
    df=df.loc[:,['Team 1','team_1_points','Team 2','team_2_points','unique_date_sort']]
    home_df=df.loc[:,['Team 1','team_1_points','unique_date_sort']].rename(columns={'Team 1':'team','team_1_points':'points'})
    away_df=df.loc[:,['Team 2','team_2_points','unique_date_sort']].rename(columns={'Team 2':'team','team_2_points':'points'})
    # st.write('home', home_df)
    # st.write('away', away_df)
    df=pd.concat((home_df,away_df),axis=0,ignore_index=True)
    return df

df_filtered_out_crap_teams,df_crap_teams_to_check=all_ireland_df(df)
# st.write('filtered', df_filtered_out_crap_teams)
melted_df=melt_df(df_filtered_out_crap_teams)
# st.write('melt', melted_df)

def calculate_rolling_points(df):
    df=df.sort_values(by=['team','unique_date_sort'],ascending=True)
    df['cumulal_points']=df.groupby(['team'])['points'].cumsum()
    df['cumulal_games']=df.groupby(['team'])['points'].cumcount()+1
    df['pts_per_game']=df['cumulal_points']/df['cumulal_games']
    return df

def last_game_played(df,year=2022):
    df=df.sort_values(by=['team','unique_date_sort'],ascending=True).drop_duplicates(subset=['team'],keep='last')
    df['year']=year
    return df.sort_values(by=['pts_per_game'],ascending=False)

calcs_df=calculate_rolling_points(melted_df)
points_table_2022=last_game_played(calcs_df)

def run_functions_together(df,year=2021):
    df_filtered_out_crap_teams,df_crap_teams_to_check=all_ireland_df(df)
    melted_df=melt_df(df_filtered_out_crap_teams)
    calcs_df=calculate_rolling_points(melted_df)
    points_table=last_game_played(calcs_df,year=year)
    return df_filtered_out_crap_teams,calcs_df,points_table



st.write('Notes: have read in the 2022 season')
st.write('what is the criteria that i have used')
st.write('Winner of provincial round robin gets 4 points, loser 2 points, winner of provincial final gets 8 points, loser gets 4 points')
st.write('winner quarter final only 2 in hurling gets 16 points, loser gets 8 points')
st.write('winner semi final gets 32 points, loser gets 16 points')
st.write('winner final gets 64 points, loser gets 32 points')
st.write('Note that have tried to filter out games where say kilkenny plays westmeath by filtering on the ELO rating, all games where one \
team has an ELO rating of less than 1600 gets filtered out')
st.write('2022 listing games', calcs_df)
st.write('2022 points table', points_table_2022)

df_filtered_out_crap_teams_2021,calcs_df_2021,points_table_2021=run_functions_together(df_2021,year=2021)
# st.write('2021 listing games', calcs_df_2021)
st.write('2021 points table', points_table_2021)
# st.write('2021 games listing it was knockout cos of COVID', df_filtered_out_crap_teams_2021)

df_filtered_out_crap_teams_2020,calcs_df_2020,points_table_2020=run_functions_together(df_2020,year=2020)
# st.write('2021 listing games', calcs_df_2020)
st.write('2020 points table', points_table_2020)
# st.write('2021 games listing', df_filtered_out_crap_teams_2020)

df_filtered_out_crap_teams_2019,calcs_df_2019,points_table_2019=run_functions_together(df_2019,year=2019)
points_table_2019=points_table_2019 [points_table_2019['team']!= 'Laois'] # laois played in quarter final get rid of them
st.write('2019 points table', points_table_2019)
combined_years=pd.concat((points_table_2022,points_table_2021,points_table_2020,points_table_2019),axis=0,ignore_index=True)\
    .sort_values(by=['year'],ascending=True)

weights_1 = np.array([0.125,0.25,0.5,1])
sum_weights_1 = np.sum(weights_1)
# combined_years['Weighted_ma_1'] = combined_years.groupby('team')['pts_per_game'].apply(lambda x: np.convolve(x, weights_1, 'valid') / sum_weights_1)
combined_years['Weighted_ma_2'] = combined_years.groupby('team')['pts_per_game'].apply(lambda x: x.rolling(window=len(weights_1), center=False)\
            .apply(lambda x: np.sum(weights_1*x) / sum_weights_1, raw=False))
# groupby on team using ewm with alpha of 0.5
combined_years['weighted'] = combined_years.groupby('team')['pts_per_game'].transform(lambda x: x.ewm(alpha=0.5).mean())
st.write('weighted and weighted ma are the same just the formula is different but same result')
st.write('can i get the percent of poitns that each team has and then convert that to betting odds would be a good exercise and then compare to actual betting odds')
st.write(combined_years.groupby('year')['weighted'].transform('sum'))
combined_years['combined annual points']=combined_years.groupby('year')['weighted'].transform('sum')
combined_years['%_combined annual points']=combined_years['weighted'] / combined_years['combined annual points']
combined_years['odds'] = 1 / combined_years['%_combined annual points']


combined_years.loc [ (combined_years['year']==2022)&(combined_years['team']=='Limerick'), 'book_odds' ] = 1.9
combined_years.loc [ (combined_years['year']==2022)&(combined_years['team']=='Kilkenny'), 'book_odds' ] = 7
combined_years.loc [ (combined_years['year']==2022)&(combined_years['team']=='Galway'), 'book_odds' ] = 7
combined_years.loc [ (combined_years['year']==2022)&(combined_years['team']=='Cork'), 'book_odds' ] = 11
combined_years.loc [ (combined_years['year']==2022)&(combined_years['team']=='Clare'), 'book_odds' ] = 13
combined_years.loc [ (combined_years['year']==2022)&(combined_years['team']=='Waterford'), 'book_odds' ] = 13
combined_years.loc [ (combined_years['year']==2022)&(combined_years['team']=='Tipperary'), 'book_odds' ] = 15
combined_years.loc [ (combined_years['year']==2022)&(combined_years['team']=='Wexford'), 'book_odds' ] = 26
combined_years.loc [ (combined_years['year']==2022)&(combined_years['team']=='Dublin'), 'book_odds' ] = 51
combined_years['variance_odds'] = combined_years['odds'] - combined_years['book_odds']
st.write('combined years', combined_years.sort_values(by=['year','weighted'],ascending=[False,False]))
# st.write('check Kilkenny ERROR here and in FPL, need to group it by player or team check NFL')
st.write('fixed above, but now need to check waterford its ok i downloaded spreadsheet and checked Waterford is ok')
st.write('maybe some value in Waterford??')
st.write('elo', elo_ratings)
# st.download_button(label="Download data as CSV",data=combined_years.sort_values(by=['team','year'],ascending=True).to_csv().encode('utf-8'),file_name='df_spread.csv',mime='text/csv',key='after_merge_spread')
# st.write('2019 games listing', df_filtered_out_crap_teams_2019)
# st.write('what is going on with Laois???')

# st.write('full df', df_filtered_out_crap_teams)
# st.write('dross', df_crap_teams_to_check)