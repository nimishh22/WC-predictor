import pandas as pd

df = pd.read_csv("results.csv")
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
df_filterted = df_filterted.sort_values("date")
print(df_filtered.shape)
print(df_filtered.head(10))
print(df_filtered["tournament"].value_counts())

def get_result(row):
    if row["home_score"] > row["away_score"]:
        return 1
    elif row['home_score'] < row["away_score"]:
        return -1
    else:
        return 0
    
df_filtered["result"] = df_filtered.apply(get_result, axis=1)
print(df_filtered[["home_team", "away_team", "home_score", "away_score", "result"]].head(10))