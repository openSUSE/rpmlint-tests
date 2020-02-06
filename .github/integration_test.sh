#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
set -x

cd "$GITHUB_WORKSPACE/.."
# If someone does changes to -tests and -checks at the same time, we want to test them together.
# So try cloning a branch with the same name of the same owner. If that fails, just clone current master.
git clone --depth 1 -b "${GITHUB_REF##*/}" "https://github.com/${GITHUB_REPOSITORY//-tests/-checks}.git" ||
    git clone --depth 1 -b master "https://github.com/openSUSE/rpmlint-checks.git"

for f in rpmlint-checks/*.py ; do
    # 'install' checks from git
    mv "$f" /opt/testing/share/rpmlint/

    # force-enable all checks, to test them even before they're added to rpmlint-Factory
    basename="${f##*/}"
    without_ext="${basename%.*}"
    echo "addCheck('$without_ext')" >> /opt/testing/share/rpmlint/config
done
# dunno why this is required, but tests fail without this
echo "addFilter(' position-independent-executable-suggested ')" >> /opt/testing/share/rpmlint/config

cd "$GITHUB_WORKSPACE"
./run
