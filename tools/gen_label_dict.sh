#!/bin/bash

pushd data/222

labels=`ls`

((i=0));

{
	echo \{ 

	for label in $labels; do
		echo \"$label\" \: $i ,
		((i++))
	done

	echo \}

} > ../label_dict.json

popd

