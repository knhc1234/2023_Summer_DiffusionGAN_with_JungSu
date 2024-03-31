from PIL import Image
import os
import h5py

dir_path = "./train/train_000.h5"

with h5py.File(dir_path, 'r') as f:
    images = f['ct'][:]

print(images.shape)