# -*- coding: utf-8 -*-

import sys
import csv
import json


def main():
    reader = csv.DictReader(sys.stdin)
    fout = sys.stdout
    json_list = []
    for row in reader:
        json_list.append(row)
    json.load(fout, json_list)


if __name__ == "__main__":
    main()
