# -*- coding: utf-8 -*-

import csv
from copy import deepcopy


def read_csv_to_dict(filename):
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
