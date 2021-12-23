import serial

import csv
import os 

import argparse

def parse_ins():
  parser = argparse.ArgumentParser(description="Image sender for oled")
  parser.add_argument('oled',help='Oled file for display')
  parser.add_argument('--port',help='Serial por to use',default='/dev/ttyUSB0')
  parser.add_argument('--baud',help='Baud Rate',type=int,default=115200)
  parser.add_argument('--parity', help='Stream parity',default='none')
  return parser.parse_args()

def setup_serial(ser_args):
  try:
    ser = serial.Serial(ser_args.port,ser_args.baud,parity='N')
  except serial.SerialException as e:
    print(e)
    ser.close()
  return ser  

def send_data(data,port):
  print("Payload: {}".format(data))
  if port.is_open:
    port.write(data)
    port.write(b'v')
  else:
    print("Error: Port closed")
  return      

def send_img(img,port):
  print("Payload length: {}".format(len(img)))
  if port.is_open:
    port.write(img)
  else:
    print("Error: Port closed")
  return      

def load_image(oled):
  payload = b''
  with open(oled,'r') as oled_file:
    reader = csv.reader(oled_file)
    for row in reader:
      ints = [ int(i) for i in row]
      #print(bytes(ints))
      payload += bytes(ints)
  return  payload

if  __name__=="__main__":
  args = parse_ins()
  ser = setup_serial(args)
  byte_arr = b'\x0a\x0a\x0a\x0a\x0a\x0a' * 64
  payload = load_image(args.oled)
  #send_data(payload,ser)
  send_img(payload,ser)

  ser.close()

