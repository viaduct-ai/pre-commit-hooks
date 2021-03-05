from __future__ import print_function

import argparse
import io
import sys

import json
from airflow.models import DagBag
from collections import Counter


def main(argv=None):

    try:
        subprocess.Popen(["make pre-commit"], stdout=subprocess.PIPE)
    except AssertionError:
        print(f'Duplicate dag ids: {dupes} found!')
        return 1
    return 0

if __name__ == '__main__':
    sys.exit(main())
