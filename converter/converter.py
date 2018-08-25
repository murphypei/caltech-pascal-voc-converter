#!/usr/bin/python
# -*- coding: utf-8 -*-

# Usage: /path/to/voc/convert_voc.py /path/to/annotations.json /path/to/images  /path/to/dst_dir reasonable

import os
import sys

from .parse_annotations_json import parse
from .create_image_sets import create_image_sets
from .create_jpeg_images import create_jpeg_images
from .create_annotations import create_annotations
from .config import caltech_reasonable_config, inria_config, eth_reasonable_config

import argparse


def create_voc(annos_json_path, src_img_path, dst_path, dataset_config):
    voc_dir = os.path.join(dst_path, 'VOC2007')
    if not os.path.exists(voc_dir):
        os.makedirs(voc_dir)
    train_annos, test_annos = parse(annos_json_path, dataset_config)
    train_annos, test_annos = create_jpeg_images(train_annos, test_annos,
                                                 src_img_path, voc_dir)
    create_image_sets(train_annos, test_annos, voc_dir)
    create_annotations(train_annos, test_annos, voc_dir,
                       dataset_config["annotation_config"])


def parse_args():
    """
    Parse input arguments 
    """
    parser = argparse.ArgumentParser(
        description='Convert a dataset to vocdevkit format')
    parser.add_argument(
        '--images',
        dest='src_img_path',
        help='source images dir path',
        default=None,
        type=str)
    parser.add_argument(
        '--anno',
        dest='annos_json_path',
        help='annotations json file path',
        default=None,
        type=str)
    parser.add_argument(
        '--dst',
        dest='dst_path',
        help='save voc dataset path',
        default=None,
        type=str)
    parser.add_argument(
        '--dataset',
        dest='dataset',
        help='dataset',
        default=None,
        type=str)
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()
    return args


if __name__ == "__main__":

    args = parse_args()

    print('Called with args:')
    print(args)

    annos_json_path = args.annos_json_path
    if not os.path.exists(annos_json_path):
        print("Can't find annotations json file: {}".format(annos_json_path))
        exit(-1)
    src_img_path = args.src_img_path
    if not os.path.exists(src_img_path):
        print("Can't find images path: {}".format(src_img_path))
        exit(-1)

    dst_path = args.dst_path

    dataset = args.dataset
    if dataset == 'caltech_reasonable':
        dataset_config = caltech_reasonable_config
    elif dataset == 'inria':
        dataset_config = inria_config
    elif dataset == 'eth_reasonable':
        dataset_config = eth_reasonable_config
    else:
        print("unidentify dataset input")
        exit(-1)

    create_voc(annos_json_path, src_img_path, dst_path, dataset_config)
