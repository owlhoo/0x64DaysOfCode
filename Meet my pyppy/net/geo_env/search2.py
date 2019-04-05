#!/usr/bin/env python3

import http.client
import json
from urllib.parse import quote_plus

base = '/maps/api/geocode/json'
# API KEY NEEDED.


def geocode(address):
    path = f'{base}?address={quote_plus(address)}&sensor=false'
    connection = http.client.HTTPConnection('maps.google.com')
    connection.request('GET', path)
    rawreply = connection.getresponse().read()
    reply = json.loads(rawreply.decode('utf-8'))
    print(reply['results'][0]['geometry']['location'])


if __name__ == "__main__":
    geocode('207 N. Defiance St, Archbold, OH')
