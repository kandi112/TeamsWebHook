import requests
import json
from getpass import getpass
from pprint import pprint

TOKEN = getpass('Paste your token: ')

BASEURL = "https://webexapis.com"
room = "/v1/rooms"

body = {
    'title': 'Kandi Room'
}

bodyJSON = json.dumps(body)

headers = {
    'Authorization': 'Bearer MWVlYzczMzQtYjM0Yi00YTVjLTk5NjUtN2MyOWI0M2Q4MzQ3ZjMzOWRhODgtYzZi_PF84_7fe15fed-c67b-4ddc-b29c-39338b4d309e',
    'Content-Type': 'application/json'
}

createRoom = BASEURL + room

response = requests.post(createRoom, headers=headers, data=bodyJSON)

responseJSON = response.json()

pprint(responseJSON)
