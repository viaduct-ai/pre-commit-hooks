from __future__ import print_function

import argparse
import io
import sys

import yaml


ENC_SUFFIX =  ".enc.yaml"

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

                kind = data.get("kind", None)

                # Only check encrypted secrets
                if kind != 'Secret' or 'sops' not in data:
                    continue

                if not filename.endswith(ENC_SUFFIX):
                    print(f"SOPS encrypted secrets should end with {ENC_SUFFIX}: {filename}")
                    retval = 1
            except:
                continue

    return retval


if __name__ == '__main__':
    sys.exit(main())
