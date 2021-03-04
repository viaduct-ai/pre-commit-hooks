from __future__ import print_function

import argparse
import io
import sys

import json
from airflow.models import DagBag
from collections import Counter


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-m',
        '--multi',
        '--allow-multiple-documents',
        action='store_true',
    )

    args = parser.parse_args(argv)

    dupes = find_duplicate_dags()
    if dupes:
        print(f'Duplicate dag ids: {dupes} found!')
        return 1
    return 0

def find_duplicate_dags():
    dagbag = DagBag()
    # dagbag stats are the only dagbag collection that haven't deduped
    dag_stats = [stat.dags.strip('][').strip('"').split(', ')  for stat in dagbag.dagbag_stats]
    counts = Counter([dag_id for stat in dag_stats for dag_id in stat])
    return [dag_id for dag_id, count in counts if count > 1]

if __name__ == '__main__':
    sys.exit(main())
