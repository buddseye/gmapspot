# -*- coding: utf-8 -*-

import sys
import csv
from copy import deepcopy
from argparse import ArgumentParser
from util.data import read_csv_to_dict, match_import_data

OUTPUT_FIELDNAMES = [
    "index",
    "id",
    "title",
    "number",
    "release",
    "description",
]


def get_args(args):
    parser = ArgumentParser(args)
    parser.add_argument("-i", "--import-file")
    return parser.parse_args()


def update_dict(value, row_num, base={}):
    outdict = deepcopy(base)
    outdict["index"] = str(row_num)
    outdict["id"] = value["id"]
    outdict["title"] = value["title"]
    outdict["number"] = ""
    outdict["release"] = ""
    outdict["description"] = ""
    return outdict


def main():
    args = get_args(sys.argv)
    import_dict = read_csv_to_dict(args.import_file)
    reader = csv.DictReader(sys.stdin, delimiter="\t")
    writer = csv.DictWriter(sys.stdout, fieldnames=OUTPUT_FIELDNAMES)
    writer.writeheader()
    i = 0
    for r in reader:
        outdict = match_import_data(import_dict, r["id"])
        outdict2 = update_dict(r, i, outdict)
        writer.writerow(outdict2)
        i += 1


if __name__ == "__main__":
    main()
