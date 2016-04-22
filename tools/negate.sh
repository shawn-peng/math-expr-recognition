#!/bin/bash

clist='A B C D E F G H I J K L M N P Q R S T U V W X Y Z'
clist+=' a b c d e f g h i j k l m n p q r s t u v w x y z'

for dir in $clist;
do
	echo $dir
	for file in $dir/*;
	do
		echo $file
		convert -negate $file $file
	done
done

