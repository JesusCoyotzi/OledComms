#!/bin/bash

OLED_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

for oled_img in $OLED_DIR/serial_imgs/*oled
do
  printf 'Sending %s\n' "$oled_img"
  python3 "$OLED_DIR/send_img.py" "$oled_img"
  sleep 3
done
