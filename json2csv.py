import pandas as pd
import json

with open('rows.json') as f:
  df = pd.json_normalize(json.load(f)['rows']).dropna(axis=1, how='all')

df = df[df.columns[~df.applymap(lambda x: isinstance(x, list)).any()]]
df.to_csv("rows.csv", index=False)
