import requests
import json
from getpass import getpass
from pprint import pprint

TOKEN = getpass('Paste your token: ')

BASEURL = "https://webexapis.com"
room = "/v1/rooms"

body = {}


headers = {
    'Authorization': 'Bearer MWVlYzczMzQtYjM0Yi00YTVjLTk5NjUtN2MyOWI0M2Q4MzQ3ZjMzOWRhODgtYzZi_PF84_7fe15fed-c67b-4ddc-b29c-39338b4d309e',
    'Accept': 'application/json'
}

getRooms= BASEURL + room

response = requests.get(getRooms, headers=headers, data=body)

responseJSON = response.json()

pprint(responseJSON)
