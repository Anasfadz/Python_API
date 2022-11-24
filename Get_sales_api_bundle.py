import requests
import csv
import pandas as pd

count = 4187

while count <= 4570:
  dataset = pd.read_csv("sql10.csv")

  sales_id = str(dataset['xilnex_sales_no'][count])

  print(count, '|', sales_id)

  url = "https://api.xilnex.com/logic/v2/sales/" + sales_id

  headers = {"Content-Type": "application/json", "appid": "***** id put here ********",
             "token": "***** token put here ********=", "auth": "***** auth put here *****"}

  response = requests.get(url, headers=headers)

  myjson = response.json()

  print(myjson)
  ourdata = []
  csvhdr = ['sales_id', 'outlet']

  for x in myjson["data"]["sale"]["collections"]:
      listing = [sales_id, x["outlet"]]
      ourdata.append(listing)

      print(ourdata)

  if count == 0:
      with open('outlet_sales.csv', 'w', newline='') as f:
          writer = csv.writer(f)
          writer.writerow(csvhdr)
          writer.writerows(ourdata)

      f.close()

  else:
      with open('outlet_sales.csv', 'a', newline='') as f:
          writer = csv.writer(f)
          writer.writerows(ourdata)

  count +=1

