#! -*- coding:utf-8 -*-

'''
create ImageSets dir: create Main dir, test.txt and trainval.txt
'''

import os


# NOTED: This function will modify train_annos and test_annos
def create_image_sets(train_annos, test_annos, voc_path):

        # make ImageSets dir
    sets_dir = os.path.join(voc_path, 'ImageSets', 'Main')
    if not os.path.exists(sets_dir):
        os.makedirs(sets_dir)

    name_length = 6

    trainval_file = open(os.path.join(sets_dir, 'trainval.txt'), 'w')
    test_file = open(os.path.join(sets_dir, 'test.txt'), 'w')

    trainval_imgs = []
    last_img = ''
    for anno in train_annos:
        current_img_name = anno.split(' ')[0].split('.')[0]
        if len(current_img_name) != name_length:
            print("name format error: {}".format(current_img_name))
            exit(-1)
        if current_img_name != last_img:
            trainval_imgs.append(current_img_name)
            last_img = current_img_name
    trainval_file.write('\n'.join(trainval_imgs))

    test_imgs = []
    for anno in test_annos:
        current_img_name = anno.split(' ')[0].split('.')[0]
        if len(current_img_name) != name_length:
            print("name format error: {}".format(current_img_name))
            exit(-1)
        if current_img_name != last_img:
            test_imgs.append(current_img_name)
            last_img = current_img_name
    test_file.write('\n'.join(test_imgs))

    trainval_file.close()
    test_file.close()
    print("write ImageSets files done.")
