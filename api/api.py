import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("TOMORROW_API_KEY")

url = "https://api.tomorrow.io/v4/timelines"

headers = {
    "accept": "application/json",
    "Accept-Encoding": "gzip",
    "content-type": "application/json",
    "apikey": api_key
}

payload = {
    "location": "38.581573, -121.494400",
    "fields": ["treeBirchIndex", "treeAshIndex", "treeOakIndex", "treeIndex"],
    "units": "metric",
    "timesteps": ["1d"],
    "startTime": "now",
    "endTime": "nowPlus5d",
    "timezone": "auto"
}


class PollenAPI:
    def __init__(self):
        self.payload = payload

    def call_api(self, location, pollen_list):
        self.payload["location"] = location
        self.payload["fields"] = pollen_list
        data = requests.post(url, json=self.payload, headers=headers).json()
        pollen_data = data["data"]["timelines"][0]["intervals"]
        reformatted_pollen_data = {day["startTime"].split("T")[0]: [value for key, value in day["values"].items()] for
                                   day in pollen_data}
        return reformatted_pollen_data

# pollen_api = PollenAPI()
# my_data = pollen_api.call_api(location="38.581573, -121.494400",
#                               pollen_list=["treeBirchIndex", "treeAshIndex", "treeOakIndex", "treeIndex"])
# print(my_data)
