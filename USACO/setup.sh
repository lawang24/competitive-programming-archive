#!/bin/bash

# Check if at least one argument is provided
if [ "$#" -lt 1 ]; then
    echo "Usage: $0 <new_file_name> [<std_file_name>]"
    exit 1
fi

# Assign arguments to variables
new_file="${1}.py"
std_file_name=${2:-}

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

# Copy the template file to the new file
cp "$template_file" "$new_file"

# USACO has specific naming conventions for grading
# If the second argument exists:
#    rename *.in and *.out files
#    reconfigure std.in/out 
if [ -n "$std_file_name" ]; then
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

    # Replace all instances of "name" with the provided file_name
    sed -i "" "2i\\
sys.stdin = open('${std_file_name}.in', 'r')\\
sys.stdout = open('${std_file_name}.out', 'w')\\
" "$new_file"

fi


echo "File has been copied to $new_file and edited."
