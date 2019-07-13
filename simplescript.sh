#!/bin/bash
sed -i '/^$/d' ~/Desktop/text.txt
sed -i 's/.*/\U&/g' ~/Desktop/text.txt
