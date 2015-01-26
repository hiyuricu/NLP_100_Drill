#!/bin/bash

sort -grk 2 dir63/tf_idf.txt | cut -f1 -d" " | grep -v "\d" | head -n 100 > dir64/tf_idf_top100.txt