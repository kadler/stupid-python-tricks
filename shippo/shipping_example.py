#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import shippo
from os import environ

shippo.api_key = environ['APIKEY']

address_from = {
  "street1": "233 S Wacker Dr",
  "city": "Chicago",
  "state": "IL",
  "zip": "60606",
  "country": "US"
}

address_to = {
  "street1": "1302 McKinley Park Rd",
  "city": "Soudan",
  "state": "MN",
  "zip": "55782",
  "country": "US"
}

parcel = {
    "length": "5",
    "width": "5",
    "height": "5",
    "distance_unit": "in",

    "weight": "2",
    "mass_unit": "lb",
}

shipment = shippo.Shipment.create(
    address_from=address_from,
    address_to=address_to,
    parcels=[parcel],
    async=False
)

for rate in shipment.rates:
    print(f'{rate["provider"]} {rate["servicelevel"]["name"]}: ${rate["amount"]}')
