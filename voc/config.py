# -*- coding: utf-8 -*-

'''
config for different dataset
'''

# caltech dataset
# train_set = ("set00", "set01", "set02", "set03", "set04", "set05")
# test_set = ("set06", "set07", "set08", "set09", "set10")

# INRIA dataset
train_set = ("set00")
test_set = ("set01")

# set VOC xml annotations config
annotation_config = {
    "folder_node": 'VOC2007',
    "root_node": 'annotation',
    "dataset": 'INRIA',
    "class": 'person',
    "annotation": 'PASCAL VOC2007',
    "author": 'Rocco',
    "segmented": '0',
    "difficult": '0',
    "truncated": '0',
    "pose": 'Unspecified',
    "channel": 3
}
