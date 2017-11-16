#! /bin/bash

DIR=$1

if [ ! -d ${DIR}/data-ETH ]; then
    mkdir ${DIR}/data-ETH
fi
cd ${DIR}/data-ETH

wget http://www.vision.caltech.edu.s3-us-west-2.amazonaws.com/Image_Datasets/CaltechPedestrians/datasets/ETH/annotations.zip
wget http://www.vision.caltech.edu.s3-us-west-2.amazonaws.com/Image_Datasets/CaltechPedestrians/datasets/ETH/set00.tar
wget http://www.vision.caltech.edu.s3-us-west-2.amazonaws.com/Image_Datasets/CaltechPedestrians/datasets/ETH/set01.tar
wget http://www.vision.caltech.edu.s3-us-west-2.amazonaws.com/Image_Datasets/CaltechPedestrians/datasets/ETH/set02.tar

unzip annotations.zip 

tar xvf set00.tar


tar xvf set01.tar


tar xvf set02.tar

