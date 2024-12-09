import requests as req
import json
import os
from dotenv import load_dotenv

load_dotenv()

service_plan_id = os.getenv('SERVICE_PLAN_ID')
access_token = os.getenv('ACCESS_TOKEN')
from_ = os.getenv('FROM_')
to_ = os.getenv('TO_')


headers = {
    "Authorization":f"Bearer {access_token}",
    "Content-Type":"application/json"
}

payload = {
    "from":from_,
    "to":[to_],
    "body":"Storvix SMS center via SinchAPI"
}

try:
    req.post(
    f'https://us.sms.api.sinch.com/xms/v1/{service_plan_id}/batches',
    headers=headers,
    data=json.dumps(payload)
).json()

except req.exceptions.HTTPError as err:
    print("HTTP Error")
    print(err.arg[0])