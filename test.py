import h5py
with h5py.File("keras_model.h5", "r") as f:
    print(f.attrs['keras_version'])
    print(f.attrs['backend'])

import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"  # Disable GPU

import tensorflow as tf
print(tf.__version__)
# sort update commit 