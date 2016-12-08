#!/usr/bin/env python3

import logging
import sys
from argparse import ArgumentParser
from time import sleep

import usb.core
import usb.util

usbVendorId = 0x046d
usbProductId = 0xc333

# initialize logger
log_format = '[%(levelname)s] %(message)s'
logging.basicConfig(format=log_format, level=logging.ERROR)
logger = logging.getLogger()

from includes.keyboard import *

dev = None
intf = None


def attach_device():
    global dev, intf
    dev = usb.core.find(idVendor=usbVendorId, idProduct=usbProductId)
    if dev is None:
        logger.error("Device not found")
        sys.exit()

    intf = 1
    if dev.is_kernel_driver_active(intf) is True:
        logger.debug("Kernel driver active")
        dev.detach_kernel_driver(intf)
        usb.util.claim_interface(dev, intf)

    logger.debug("Attached to device %s:%s", usbVendorId, usbProductId)


def detach_device():
    global dev, intf
    if intf is not None:
        usb.util.release_interface(dev, intf)
        dev.attach_kernel_driver(intf)
        dev = None
        intf = None


def commit():
    data = list()
    data.append(0x11)
    data.append(0xff)
    data.append(0x0c)
    data.append(0x5a)
    for i in range(1, 17):
        data.append(0x00)
    send_data(data)


def convert_data_string(data):
    logger.debug("convert string: %s", data)
    return [int(''.join([data[i], data[i + 1]]), base=16) for i in range(0, len(data), 2)]


def send_data(data):
    global dev
    data_queue = list()

    # create a list of converted data
    data_type = type(data)
    if data_type == str:
        data_queue.append(convert_data_string(data))

    if data_type == list:
        if type(data[0]) == int and data[0] <= 255:
            data_queue.append(data)
        else:
            for item in data:
                item_type = type(item)
                if item_type == list:
                    data_queue.append(item)
                elif item_type == str:
                    data_queue.append(convert_data_string(item))
                else:
                    logger.error("Wrong data type: %s", item_type)
                    sys.exit()

    if logger.level >= logging.INFO:
        logger.info("Queue Data")
        logger.info(data_queue)

    for item in data_queue:
        item_len = len(item)
        if item_len == 20:
            w_value = 0x0211
        elif item_len == 64:
            w_value = 0x0212
        else:
            logger.error(item)
            sys.exit("Error: unknown data length %s" % item_len)

        try:
            logger.debug("sending item: %s", item)
            dev.ctrl_transfer(0x21, 0x09, w_value, 1, item)
        except:
            print('Error sending data', file=sys.stderr)

        # just let keyboard breath
        sleep(.001)


def set_all_brightness(level):
    keys = list(map(int, Key))
    data = get_key_data(keys, level)
    for key, items in data.items():
        send_data(items)
        commit()


def set_group_brightness(group, level):
    data = get_key_group_data(group, level)
    for key, items in data.items():
        send_data(items)
        commit()


def test(data):
    send_data(data)
    commit()


def main():
    parser = ArgumentParser(description="Control Logitech G610 keyboard functions")
    parser.add_argument("-v", "--verbose",
                        help="set verbose output", action="store_true", default=False)
    parser.add_argument("-a", "--all",
                        action="store_true", default=False,
                        help="sets brightness of all keys, logos, etc. (default)")
    parser.add_argument("-g", "--group",
                        help="sets brightness of key group"
                             " (logo, multimedia, fkeys, modifiers, arrows, numeric, gaming)",
                        dest="group",
                        metavar="<group>")
    parser.add_argument("--debug", action="store_true", default=False,
                        help="enable debug mode",
                        dest="debug")
    parser.add_argument("value", type=str, default="",
                        help="brightness level (off, l1-9, max) or manual value (000000 to ffffff)",
                        metavar="<value>")

    args = parser.parse_args()

    if args.verbose is True:
        logger.setLevel(logging.INFO)
    elif args.debug is True:
        logger.setLevel(logging.DEBUG)

    attach_device()

    if args.all is not False:
        set_all_brightness(args.value)
    elif args.group is not None:
        set_group_brightness(args.group, args.value)
    else:
        set_all_brightness(args.value)

    # app shutdown
    detach_device()


if __name__ == "__main__":
    main()
