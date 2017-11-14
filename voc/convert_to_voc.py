#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
from parse_annotations_json import parse
from create_image_sets import create_image_sets
from create_jpeg_images import create_jpeg_images
from create_annotations import create_annotations
from dataset_sets import train_set, test_set


def create_voc(annos_json_path, src_img_path, dst_path):
    voc_dir = os.path.join(dst_path, 'VOC2007')
    if not os.path.exists(voc_dir):
        os.makedirs(voc_dir)
    train_annos, test_annos = parse(annos_json_path, train_set, test_set)
    train_annos, test_annos = create_jpeg_images(train_annos, test_annos, src_img_path, voc_dir)
    create_image_sets(train_annos, test_annos, voc_dir)
    create_annotations(train_annos, test_annos, voc_dir)


if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("invalid argv input, must have 4 args")
        exit(-1)
    annos_json_path = sys.argv[1]
    src_img_path = sys.argv[2]
    voc_path = sys.argv[3]
    
    create_voc(annos_json_path, src_img_path, dst_path)

    
    

