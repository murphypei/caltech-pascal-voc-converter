#! /bin/bash

DIR=$1

if [ ! -d ${DIR}/data-INRIA ]; then
    mkdir -p ${DIR}/data-INRIA
fi
cd d${DIR}/data-INRIA

wget http://www.vision.caltech.edu.s3-us-west-2.amazonaws.com/Image_Datasets/CaltechPedestrians/datasets/INRIA/annotations.zip
wget http://www.vision.caltech.edu.s3-us-west-2.amazonaws.com/Image_Datasets/CaltechPedestrians/datasets/INRIA/set00.tar
wget http://www.vision.caltech.edu.s3-us-west-2.amazonaws.com/Image_Datasets/CaltechPedestrians/datasets/INRIA/set01.tar


unzip annotations.zip 

tar xvf set00.tar

tar xvf set01.tar

cd ..