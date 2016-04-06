#!/bin/bash

if [ -z "$1" ];
then
	echo "Usage: $0 <dir>"
	exit
fi


for img in `find $1 -name "*.png"`;
do
	echo $img
	convert -negate $img $img
done
