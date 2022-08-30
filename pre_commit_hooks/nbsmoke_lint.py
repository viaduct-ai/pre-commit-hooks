from __future__ import print_function

import argparse
import io
import os
import shutil
import sys
import tempfile
import pytest


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*", help="Filenames to check.")
    args = parser.parse_args(argv)

    # Copy all notebooks to a temporary directory for the lint check.
    # Without copying, pytest will try to import the notebook folders as python modules
    # which is unnecessary and may fail if we don't have the required dependencies.
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_filenames = []
        for nb_path in args.filenames:
            os.makedirs(os.path.join(tmp_dir, os.path.dirname(nb_path)), exist_ok=True)
            tmp_nb_path = os.path.join(tmp_dir, nb_path)
            shutil.copyfile(nb_path, tmp_nb_path)
            tmp_filenames.append(tmp_nb_path)
        return pytest.main(
            [
                # Avoid printing nbsmoke warnings.
                # Most seem irrelevant for PySpark notebooks.
                "-Wignore",
                # Ignore undefined 'spark' for PySpark notebooks.
                "-o",
                "nbsmoke_flakes_to_ignore=undefined name '(sc|spark)'",
                # Perform nbsmoke lint check.
                "--nbsmoke-lint",
            ]
            + tmp_filenames
        )


if __name__ == "__main__":
    sys.exit(main())
