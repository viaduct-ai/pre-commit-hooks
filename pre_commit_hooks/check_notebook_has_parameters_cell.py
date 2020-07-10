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

    for filename in args.filenames:

        with io.open(filename) as f:
            try:
                data = json.load(f)

                parameters_cell_exists = False

                for cell in data['cells']:
                    metadata = cell['metadata']

                    if 'tags' not in metadata:
                        continue

                    if 'parameters' in metadata['tags']:
                        parameters_cell_exists = True

                if not parameters_cell_exists:
                    print(f'File {filename} does not have a parameters cell')
                    return 1
            except Exception as e:
                print(f'Exception of file {filename}: {e}')
                continue

    return 0


if __name__ == '__main__':
    sys.exit(main())
