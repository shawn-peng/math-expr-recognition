#!/bin/bash

list=`ls data/latex2e-OT1-_infty/*.svg`

for file in $list;
do
	echo $file;
	convert $file ${file/svg/png};
	#echo $file ${file/svg/png};
done
