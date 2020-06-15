# -*- coding: utf-8 -*-

import sys
import csv
import os
import googlemaps
import json
import time
from copy import deepcopy


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

    def get_places(self, query, lat=None, lon=None, radius=None):
        if MAPS_JAVASCRIPT_API is None:
            print("Please set env: MAPS_JAVASCRIPT_API")
            return
        LANGUAGE = "ja"
        return self.gmaps.places(
            query=query,
            language=LANGUAGE,
            location=None if lat is None or lon is None else (lat, lon),
            radius=radius
        )


def add_near_spot(gmaps, row):
    output = deepcopy(row)
    res = gmaps.get_nearby_place(row["lat"], row["lon"])
    output["spot"] = json.dumps(res, ensure_ascii=False)
    return output


def add_search_spot(gmaps, row):
    output = deepcopy(row)
    res = gmaps.get_places(row["title"], row["lat"], row["lon"], 50000)
    output["search_spot"] = json.dumps(res, ensure_ascii=False)
    return output


def main():
    reader = csv.DictReader(sys.stdin, delimiter="\t")
    output_fieldnames = list(deepcopy(reader.fieldnames))
    output_fieldnames.append("search_spot")
    writer = csv.DictWriter(sys.stdout,
                            delimiter="\t",
                            fieldnames=output_fieldnames,
                            quoting=csv.QUOTE_NONE,
                            quotechar="")
    writer.writeheader()
    gmaps = GoogleMaps(MAPS_JAVASCRIPT_API)
    i = 0
    for r in reader:
        # writer.writerow(add_search_spot(gmaps, add_near_spot(gmaps, r)))
        writer.writerow(add_search_spot(gmaps, r))
        i += 1
        time.sleep(30)


if __name__ == "__main__":
    main()
