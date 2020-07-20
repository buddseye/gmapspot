# -*- coding: utf-8 -*-

import sys
import csv
from copy import deepcopy
from argparse import ArgumentParser
from util.data import read_csv_to_dict, match_import_data


def get_args(args=None):
    '''
    >>> args = get_args(['importfile'])
    >>> args.import_file
    'importfile'
    '''
    parser = ArgumentParser()
    parser.add_argument("import_file")
    return parser.parse_args(args)


def product_list(base, target):
    '''
    >>> product_list(['a', 'b'], ['b', 'c'])
    ['a', 'b', 'c']
    '''
    outlist = deepcopy(base)
    for t in target:
        if t not in base:
            outlist.append(t)
    return outlist


def merge_dict(base, target):
    '''
    >>> merge_dict({'a': 1, 'b': 2}, {'b': 3, 'd': 4})
    {'a': 1, 'b': 3, 'd': 4}
    >>> merge_dict({'a': 1, 'b': 2}, {'id': 3, 'index': 4, 'e': 5})
    {'a': 1, 'b': 2, 'e': 5}
    >>> merge_dict({'a': 1, 'id': 2}, {'': 4, 'e': 5})
    {'a': 1, 'id': 2, 'e': 5}
    '''
    merge_data = deepcopy(base)
    for k, v in target.items():
        if k in ('id', 'index', ''):
            continue
        merge_data[k] = v
    return merge_data


def main():
    args = get_args()
    import_dict = read_csv_to_dict(args.import_file)
    reader = csv.DictReader(sys.stdin, delimiter="\t")
    import_first_row = next(iter(import_dict.values()))
    output_fieldnames = product_list(reader.fieldnames,
                                     import_first_row.keys())
    writer = csv.DictWriter(sys.stdout,
                            fieldnames=output_fieldnames,
                            delimiter='\t')
    writer.writeheader()
    for r in reader:
        target_data = match_import_data(import_dict, r["id"])
        outdict = merge_dict(r, target_data)
        writer.writerow(outdict)


if __name__ == "__main__":
    main()
