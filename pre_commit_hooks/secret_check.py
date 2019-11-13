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
        try:
            f = io.open(filename, encoding='UTF-8')
            docs = yaml.load_all(f, Loader=yaml.FullLoader)
        except:
            continue

        for doc in docs:
            if 'kind' in doc:
                if doc['kind'] == 'Secret':
                    if 'sops' not in doc:
                        retval = 1
                    elif not filename.endswith('enc.yaml'):
                        retval = 1

    return retval


if __name__ == '__main__':
    sys.exit(main())
