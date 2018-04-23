#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
input caltech video dataset path, convert annotations and videos to images.
"""

import sys
import os
from convert_annotations import convert_annotations
from convert_seqs import convert_seqs

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Error, {} args input, pls input dataset path only !".format(len(sys.argv)))
        exit(-1)
    elif len(sys.argv) == 2:
        path = sys.argv[1]
        if not os.path.exists(path):
            print("input path not find.")
            exit(-1)
    print("input dataset path: " + path)

    convert_seqs(path)
    convert_annotations(path)