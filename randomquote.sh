# This program when executed randomly generates a quote from a quote.txt file.
#You need to have a quote.txt file to execute this
#To execute this, You can only do it in an bash environment
# Execution code :- ./randomquote.sh

#!/bin/bash

i=0

# Read lines into array
while read -r line
do
    arr[$i]="$line"
    let i++
done < quote.txt

# Get random index
RAN=$((RANDOM % i))

# Print random quote
echo "${arr[$RAN]}"
