#! -*- coding:utf-8 -*-

'''
create JPEGImages dir: copy and rename images and train_annos and test_annos
'''

import os
from PIL import Image
from parse_annotations_json import parse


# NOTED: This function will modify train_annos and test_annos
def create_jpeg_images(train_annos, test_annos, src_img_path, voc_path):

    name_length = 6

    if not os.path.exists(src_img_path):
        print("source images dir path doesn't exist.")
        exit(-1)

    jpeg_dir = os.path.join(voc_path, 'JPEGImages')
    if not os.path.exists(jpeg_dir):
        os.makedirs(jpeg_dir)

    name_number = 1
    last_img_name = ''
    # annos must be sorted
    for i in xrange(len(train_annos)):  
        anno = train_annos[i]      
        current_img_name = anno.split(' ')[0]
        pos = anno.split(' ')[1:]

        if last_img_name == '':
            last_img_name = current_img_name
        elif last_img_name != '' and last_img_name != current_img_name:
            name_number += 1
            last_img_name = current_img_name
        else:
            pass
        
        # save new image as jpeg
        dst_img_name = (name_length - len(str(name_number))) * '0' + str(name_number) + ".jpg"
        if not os.path.exists(os.path.join(jpeg_dir, dst_img_name)):
            image = Image.open(os.path.join(src_img_path, current_img_name))
            image.save(os.path.join(jpeg_dir, dst_img_name), 'jpeg')
            print("save {} done.".format(dst_img_name))
        train_annos[i] = dst_img_name + ' ' + ' '.join(pos)

    for i in xrange(len(test_annos)):  
        anno = test_annos[i]      
        current_img_name = anno.split(' ')[0]
        pos = anno.split(' ')[1:]

        if last_img_name == '':
            last_img_name = current_img_name
        elif last_img_name != '' and last_img_name != current_img_name:
            name_number += 1
            last_img_name = current_img_name
        else:
            pass

        # save new image as jpeg
        dst_img_name = (name_length - len(str(name_number))) * '0' + str(name_number) + ".jpg"
        if not os.path.exists(os.path.join(jpeg_dir, dst_img_name)):
            image = Image.open(os.path.join(src_img_path, current_img_name))
            image.save(os.path.join(jpeg_dir, dst_img_name), 'jpeg')
            print("save {} done.".format(dst_img_name))
        test_annos[i] = dst_img_name + ' ' + ' '.join(pos)

    return (train_annos, test_annos)


if __name__ == "__main__":

    # set train and test set
    train_set = ("set00")
    test_set = ("set01")

    train_annos, test_annos = parse("./annotations.json", train_set, test_set)

    print(train_annos)
    print(test_annos)

    create_jpeg_images(train_annos, test_annos, '', '')
    print train_annos
    print test_annos
