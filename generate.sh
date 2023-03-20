#!/usr/bin/env bash

set -e
{
	cat <<-'EOF'
# individuals having contributed content to the repositery
EOF
echo
git log --format='%aN <%aE>' | LC_ALL=C.UTF-8 sort -uf
} > AUTHORS
