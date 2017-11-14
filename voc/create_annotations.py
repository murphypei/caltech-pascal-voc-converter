#! -*- coding:utf-8 -*-

'''
create Annotations dir: create annotations xml file
'''

import os
import xml.dom
import xml.dom.minidom
from PIL import Image
from config import annotation_config


_FOLDER_NODE = annotation_config["folder_node"]
_ROOT_NODE = annotation_config["root_node"]
_DATABASE_NAME = annotation_config["dataset"]
_CLASS = annotation_config["class"]
_ANNOTATION = annotation_config["annotation"]
_AUTHOR = annotation_config["author"]

_SEGMENTED = annotation_config["segmented"]
_DIFFICULT = annotation_config["difficult"]
_TRUNCATED = annotation_config["truncated"]
_POSE = annotation_config["pose"]

_IMAGE_CHANNEL = annotation_config["channel"]


# create node
def createElementNode(doc, tag, attr):
    # create a element node
    element_node = doc.createElement(tag)

    # create a text node
    text_node = doc.createTextNode(attr)

    # text node as a child node of element
    element_node.appendChild(text_node)

    return element_node


# create a child node
def createChildNode(doc, tag, attr, parent_node):

    child_node = createElementNode(doc, tag, attr)
    parent_node.appendChild(child_node)


# create object node
def createObjectNode(doc, attrs):
    object_node = doc.createElement('object')
    createChildNode(doc, 'name', attrs['classification'], object_node)
    createChildNode(doc, 'pose', _POSE, object_node)
    createChildNode(doc, 'truncated', _TRUNCATED, object_node)
    createChildNode(doc, 'difficult', _DIFFICULT, object_node)

    bndbox_node = doc.createElement('bndbox')
    createChildNode(doc, 'xmin', attrs['xmin'], bndbox_node)
    createChildNode(doc, 'ymin', attrs['ymin'], bndbox_node)
    createChildNode(doc, 'xmax', attrs['xmax'], bndbox_node)
    createChildNode(doc, 'ymax', attrs['ymax'], bndbox_node)
    object_node.appendChild(bndbox_node)

    return object_node


# write documentElement to xml file
def writeXMLFile(doc, filename):

    tmpfile = open('tmp.xml', 'w')
    doc.writexml(tmpfile, addindent=' '*4, newl='\n', encoding='utf-8')
    tmpfile.close()

    # delete first line(because of writexml function auto add tag)
    fin = open('tmp.xml')
    fout = open(filename, 'w')
    lines = fin.readlines()

    for line in lines[1:]:
        if line.split():
            fout.writelines(line)

    fin.close()
    fout.close()


# create xml file and write node info
def createXMLFile(attrs, width, height, filename):

    # create doc object
    my_dom = xml.dom.getDOMImplementation()
    doc = my_dom.createDocument(None, _ROOT_NODE, None)

    # get root node
    root_node = doc.documentElement

    # create folder node
    createChildNode(doc, 'folder', _FOLDER_NODE, root_node)

    # create filename node
    createChildNode(doc, 'filename', attrs['name'], root_node)

    # create source node and it's childnode
    source_node = doc.createElement('source')
    createChildNode(doc, 'database', _DATABASE_NAME, source_node)
    createChildNode(doc, 'annotation', _ANNOTATION, source_node)
    createChildNode(doc, 'image', 'flickr', source_node)
    createChildNode(doc, 'flickrid', 'NULL', source_node)
    root_node.appendChild(source_node)

    # create owner node and it's childnode
    owner_node = doc.createElement('owner')
    createChildNode(doc, 'flickrid', 'NULL', owner_node)
    createChildNode(doc, 'name', _AUTHOR, owner_node)
    root_node.appendChild(owner_node)

    # create size node and it's childnode
    size_node = doc.createElement('size')
    createChildNode(doc, 'width', str(width), size_node)
    createChildNode(doc, 'height', str(height), size_node)
    createChildNode(doc, 'depth', str(_IMAGE_CHANNEL), size_node)
    root_node.appendChild(size_node)

    # create segmented node
    createChildNode(doc, 'segmented', _SEGMENTED, root_node)

    # create object node
    object_node = createObjectNode(doc, attrs)
    root_node.appendChild(object_node)

    writeXMLFile(doc, filename)


def create_annotations(train_annos, test_annos, voc_path):

    anno_dir = os.path.join(voc_path, 'Annotations')
    if not os.path.exists(anno_dir):
        os.makedirs(anno_dir)

    train_test_annos = train_annos + test_annos
    attrs = dict()
    for anno in train_test_annos:
        attrs.clear()
        array = anno.split(' ')
        attrs['name'] = array[0]
        attrs['xmin'] = array[1].split('.')[0]  # abandon float
        attrs['ymin'] = array[2].split('.')[0]
        attrs['xmax'] = array[3].split('.')[0]
        attrs['ymax'] = array[4].split('.')[0]
        attrs['classification'] = _CLASS

        # build xml file name
        xml_file_name = os.path.join(anno_dir, (attrs['name'].split('.'))[0] + '.xml')
        print ("process xml file: {}".format(xml_file_name))

        # write to xml file
        if os.path.exists(xml_file_name):
            existed_doc = xml.dom.minidom.parse(xml_file_name)
            root_node = existed_doc.documentElement

            object_node = createObjectNode(existed_doc, attrs)
            root_node.appendChild(object_node)

            writeXMLFile(existed_doc, xml_file_name)

        else:
            img_name = attrs['name']
            img_path = os.path.join(voc_path, "JPEGImages", img_name)

            img = Image.open(img_path)
            width, height = img.size
            # img.close()
            createXMLFile(attrs, width, height, xml_file_name)
