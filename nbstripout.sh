#!/bin/sh
#
# strip output of IPython Notebooks
# add this as `.git/hooks/pre-commit`
# to run every time you commit a notebook
#
# requires `nbstripout` to be available on your PATH
#

if git rev-parse --verify HEAD >/dev/null 2>&1; then
   against=HEAD
else
   # Initial commit: diff against an empty tree object
   against=4b825dc642cb6eb9a060e54bf8d69288fbee4904
fi

# Find notebooks to be committed
(
IFS='
'
NBS=`git diff-index --cached $against --name-only --diff-filter=A | grep '.ipynb' | uniq`

for NB in $NBS ; do
    echo "Removing outputs from $NB"
    nbstripout "$NB"
    git add "$NB"
done
)

exec git diff-index --check --cached $against --
