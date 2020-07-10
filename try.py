import calendar
import os
import requests

fish = "tuna"
url = "https://acnhapi.com/v1/fish/" + fish.lower().strip().replace(" ", "_")

data = requests.get(url).json()

name = data["name"]["name-USen"].title()
museum_phrase = data["museum-phrase"]

availability_northern = []
for month in data["availability"]["month-array-northern"]:
    month_name = calendar.month_abbr[month]
    availability_northern.append(month_name)

availability_southern = []
for month in data["availability"]["month-array-southern"]:
    month_name = calendar.month_abbr[month]
    availability_southern.append(month_name)

if data["availability"]["isAllYear"] == True:
    availability_northern = "All Year"
    availability_southern = "All Year"
else:
    availability_northern = availability_northern[0] + " - " + availability_northern[-1]
    availability_southern = availability_southern[0] + " - " + availability_southern[-1]

time_of_day = ""
if data["availability"]["isAllDay"] == True:
    time_of_day = "All Day"
else:
    time_of_day = data["availability"]["time"]