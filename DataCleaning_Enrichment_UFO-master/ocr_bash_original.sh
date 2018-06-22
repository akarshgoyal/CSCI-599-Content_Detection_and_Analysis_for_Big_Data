#!/bin/bash

export FILENAME=$1

filename_no_path=$(basename "$FILENAME")
extension="${filename_no_path##*.}"
filename_no_extension="${filename_no_path%.*}convert_original"
echo "Processing $FILENAME: extension $extension: filename no extension: $filename_no_extension"

mkdir -p "$filename_no_extension"
mkdir -p "$filename_no_extension"
mkdir -p "$filename_no_extension"/tiff
mkdir -p "$filename_no_extension"/outtxt
pdfseparate "$FILENAME" "$filename_no_extension"/%d.pdf


for f in $( ls $filename_no_extension ); do

the_file=$(basename $f)
the_file_ex="${the_file##*.}"
the_file_noext="${the_file%.*}"

#magick  -density 300 $filename_no_extension/$the_file  -depth 8 $filename_no_extension/tiff/$the_file_noext.tif
convert -density 300 $filename_no_extension/$the_file -depth 8 -strip -background white -alpha off $filename_no_extension/tiff/$the_file_noext.tif
# convert -density 580 "$filename_no_extension"/$the_file -depth 8 -strip -background white -alpha off "$filename_no_extension"/tiff/$the_file_noext.tif
#convert -density 580 -despeckle -enhance $filename_no_extension/$the_file  -alpha remove -edge 1 -compose darken -depth 32 $filename_no_extension/tiff/$the_file_noext.tif
tesseract "$filename_no_extension"/tiff/$the_file_noext.tif "$filename_no_extension"/outtxt/$the_file_noext
rm "$filename_no_extension"/tiff/$the_file_noext.tif
done
