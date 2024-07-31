#!/bin/bash

mv leetcode_rerun "$1"
mv leetcode_rerun.deps.yaml "$1".deps.yaml

# change project name in all files
find . \( -type d -name .git -prune \) -o \( -type f -not -name 'tasks.json' -not -name 'update_from_template.sh'  \) -print0 | xargs -0 sed -i "s/leetcode_rerun/$1/g"

# author name
if [ -n "$2" ]; then
    find . \( -type d -name .git -prune \) -o \( -type f -not -name 'tasks.json' -not -name 'update_from_template.sh'  \) -print0 | xargs -0 sed -i "s/Austin Gregg-Smith/$2/g"
fi

# author email
if [ -n "$3" ]; then
    find . \( -type d -name .git -prune \) -o \( -type f -not -name 'tasks.json' -not -name 'update_from_template.sh'  \) -print0 | xargs -0 sed -i "s/blooop@gmail.com/$3/g"
fi

# github username
if [ -n "$3" ]; then
    find . \( -type d -name .git -prune \) -o \( -type f -not -name 'setup_host.sh' -not -name 'update_from_template.sh'  \) -print0 | xargs -0 sed -i "s/blooop/$4/g"
fi
