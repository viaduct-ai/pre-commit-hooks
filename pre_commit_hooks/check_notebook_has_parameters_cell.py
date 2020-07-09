from __future__ import print_function

import argparse
import io
import sys

import json


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-m',
        '--multi',
        '--allow-multiple-documents',
        action='store_true',
    )

    parser.add_argument('filenames', nargs='*', help='Filenames to check.')
    args = parser.parse_args(argv)

    retval = 0
    for filename in args.filenames:

        with io.open(filename) as f:
            try:
                data = json.load(f)

                parameters_cell_exists = False

                for cell in data['cells']:
                    if 'parameters' in cell['metadata']['tags']:
                        parameters_cell_exists = True

                if not parameters_cell_exists:
                    retval = 1
            except:
                continue

    return retval


if __name__ == '__main__':
    sys.exit(main())