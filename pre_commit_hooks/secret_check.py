from __future__ import print_function

import argparse
import io
import sys

import yaml


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

        with io.open(filename, encoding='UTF-8') as f:
            try:
                data = yaml.safe_load(f)

                if 'kind' in data:
                    if data['kind'] == 'Secret':
                        if 'sops' not in data:
                            print(f'Sops not defined: {filename}')
                            retval = 1
                        elif not filename.endswith('enc.yaml'):
                            print(f"Doesn't end correctly: {filename}")
                            retval = 1
            except:
                continue

    return retval


if __name__ == '__main__':
    sys.exit(main())
