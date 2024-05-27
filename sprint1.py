# Testování responses
import json

import requests

api_key_name = 'X-API-KEY'
api_key = 'xxAGdpu3nTQUnI5EP7NFfQ'
endpoint = 'https://service.sysnet.cz/taxonomy/1.0.1'
headers = {'Accept': 'application/json', api_key_name: api_key}

def test_info():
    reply = requests.get(f"{endpoint}/info")
    if reply.status_code != 200:
        return None
    data_json = reply.text
    data_dict = json.loads(data_json)
    return data_dict


def test_taxon_list(search='luňák'):
    reply = requests.get(f"{endpoint}/taxon?key={search}", headers=headers)
    if reply.status_code != 200:
        return None
    data_json = reply.text
    data_dict = json.loads(data_json)
    return data_dict


def test_taxon(identifier='EAP7BAWA1T01'):
    reply = requests.get(f"{endpoint}/taxon/{identifier}", headers=headers)
    if reply.status_code != 200:
        return None
    data_json = reply.text
    data_dict = json.loads(data_json)
    return data_dict
