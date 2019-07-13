#!/bin/bash
mkdir -p 201{0..7}/{01..12}
for i in 201{0..7}
do
  for j in {01..12}
  do
    for k in 0{1..3}.txt
    do
      echo "file is ${k}" > $i/$j/$k
    done
  done
done
