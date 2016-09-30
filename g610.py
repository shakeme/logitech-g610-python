#!/usr/bin/env python2

import sys
import os.path
import imp
import time
import usb.core
import usb.util
from time import sleep

dev = None
intf = None
data = []

g610_brightness = [
  "000000",
  "424242",
  "818181",
  "c0c0c0",
  "ffffff"
]

g610_backlitmode_static       = "11ff0d3b0001#brightness#0200000000000000000000"
g610_backlitmode_logo_static  = "11ff0d3b0101#brightness#0200000000000000000000"

def help():
  print '  Usage :'
  print '    g610.py backlit {level 0-4}'
  print '    g610.py --test {data_frame}'
  print '    g610.py --help'
  print ''

def main():
  global data

  if len(sys.argv) == 3:
    if sys.argv[1] == "backlit":
      level = int(sys.argv[2])
      data.append(g610_backlitmode_static.replace("#brightness#", g610_brightness[level]))
      data.append(g610_backlitmode_logo_static.replace("#brightness#", g610_brightness[level]))

    elif sys.argv[1] == "--test":
      data.append(sys.argv[2])
      print "test mode: "
      print data

    attachKeyboard()
    updateKeyboard()
    detachKeyboard()

  else:
    help()
    sys.exit()

def attachKeyboard():
  global dev
  global intf
  dev = usb.core.find(idVendor=0x046d, idProduct=0xc333)
  if dev is None:
    print 'Device not found, exiting...'
    sys.exit()
  intf = 1
  if dev.is_kernel_driver_active(intf) is True:
    dev.detach_kernel_driver(intf)
    usb.util.claim_interface(dev, intf)


def detachKeyboard():
  global dev
  global intf
  if intf is not None:
    usb.util.release_interface(dev, intf)
    dev.attach_kernel_driver(intf)
    dev = None
    intf = None


def updateKeyboard():
  global dev
  global data
  try:
    for item in data:
      encoded_data = [ int(''.join([item[i], item[i+1]]), base=16) for i in range(0, len(item), 2)]
      dev.ctrl_transfer(0x21,0x09,0x0211,1,encoded_data)
      sleep(.01)

  except:
    print 'Error updating keyboard'


if len(sys.argv) > 1:
  if sys.argv[1] == '--help':
    help()
    sys.exit()

if __name__ == "__main__":
  main()
