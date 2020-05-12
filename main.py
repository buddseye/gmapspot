# -*- coding: utf-8 -*-

import sys
import csv
import os
import googlemaps
import json
import gzip

MAPS_JAVASCRIPT_API = os.getenv("MAPS_JAVASCRIPT_API")


class GoogleMaps:
    def __init__(self, key):
        self.gmaps = googlemaps.Client(key=key)

    def get_nearby_place(self, lat, lon):
        if MAPS_JAVASCRIPT_API is None:
            print("Please set env: MAPS_JAVASCRIPT_API")
            return
        RADIUS = 100
        LANGUAGE = "ja"

        return self.gmaps.places_nearby(
            location=(lat, lon), radius=RADIUS, language=LANGUAGE)


def convert(row):
    gmaps = GoogleMaps(MAPS_JAVASCRIPT_API)
    res = gmaps.get_nearby_place(row["lat"], row["lon"])
    return json.dumps(res, ensure_ascii=False)


def main():
    reader = csv.DictReader(sys.stdin, delimiter="\t")
    i = 0
    for r in reader:
        with gzip.open(f'./output/{i:03}.json.gz', mode='wt') as writer:
            output = convert(r)
            writer.write(output)
        i += 1


if __name__ == "__main__":
    main()
