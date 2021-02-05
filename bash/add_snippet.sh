#!/bin/bash

OUTFILE=/some/path/schnipsel.md

if [ $# -eq 0 ]; then
  input=""
  while read line; do
    input="$input $line"
  done
else
  input="$@"
fi

# pipe to xargs first to trim leading and trailing whitespace
trimmed_input="$(echo $input | xargs | tr -d '\n')"
# trimmed_input="$(echo $input | sed -e 's/^[[:space:]]+//' -e 's/[[:space:]]+$//')"
echo "- \`$trimmed_input\`" >> $OUTFILE
