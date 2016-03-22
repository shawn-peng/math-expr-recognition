#!/bin/bash

if [ -z "$1" ]; then
	echo $0 PATH;
	exit
fi

PICDIR=${1}

dirlist=`ls $PICDIR`
echo $dirlist

for dir in $dirlist;
do
	((index++));
	piclist=`find ${PICDIR}/$dir -name '*.png'`;
	for pic in $piclist;
	do
		echo $pic $index;
	done
done > piclist

