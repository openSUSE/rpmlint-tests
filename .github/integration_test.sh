#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
#set -x

cyan() {
    printf "\e[36m\e[1m%s\e[m\x0f\n" "$@"
}

echo


cd "$GITHUB_WORKSPACE/.."
# If someone does changes to -tests and -checks at the same time, we want to test them together.
# So try cloning a branch with the same name of the same owner. If that fails, just clone current master.
git clone -q --depth 1 -b "${GITHUB_REF##*/}" "https://github.com/${GITHUB_REPOSITORY//-tests/-checks}.git" ||
    git clone -q --depth 1 -b master "https://github.com/openSUSE/rpmlint-checks.git"

branch_info=$(git -C rpmlint-checks branch -r -v | cut -d/ -f 2-)
branch_name=$(echo "$branch_info" | cut '-d ' -f 1)
branch_commit_id=$(echo "$branch_info" | cut '-d ' -f 2)
branch_commit_msg=$(echo "$branch_info" | cut '-d ' -f 3-)
remote=$(git -C rpmlint-checks remote get-url origin)
echo "testing against rpmlint-checks branch $branch_name from $remote / commit $branch_commit_id: '$branch_commit_msg'"


for f in rpmlint-checks/*.py ; do
    # 'install' checks from git
    mv "$f" /opt/testing/share/rpmlint/

    # force-enable all checks, to test them even before they're added to rpmlint-Factory
    basename="${f##*/}"
    without_ext="${basename%.*}"
    [[ "$without_ext" != "Whitelisting" ]] &&
        echo "addCheck('$without_ext')" >> /opt/testing/share/rpmlint/config
done

cd "$GITHUB_WORKSPACE"
cyan "Starting testsuite..."

# run the testsuite, overriding the 'diff' command to 'colordiff'
bash -c 'diff() {
    colordiff "$@"
}
source ./run'
