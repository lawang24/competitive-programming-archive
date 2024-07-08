#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <new_file_name> <std_file_name>"
    exit 1
fi

# Assign arguments to variables
new_file="${1}.py"
std_file_name=$2

# Define the source file
template_file="template.py"

# Check if the template file exists
if [[ ! -f "$template_file" ]]; then
  echo "Template file $template_file does not exist."
  exit 1
fi

# Check if the new file already exists
if [[ -f "$new_file" ]]; then
  echo "File $new_file already exists. Aborting to prevent overwrite."
  exit 1
fi

# USACO has specific naming conventions for grading

# Rename all *.in input files
for file in *.in; do
    if [[ -f "$file" ]]; then
        mv "$file" "$std_file_name.in"
    fi
done

# Rename all *.out output files
for file in *.out; do
    if [[ -f "$file" ]]; then
        mv "$file" "$std_file_name.out"
    fi
done

# Copy the template file to the new file
cp "$template_file" "$new_file"

# Replace all instances of "name" with the provided file_name
sed -i "" "s/name/$std_file_name/g" "$new_file"

echo "File has been copied to $new_file and edited."
