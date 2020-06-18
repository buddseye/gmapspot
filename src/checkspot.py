# -*- coding: utf-8 -*-

import sys
import csv
import json


def convert(row):
    def get(base, *args):
        value = base
        for i in args:
            try:
                value = value[i]
            except (KeyError, IndexError, TypeError):
                return None
        return value

    spot = json.loads(row["spot"])
    search_spot = json.loads(row["search_spot"])
    original_spots = list(filter(
        lambda x: "political" not in x["types"], spot["results"]))
    s1 = get(original_spots, 0)
    s2 = get(original_spots, 1)
    return {
        "id": row["id"],
        "title": row["title"],
        "thumb_url": row["thumb_url"],
        "lat": row["lat"],
        "lon": row["lon"],
        "spot1_name": get(s1, "name"),
        "spot1_type": str(get(s1, "types")),
        "spot1_address": get(s1, "vicinity"),
        "spot1_lat": get(s1, "geometry", "location", "lat"),
        "spot1_lon": get(s1, "geometry", "location", "lng"),
        "spot1_place_id": get(s1, 'place_id'),
        "spot2_name": get(s2, "name"),
        "spot2_type": str(get(s2, "types")),
        "spot2_address": get(s2, "vicinity"),
        "spot2_lat": get(s2, "geometry", "location", "lat"),
        "spot2_lon": get(s2, "geometry", "location", "lng"),
        "spot2_place_id": get(s2, 'place_id'),
        "spot3_name": get(search_spot, "results", 0, "name"),
        "spot3_type": str(get(search_spot, "results", 0, "types")),
        "spot3_address": get(search_spot, "results", 0, "formatted_address"),
        "spot3_lat": get(search_spot, "results", 0, "geometry", "location", "lat"),
        "spot3_lon": get(search_spot, "results", 0, "geometry", "location", "lng"),
        "spot3_place_id": get(search_spot, 'results', 0, 'place_id'),
    }


def main():
    reader = csv.DictReader(sys.stdin, delimiter="\t")
    spots = []
    for r in reader:
        spots.append(convert(r))
    print(json.dumps(spots, ensure_ascii=False))
    # data = {
    #     "spots": spots
    # }
    # print(template.render(data))

    # writer.writeheader()
    # i = 0
    # for r in reader:
    #     # if i <= 208:
    #     #     i += 1
    #     #     continue
    #     spot = convert(r)
    #     output = dict(deepcopy(r))
    #     output["spot"] = spot
    #     writer.writerow(output)
    #     i += 1
    #     time.sleep(30)


if __name__ == "__main__":
    main()
