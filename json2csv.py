import pandas as pd
import json
import argparse

parser = argparse.ArgumentParser(description='Process Json File')
parser.add_argument('--check24core', action='store_true')
parser.add_argument('--check24all', action='store_true')
parser.add_argument('--check24adjusted', action='store_true')
args = parser.parse_args()

with open('rows.json') as f:
  df = pd.json_normalize(json.load(f)['rows']).dropna(axis=1, how='all')

df = df[df.columns[~df.applymap(lambda x: isinstance(x, list)).any()]]
df_simple = df[
  [
    "pricelayer.prices.effective.amount",
    "pricelayer.provider.name",
    "tariff.names.default",
    "tariff.network.name",
    "tariff.internet.pricePerUnit.price.amount",
    "tariff.internet.traffic.value",
    "tariff.internet.speed.value",
    "tariff.ageCheck",
    "tariff.voice.highestPrice.amount",
    "tariff.voice.flatrate",
    "tariff.sms.highestPrice.amount",
    "tariff.sms.flatrate",
    "tariff.contract.periods.contract.value",
    "tariff.contract.periods.contract.unit",
  ]
]

if args.check24core:
  df_simple.to_csv("rows-simple.csv", index=False)

if args.check24all:
  df.to_csv("rows.csv", index=False)
  for c in df.columns:
    print(c)

if args.check24adjusted:
  df_simple.replace(
    to_replace = {
      'pricelayer.provider.name': {"web.de": "gmx.de"}
    }
  ).sort_values(
    by=[
      "pricelayer.prices.effective.amount", 
      "pricelayer.provider.name"
    ]
  ).to_csv(
    path_or_buf="rows-adjusted.csv", 
    index=False
  )
