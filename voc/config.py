# -*- coding: utf-8 -*-

'''
configuration for different dataset
'''

from filter import caltech_reasonable_filter, eth_reasonable_filter

# for all object
caltech_config = {
    # caltech dataset
    "train_set": set(["set00", "set01", "set02", "set03", "set04", "set05"]),
    "test_set": set(["set06", "set07", "set08", "set09", "set10"]),

    "version": "reasonable",     # default
    "reasonable_filter": caltech_reasonable_filter,    # reasonable filter

    "fps_interval": 10,

    # set VOC xml annotations config
    "annotation_config": {
        "folder_node": 'VOC2007',
        "root_node": 'annotation',
        "dataset": 'Caltech',
        "class": 'pedestrian',
        "annotation": 'PASCAL VOC2007',
        "author": 'Rocco',
        "segmented": '0',
        "difficult": '0',
        "truncated": '0',
        "pose": 'Unspecified',
        "channel": 3
    }
}


# inria dataset
inria_config = {
    "train_set": set(["set00"]),
    "test_set": set(["set01"]),

    "version": "all",
    "reasonable_filter": None,

    "fps_interval": 0,

    "annotation_config": {
        "folder_node": 'VOC2007',
        "root_node": 'annotation',
        "dataset": 'INRIA',
        "class": 'pedestrian',
        "annotation": 'PASCAL VOC2007',
        "author": 'Rocco',
        "segmented": '0',
        "difficult": '0',
        "truncated": '0',
        "pose": 'Unspecified',
        "channel": 3
    }
}


# for all object
eth_config = {
    # caltech dataset
    "train_set": set(["set00", "set01"]),
    "test_set": set(["set02"]),

    "version": "reasonable",     # default
    "reasonable_filter": eth_reasonable_filter,

    "fps_interval": 0,

    # set VOC xml annotations config
    "annotation_config": {
        "folder_node": 'VOC2007',
        "root_node": 'annotation',
        "dataset": 'ETH',
        "class": 'pedestrian',
        "annotation": 'PASCAL VOC2007',
        "author": 'Rocco',
        "segmented": '0',
        "difficult": '0',
        "truncated": '0',
        "pose": 'Unspecified',
        "channel": 3
    }
}

