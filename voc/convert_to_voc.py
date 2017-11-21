#!/usr/bin/python
# -*- coding: utf-8 -*-

# Usage: /path/to/voc/convert_voc.py /path/to/annotations.json /path/to/images  /path/to/dst_dir reasonable

import os
import sys
from parse_annotations_json import parse
from create_image_sets import create_image_sets
from create_jpeg_images import create_jpeg_images
from create_annotations import create_annotations
from config import caltech_config, inria_config, eth_config


def create_voc(annos_json_path, src_img_path, dst_path, dataset_config):
    voc_dir = os.path.join(dst_path, 'VOC2007')
    if not os.path.exists(voc_dir):
        os.makedirs(voc_dir)
    train_annos, test_annos = parse(annos_json_path, dataset_config)
    train_annos, test_annos = create_jpeg_images(train_annos, test_annos, src_img_path, voc_dir)
    create_image_sets(train_annos, test_annos, voc_dir)
    create_annotations(train_annos, test_annos, voc_dir, dataset_config["annotation_config"])


if __name__ == "__main__":

    if len(sys.argv) != 5:
        print("invalid argv input, must have 5 args.")
        exit(-1)

    annos_json_path = sys.argv[1]
    if not os.path.exists(annos_json_path):
        print("Can't find annotations json file: {}".format(annos_json_path))
        exit(-1)
    src_img_path = sys.argv[2]
    if not os.path.exists(src_img_path):
        print("Can't find images path: {}".format(src_img_path))
        exit(-1)

    dst_path = sys.argv[3]

    dataset = sys.argv[4]
    if dataset == 'all':
        dataset_config = caltech_config
        caltech_config["version"] = "all"
    elif dataset == 'reasonable':
        dataset_config = caltech_config
        caltech_config["version"] = "reasonable"
    elif dataset == 'inria':
        dataset_config = inria_config
    elif dataset == 'eth':
        dataset_config = eth_config
    else:
        print("unidentify dataset input")
        exit(-1)

    create_voc(annos_json_path, src_img_path, dst_path, dataset_config)
