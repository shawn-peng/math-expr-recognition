#!/bin/bash

sym=$1
#list=`ls data/latex2e-OT1-_infty/*.svg`
pattern="*.svg"

for dir in svgdata/*;
do
	mkdir ${dir/svgdata/data} -p
done

list=`find svgdata -name "*.svg"`
#echo $list


for file in $list;
do
	pngfile=${file/svgdata/data}
	pngfile=${pngfile/\.svg/.png}
	echo "$file => $pngfile";
	convert -type Grayscale -negate $file $pngfile
	#echo $file ${file/svg/png};
done
