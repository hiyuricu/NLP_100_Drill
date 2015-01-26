#!/bin/bash

for i in corpus/*
do
        a=`basename ${i}.cabocha`
		cabocha -f1 $i > dir61/$a
done

