#!/usr/bin/python
'''
def filter for caltech reasonable person object
'''


# For boxes with certain Label, default is person_class only
def label_filter(box, label="person"):
    return box['lbl'] == label


# For boxes with a specified boundry, the default values arefrom
def boundry_filter(box, bnds={'xmin': 5, 'ymin': 5, 'xmax': 635, 'ymax': 475}):
    x1 = box['pos'][0]
    y1 = box['pos'][1]
    width = box['pos'][2]
    height = box['pos'][3]
    x2 = x1 + width
    y2 = y1 + height

    validity = x1 >= bnds['xmin'] and \
        x2 <= bnds['xmax'] and \
        y1 >= bnds['ymin'] and \
        y2 <= bnds['ymax']

    return validity


# For boxes more visible than a speifcied range
def visibility_filter(box, visible_range={'min': 0.65, 'max': float('inf')}):

    occluded = box['occl']

    # A dirty condition to deal with the ill-formatted data.
    if occluded == 0 or \
       not hasattr(box['posv'], '__iter__') or \
       all([v == 0 for v in box['posv']]):

        visiable_ratio = 1

    else:
        width = box['pos'][2]
        height = box['pos'][3]
        area = width * height

        visible_width = box['posv'][2]
        visible_height = box['posv'][3]
        visible_area = visible_width * visible_height

        visiable_ratio = visible_area / area

    validity = visiable_ratio >= visible_range['min'] and \
        visiable_ratio <= visible_range['max']

    return validity


# For boxes higher than a speifcied height
def height_filter(box, height_range={'min': 50, 'max': float('inf')}):

    height = box['pos'][3]
    validity = height >= height_range['min'] and \
        height < height_range['max']
    return validity


# For reasonable subset
def caltech_reasonable_filter(box):

    validity = label_filter(box) and\
        boundry_filter(box) and\
        height_filter(box) and \
        visibility_filter(box)

    return validity


def eth_reasonable_filter(box):

    def verity_bnds(pos):
        bnds = [5, 5, 635, 475]
        return pos[0] >= bnds[0] and pos[0] + pos[2] <= bnds[2] and pos[1] >= bnds[1] and pos[1] + pos[3] <= bnds[3]

    height_min = 50
    visiable_min = .65
    pos = box['pos']
    pos_v = box['posv']
    occl = box['occl']

    pos_area = pos[2] * pos[3]

    if occl == 0 or not hasattr(pos_v, '__iter__') or all(x == 0 for x in pos_v):
        visiable_ratio = 1
    else:
        pos_v_area = pos_v[2] * pos_v[3]
        visiable_ratio = (pos_v_area / pos_area)

    return label_filter(box, 'person') and\
        visiable_ratio > visiable_min and\
        pos[3] > height_min and\
        verity_bnds(pos)
