#!/bin/bash

# create virtualenv
python -m virtualenv .
source ./bin/activate
python -m pip install -r requirements.txt

# import CIFAR-10 data
mkdir -p data
CIFAR=cifar-10-python.tar.gz
DATA=data/
TAR=$DATA$CIFAR
BATCHES=cifar-10-batches-py
UNTAR_DIR=$DATA$BATCHES
if [ ! -f "$TAR" ]; then
    curl https://www.cs.toronto.edu/\~kriz/$CIFAR > $TAR
    tar -xvf $TAR -C $DATA/
fi
