#!/bin/bash
find -user $USER|while read i
do
  cp $i /home/$USER/$i
done
