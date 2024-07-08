#!/bin/bash

# Check if the user provided the number of copies and the prefix as arguments
if [ -z "$1" ] || [ -z "$2" ]; then
  echo "Usage: $0 <number_of_copies> <prefix_number>"
  exit 1
fi

# The prefix number to add to each filename
prefix=$1

# The number of copies to create
n=$2

# The source file to duplicate (located in the parent directory)
template_file="template.py"

# Check if the template file exists
if [ ! -f "$template_file" ]; then
  echo "Error: $template_file not found!"
  exit 1
fi

# Function to generate the nth alphabetical name
generate_filename() {
  num=$1
  filename=""
  while [ $num -ge 0 ]; do
    char=$(printf "\\$(printf %o $((num % 26 + 97)))")
    filename="${char}${filename}"
    num=$((num / 26 - 1))
  done
  echo "${prefix}${filename}.py"
}

# Create n copies of the template file
for ((i = 0; i < n; i++)); do
  new_file=$(generate_filename $i)
  cp "$template_file" "$new_file"
  echo "Created $new_file"
done
