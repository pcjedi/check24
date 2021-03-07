import pandas as pd
import json

with open('rows.json') as f:
  df = pd.json_normalize(json.load(f)['rows']).dropna(axis=1, how='all')

df = df[df.columns[~df.applymap(lambda x: isinstance(x, list)).any()]]
df.to_csv("rows.csv", index=False)

for c in df.columns:
  print(c)

try:
  df[
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
  ].to_csv("rows-simple.csv", index=False)
except KeyError as e:
  print(e)
