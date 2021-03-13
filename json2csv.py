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
core = [
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

if args.check24core:
  df[core].to_csv("rows-simple.csv", index=False)

if args.check24all:
  df.to_csv("rows.csv", index=False)
  for c in df.columns:
    print(c)

if args.check24adjusted:
  df_core = df[core]
  df_core.loc[df_core["tariff.names.default"]=="WhatsAll 4000", "tariff.internet.traffic.value"] = 4000
  df_core = df_core.replace(
    to_replace = {
      'pricelayer.provider.name': {
        "web.de": "gmx.de",
        "Penny Mobil": "ja! mobil"
      },
      'tariff.network.name': {
        "o2": "Telefónica"
      }
    }
  ).sort_values(
    by = [
      "pricelayer.prices.effective.amount", 
      "pricelayer.provider.name",  
      "tariff.names.default",
    ]
  )
  df_core.to_csv(
    path_or_buf="rows-adjusted.csv", 
    index=False
  )
  
  df_core = df_core[df_core["tariff.internet.pricePerUnit.price.amount"]==0]
  df_core["24m"] = False
  df_core.loc[
    (df_core["tariff.contract.periods.contract.value"] == 24) & 
    (df_core["tariff.contract.periods.contract.unit"] == "month"), 
    "24m"
  ] = True
  df_core.groupby([
        "tariff.internet.traffic.value", 
        "tariff.network.name", 
        "tariff.ageCheck", 
        "24m"
  ])[
      "pricelayer.prices.effective.amount"
  ].min().reset_index().to_csv(
    path_or_buf="grouped-minimum.csv", 
    index=False
  )
