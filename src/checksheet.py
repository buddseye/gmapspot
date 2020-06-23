# -*- coding: utf-8 -*-

import sys
import csv
from copy import deepcopy
from argparse import ArgumentParser

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


def read_file_to_dict(filename):
    if not filename:
        return {}
    with open(filename, "r", encoding="sjis") as ifp:
        reader = csv.DictReader(ifp)
        return {r["id"]: deepcopy(r) for r in reader}


def match_import_data(import_dict, index):
    try:
        return import_dict[index]
    except KeyError:
        return {}


def update_dict(base, value, row_num):
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
    import_dict = read_file_to_dict(args.import_file)
    reader = csv.DictReader(sys.stdin, delimiter="\t")
    writer = csv.DictWriter(sys.stdout, fieldnames=OUTPUT_FIELDNAMES)
    writer.writeheader()
    i = 0
    for r in reader:
        outdict = match_import_data(import_dict, r["id"])
        outdict2 = update_dict(outdict, r, i)
        writer.writerow(outdict2)
        i += 1


if __name__ == "__main__":
    main()
