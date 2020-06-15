# -*- coding: utf-8 -*-

import sys
import csv
import codecs

OUTPUT_FIELDNAMES = [
    "index",
    "id",
    "title",
    "number",
]


def main():
    reader = csv.DictReader(sys.stdin, delimiter="\t")
    writer = csv.DictWriter(sys.stdout, fieldnames=OUTPUT_FIELDNAMES)
    writer.writeheader()
    i = 0
    for r in reader:
        writer.writerow({
            "index": str(i),
            "id": r["id"],
            "title": r["title"],
            "number": ""
        })
        i += 1


if __name__ == "__main__":
    main()
