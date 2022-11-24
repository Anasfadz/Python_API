import pandas as pd
import requests

count = 0

while count <= 4:
  dataset = pd.read_csv("point.csv")

  client_id = int(dataset['Client_id'][count])
  point = float(dataset['point'][count])
  outlet = str(dataset['outlet'][count])

  print(client_id, '|', point, '|', outlet)

  url = "https://api.xilnex.com/logic/v2/clients/pointadjust"

  body = {
    "clientPoint": {
      "clientId": client_id,
      "pointAdjustment": point,
      "remark": "Normal Point",
      "outlet": outlet,
      "expiryDate": "",
      "salesId": "",
      "isIntegrationPosted": "true"
    }
  }

  headers = {"Content-Type": "application/json", "appid": "**** id put here ******",
             "token": "***** token put here ******", "auth": "**** auth put here *****"}

  response = requests.put(url, headers=headers, json=body)

  print("Status Code", response.status_code, response.text)
  print('----------------------------------------------------------------------------------------------------------------')

  count +=1
