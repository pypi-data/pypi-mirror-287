#!/bin/bash
# -*- indent-tabs-mode: nil; tab-width: 2; sh-indentation: 2; -*-

# Tests full bootstrap with packages that have extras.

set -x
set -e
set -o pipefail

SCRIPTDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
OUTDIR="$(dirname "$SCRIPTDIR")/e2e-output"

rm -rf "$OUTDIR"
mkdir "$OUTDIR"

tox -e e2e -n -r
source .tox/e2e/bin/activate

fromager \
  --log-file="$OUTDIR/test.log" \
  --sdists-repo="$OUTDIR/sdists-repo" \
  --wheels-repo="$OUTDIR/wheels-repo" \
  --work-dir="$OUTDIR/work-dir" \
  bootstrap -r "${SCRIPTDIR}/bootstrap_extras.txt"

find "$OUTDIR/wheels-repo/" -name '*.whl'
find "$OUTDIR/sdists-repo/" -name '*.tar.gz'
ls "$OUTDIR"/work-dir/*/build.log || true

UNEXPECTED_FILES="
$OUTDIR/wheels-repo/downloads/stevedore-*.whl
$OUTDIR/sdists-repo/downloads/stevedore-*.tar.gz
$OUTDIR/sdists-repo/builds/stevedore-*.tar.gz
$OUTDIR/work-dir/stevedore-*/build.log
"

pass=true

for pattern in $UNEXPECTED_FILES; do
  if [ -f "${pattern}" ]; then
    echo "Found unexpected file $pattern" 1>&2
    pass=false
  fi
done

EXPECTED_FILES="
$OUTDIR/wheels-repo/downloads/setuptools-*.whl
$OUTDIR/sdists-repo/downloads/setuptools-*.tar.gz
$OUTDIR/sdists-repo/builds/setuptools-*.tar.gz
$OUTDIR/work-dir/setuptools-*/build.log

$OUTDIR/wheels-repo/downloads/PySocks-*.whl
$OUTDIR/sdists-repo/downloads/PySocks-*.tar.gz
$OUTDIR/sdists-repo/builds/PySocks-*.tar.gz
$OUTDIR/work-dir/PySocks-*/build.log
"

for pattern in $EXPECTED_FILES; do
  if [ ! -f "${pattern}" ]; then
    echo "Did not find file $pattern" 1>&2
    pass=false
  fi
done

# Verify that the constraints file matches the build order file.
jq -r '.[] | .dist + "==" + .version' "$OUTDIR/work-dir/build-order.json" > "$OUTDIR/build-order-constraints.txt"
cat "$OUTDIR/work-dir/constraints.txt" | sed 's/  #.*//g' > "$OUTDIR/constraints-without-comments.txt"
sort -o "$OUTDIR/constraints-without-comments.txt" "$OUTDIR/constraints-without-comments.txt"
sort -o "$OUTDIR/build-order-constraints.txt" "$OUTDIR/build-order-constraints.txt"
if ! diff "$OUTDIR/constraints-without-comments.txt" "$OUTDIR/build-order-constraints.txt";
then
  echo "FAIL: constraints do not match build order"
  pass=false
fi

$pass
