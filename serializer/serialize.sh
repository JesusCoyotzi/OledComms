#!/bin/bash

for bin_img in ./images/results/*64.png
do
  echo "Serializing $bin_img"
  python3 serializer.py --height 64 "$bin_img"
done
