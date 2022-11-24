import requests
import csv
import pandas as pd

count = 0

while count <= 362:
  dataset = pd.read_csv("customer_record (7).csv")

  phone_no = str(dataset['phone_no'][count])

  print(count, '|', phone_no)

  url = "https://api.xilnex.com/logic/V2/clients/query?mobile=" + phone_no

  headers = {"Content-Type": "application/json", "appid": "***** id put here ******",
             "token": "***** token put here ******", "auth": "**** auth put here *****"}

  response = requests.get(url, headers=headers)

  myjson = response.json()

  print(myjson)
  ourdata = []
  csvhdr = ['phone_no', 'client_id']

  for x in myjson["data"]["clients"]:
      listing = [phone_no, x["id"]]
      ourdata.append(listing)

      print(ourdata)

  if count == 0:
      with open('customer_id.csv', 'w', newline='') as f:
          writer = csv.writer(f)
          writer.writerow(csvhdr)
          writer.writerows(ourdata)

      f.close()

  else:
      with open('customer_id.csv', 'a', newline='') as f:
          writer = csv.writer(f)
          writer.writerows(ourdata)

  count +=1

