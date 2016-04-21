#!/bin/bash

symlist=`cat symlist`

for sym in $symlist;
do
	echo $sym;
	node convert-tools.js latex2e-OT1-_${sym};
done

mv data svgdata

