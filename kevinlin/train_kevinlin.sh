#!/bin/bash

CURDIR=`pwd`

while [[ $# > 1 ]]
do
	key="$1"

	case $key in
		-s|--snapshot)
			SNAP="$2"
			shift # past argument
			;;
		-m|--model)
			MODEL="$2"
			shift # past argument
			;;
		*)
			# unknown option
			echo error augument
			exit
			;;
	esac
	shift # past argument or value
done

if [ -z "$MODEL" ]; then
	MODEL=${CURDIR}/KevinNet_CIFAR10_48.caffemodel
else
	MODEL=`realpath $MODEL`
fi

if [ ! -z "$SNAP" ]; then
	SNAP=`realpath $SNAP`
	SNAPOPT="--snapshot=${SNAP}"
fi

echo Using model file $MODEL


pushd ../../../caffe > /dev/null

./build/tools/caffe train --solver=${CURDIR}/solver.prototxt --weights=$MODEL ${SNAPOPT}
#echo optirun ./build/tools/caffe train --solver=${CURDIR}/lenet_solver.prototxt --model=$MODEL ${SNAPOPT}

popd
