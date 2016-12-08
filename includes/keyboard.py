from includes.keys import *
from g610 import logger
from g610 import convert_data_string

import math

brightness_levels = {
    "off": "000000",
    "l1": "030303",
    "l2": "101010",
    "l3": "222222",
    "l4": "424242",
    "l5": "818181",
    "l6": "c0c0c0",
    "max": "ffffff"
}


def get_key_values(keys):
    ret = []
    for key in keys:
        ret.append(key_values[key])
    return ret


def get_group_keys(key_group):
    if key_group not in key_groups:
        logger.error("key group not found: %s", key_group)
        return ()

    keys = key_groups[key_group]

    # convert single item into tuple
    if type(keys) != tuple:
        keys = (keys,)

    logger.debug("keys in get_group_keys: %s", keys)

    return keys


def get_brightness_value(brightness):
    if len(brightness) == 6:
        # override brightness level on direct value
        level = brightness
    elif brightness in brightness_levels:
        level = brightness_levels[brightness]
    else:
        level = brightness_levels["l1"]

    ret = convert_data_string(level)
    return ret


def process_key_data(data):
    data_processed = {}
    for key, items in data.items():
        if key not in data_processed:
            data_processed[key] = []

        if key == AddressGroup.LOGO:
            for item in items:
                data_items = address_group_prefix[key][:]
                data_items += item
                for i in range(0, 8):
                    data_items.append(0x00)
                data_processed[key].append(data_items)
        else:
            address_prefix_count = len(address_group_prefix[key])
            items_count = len(items)
            data_size = 64
            batch_size = int(data_size / 4) - int(address_prefix_count / 4)
            batch_data_size = 12
            batch_count = math.ceil(items_count / batch_data_size)

            items_index = 0
            for i in range(0, batch_count):
                data_items = address_group_prefix[key][:]

                for j in range(0, batch_size):
                    if j < batch_data_size and items_index < items_count:
                        for item in items[items_index]:
                            data_items.append(item)
                        items_index += 1
                    else:
                        for k in range(0, 4):
                            data_items.append(0x00)

                data_processed[key].append(data_items)

    return data_processed


def get_key_data(keys, brightness):
    data = {}

    if type(keys) != list:
        keys = [keys]

    brightness_value = get_brightness_value(brightness)
    key_data = get_key_values(keys)

    for item in key_data:
        address_group = item["address_group"]

        if address_group not in data:
            data[address_group] = []

        key_data_merged = [item["address"]]
        for value in brightness_value:
            key_data_merged.append(value)

        data[address_group].append(key_data_merged)

    data_final = process_key_data(data)

    return data_final


def get_key_group_data(key_group, brightness):
    groups = key_group.split(",")

    keys = []

    for group in groups:
        group_keys = get_group_keys(group)
        for key in group_keys:
            keys.append(key)

    return get_key_data(keys, brightness)
