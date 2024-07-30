#!/bin/bash

# Configuration base dir has chapters sorted by number
base_dir=$1
base_dir_name=$(basename "$base_dir")
config_json=$2

chapter_files=$(ls "$base_dir"/*.md | sort -V)

# Create a temporary file for intermediate processing
full_book=$(mktemp)

# Concatenate all chapter files and clean the content
for file in $chapter_files; do
    echo "Processing $file"
    cat "$file" >> "$full_book"
done

# Convert the Markdown files to PDF with Pandoc
pandoc "$full_book" -o "$base_dir/$base_dir_name.pdf" \
    --biblatex \
    --slide-level=3 \
    -V geometry:margin=1in \
    -V fontsize=12pt \
    -V linestretch=1.3 \
    --filter=pandoc-crossref

# Cleanup intermediate files
rm -f "$full_book"

# Open the final PDF file
open "$base_dir/$base_dir_name.pdf"