from pathlib import Path

import pandas as pd

DATA_FILE = Path(__file__).resolve().parent / "results.csv"
df = pd.read_csv(DATA_FILE)
important = [
    'FIFA World Cup',
    'FIFA World Cup qualification',
    'UEFA Euro',
    'UEFA Euro qualification',
    'Copa América',
    'AFC Asian Cup',
    'African Cup of Nations',
    'Confederations Cup',
    'Friendly'
]

df_filtered = df[df["tournament"].isin(important)].copy()
df_filtered["date"] = pd.to_datetime(df_filtered["date"])
df_filtered = df_filtered[df_filtered["date"].dt.year >= 2014]
df_filtered = df_filtered.sort_values("date")
#print(df_filtered.shape)
#print(df_filtered.head(10))
#print(df_filtered["tournament"].value_counts())

def get_result(row):
    if row["home_score"] > row["away_score"]:
        return 1
    elif row['home_score'] < row["away_score"]:
        return -1
    else:
        return 0
    
df_filtered["result"] = df_filtered.apply(get_result, axis=1)
#print(df_filtered[["home_team", "away_team", "home_score", "away_score", "result"]].head(10))


def get_recent_form(team, match_date):
    match_date = pd.to_datetime(match_date)
    team_matches = df_filtered[
        (
            (df_filtered["home_team"] == team)
            | (df_filtered["away_team"] == team)
        )
        & (df_filtered["date"] < match_date)
    ]
    #print(len(team_matches))
    recent_matches = team_matches.tail(10)
    points = 0

    for _, row in recent_matches.iterrows():
        if row["home_team"] ==  team:
            team_score = row["home_score"]
            opponent_score = row["away_score"]
        else:
            team_score = row["away_score"]
            opponent_score = row["home_score"]

        if team_score > opponent_score:
            points += 3
        elif team_score == opponent_score:
            points += 1
    return points / 30 

home_forms = []
away_forms = []

for _, row in  df_filtered.iterrows():
    home_form = get_recent_form(
        row["home_team"] , 
        row["date"] 
    )
    away_form = get_recent_form(
        row["away_team"] ,
        row["date"]
    ) 

    home_forms.append(home_form)
    away_forms.append(away_form)

df_filtered["home_form"] = home_forms
df_filtered["away_form"] = away_forms

#print (df_filtered.iloc[3000:3010])

def average_goals_scored(team, match_date):
    match_date = pd.to_datetime(match_date)

    team_matches = df_filtered[
        (
            (df_filtered["home_team"] == team)
            | (df_filtered["away_team"] == team)
        )
        & (df_filtered["date"] < match_date)
    ]
    recent_matches = team_matches.tail(10)
    total_goals = 0

    for _, row in recent_matches.iterrows():
        if row["home_team"] == team:
            team_goals = row["home_score"]
        else:
            team_goals = row["away_score"]

        total_goals += team_goals

    return total_goals / 10 

print(average_goals_scored("Argentina", "2026-4-7"))
