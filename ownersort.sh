#!/bin/env bash
find . -user "$USER"|while read -r i
do
  cp "$i" /home/"$USER"/"$i"
done

