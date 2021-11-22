from __future__ import print_function

import argparse
import io
import sys
import pytest


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*", help="Filenames to check.")
    args = parser.parse_args(argv)

    return pytest.main(
        [
            # Avoid printing nbsmoke warnings.
            # Most seem irrelevant for PySpark notebooks.
            "-Wignore",
            # Ignore undefined 'spark' for PySpark notebooks.
            "-o",
            "nbsmoke_flakes_to_ignore=undefined name 'spark'",
            # Perform nbsmoke lint check.
            "--nbsmoke-lint",
        ]
        + args.filenames
    )


if __name__ == "__main__":
    sys.exit(main())
