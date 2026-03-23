#=======================================
import numpy as np
import matplotlib.pyplot as plt
import sys
#================

ifn1 = './data-input/asia/m01_su.bin'
ifn2 = './data-input/asia/m01_up.bin'
ofn1 = './data-input/asia/m01_input_surface_from_bin.npy'
ofn2 = './data-input/asia/m01_input_upper_from_bin.npy'
print('ifn1= ', ifn1)
print('ifn2= ', ifn2)
print('ofn1= ', ofn1)
print('ofn2= ', ofn2)
shape = (4, 721, 1440)
with open(ifn1, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
surface = np.flip(data, axis=1) # lat方向翻轉
np.save(ofn1, surface.astype(np.float32))
shape = (5, 13, 721, 1440)
with open(ifn2, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
upper = np.flip(data, axis=2) # lat方向翻轉
np.save(ofn2, upper.astype(np.float32))
ifn1 = './data-input/asia/m02_su.bin'
ifn2 = './data-input/asia/m02_up.bin'
ofn1 = './data-input/asia/m02_input_surface_from_bin.npy'
ofn2 = './data-input/asia/m02_input_upper_from_bin.npy'
print('ifn1= ', ifn1)
print('ifn2= ', ifn2)
print('ofn1= ', ofn1)
print('ofn2= ', ofn2)
shape = (4, 721, 1440)
with open(ifn1, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
surface = np.flip(data, axis=1) # lat方向翻轉
np.save(ofn1, surface.astype(np.float32))
shape = (5, 13, 721, 1440)
with open(ifn2, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
upper = np.flip(data, axis=2) # lat方向翻轉
np.save(ofn2, upper.astype(np.float32))
ifn1 = './data-input/asia/m03_su.bin'
ifn2 = './data-input/asia/m03_up.bin'
ofn1 = './data-input/asia/m03_input_surface_from_bin.npy'
ofn2 = './data-input/asia/m03_input_upper_from_bin.npy'
print('ifn1= ', ifn1)
print('ifn2= ', ifn2)
print('ofn1= ', ofn1)
print('ofn2= ', ofn2)
shape = (4, 721, 1440)
with open(ifn1, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
surface = np.flip(data, axis=1) # lat方向翻轉
np.save(ofn1, surface.astype(np.float32))
shape = (5, 13, 721, 1440)
with open(ifn2, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
upper = np.flip(data, axis=2) # lat方向翻轉
np.save(ofn2, upper.astype(np.float32))
ifn1 = './data-input/asia/m04_su.bin'
ifn2 = './data-input/asia/m04_up.bin'
ofn1 = './data-input/asia/m04_input_surface_from_bin.npy'
ofn2 = './data-input/asia/m04_input_upper_from_bin.npy'
print('ifn1= ', ifn1)
print('ifn2= ', ifn2)
print('ofn1= ', ofn1)
print('ofn2= ', ofn2)
shape = (4, 721, 1440)
with open(ifn1, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
surface = np.flip(data, axis=1) # lat方向翻轉
np.save(ofn1, surface.astype(np.float32))
shape = (5, 13, 721, 1440)
with open(ifn2, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
upper = np.flip(data, axis=2) # lat方向翻轉
np.save(ofn2, upper.astype(np.float32))
ifn1 = './data-input/asia/m05_su.bin'
ifn2 = './data-input/asia/m05_up.bin'
ofn1 = './data-input/asia/m05_input_surface_from_bin.npy'
ofn2 = './data-input/asia/m05_input_upper_from_bin.npy'
print('ifn1= ', ifn1)
print('ifn2= ', ifn2)
print('ofn1= ', ofn1)
print('ofn2= ', ofn2)
shape = (4, 721, 1440)
with open(ifn1, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
surface = np.flip(data, axis=1) # lat方向翻轉
np.save(ofn1, surface.astype(np.float32))
shape = (5, 13, 721, 1440)
with open(ifn2, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
upper = np.flip(data, axis=2) # lat方向翻轉
np.save(ofn2, upper.astype(np.float32))
ifn1 = './data-input/asia/m06_su.bin'
ifn2 = './data-input/asia/m06_up.bin'
ofn1 = './data-input/asia/m06_input_surface_from_bin.npy'
ofn2 = './data-input/asia/m06_input_upper_from_bin.npy'
print('ifn1= ', ifn1)
print('ifn2= ', ifn2)
print('ofn1= ', ofn1)
print('ofn2= ', ofn2)
shape = (4, 721, 1440)
with open(ifn1, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
surface = np.flip(data, axis=1) # lat方向翻轉
np.save(ofn1, surface.astype(np.float32))
shape = (5, 13, 721, 1440)
with open(ifn2, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
upper = np.flip(data, axis=2) # lat方向翻轉
np.save(ofn2, upper.astype(np.float32))
ifn1 = './data-input/asia/m07_su.bin'
ifn2 = './data-input/asia/m07_up.bin'
ofn1 = './data-input/asia/m07_input_surface_from_bin.npy'
ofn2 = './data-input/asia/m07_input_upper_from_bin.npy'
print('ifn1= ', ifn1)
print('ifn2= ', ifn2)
print('ofn1= ', ofn1)
print('ofn2= ', ofn2)
shape = (4, 721, 1440)
with open(ifn1, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
surface = np.flip(data, axis=1) # lat方向翻轉
np.save(ofn1, surface.astype(np.float32))
shape = (5, 13, 721, 1440)
with open(ifn2, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
upper = np.flip(data, axis=2) # lat方向翻轉
np.save(ofn2, upper.astype(np.float32))
ifn1 = './data-input/asia/m08_su.bin'
ifn2 = './data-input/asia/m08_up.bin'
ofn1 = './data-input/asia/m08_input_surface_from_bin.npy'
ofn2 = './data-input/asia/m08_input_upper_from_bin.npy'
print('ifn1= ', ifn1)
print('ifn2= ', ifn2)
print('ofn1= ', ofn1)
print('ofn2= ', ofn2)
shape = (4, 721, 1440)
with open(ifn1, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
surface = np.flip(data, axis=1) # lat方向翻轉
np.save(ofn1, surface.astype(np.float32))
shape = (5, 13, 721, 1440)
with open(ifn2, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
upper = np.flip(data, axis=2) # lat方向翻轉
np.save(ofn2, upper.astype(np.float32))
ifn1 = './data-input/asia/m09_su.bin'
ifn2 = './data-input/asia/m09_up.bin'
ofn1 = './data-input/asia/m09_input_surface_from_bin.npy'
ofn2 = './data-input/asia/m09_input_upper_from_bin.npy'
print('ifn1= ', ifn1)
print('ifn2= ', ifn2)
print('ofn1= ', ofn1)
print('ofn2= ', ofn2)
shape = (4, 721, 1440)
with open(ifn1, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
surface = np.flip(data, axis=1) # lat方向翻轉
np.save(ofn1, surface.astype(np.float32))
shape = (5, 13, 721, 1440)
with open(ifn2, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
upper = np.flip(data, axis=2) # lat方向翻轉
np.save(ofn2, upper.astype(np.float32))
ifn1 = './data-input/asia/m10_su.bin'
ifn2 = './data-input/asia/m10_up.bin'
ofn1 = './data-input/asia/m10_input_surface_from_bin.npy'
ofn2 = './data-input/asia/m10_input_upper_from_bin.npy'
print('ifn1= ', ifn1)
print('ifn2= ', ifn2)
print('ofn1= ', ofn1)
print('ofn2= ', ofn2)
shape = (4, 721, 1440)
with open(ifn1, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
surface = np.flip(data, axis=1) # lat方向翻轉
np.save(ofn1, surface.astype(np.float32))
shape = (5, 13, 721, 1440)
with open(ifn2, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
upper = np.flip(data, axis=2) # lat方向翻轉
np.save(ofn2, upper.astype(np.float32))
ifn1 = './data-input/asia/m11_su.bin'
ifn2 = './data-input/asia/m11_up.bin'
ofn1 = './data-input/asia/m11_input_surface_from_bin.npy'
ofn2 = './data-input/asia/m11_input_upper_from_bin.npy'
print('ifn1= ', ifn1)
print('ifn2= ', ifn2)
print('ofn1= ', ofn1)
print('ofn2= ', ofn2)
shape = (4, 721, 1440)
with open(ifn1, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
surface = np.flip(data, axis=1) # lat方向翻轉
np.save(ofn1, surface.astype(np.float32))
shape = (5, 13, 721, 1440)
with open(ifn2, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
upper = np.flip(data, axis=2) # lat方向翻轉
np.save(ofn2, upper.astype(np.float32))
ifn1 = './data-input/asia/m12_su.bin'
ifn2 = './data-input/asia/m12_up.bin'
ofn1 = './data-input/asia/m12_input_surface_from_bin.npy'
ofn2 = './data-input/asia/m12_input_upper_from_bin.npy'
print('ifn1= ', ifn1)
print('ifn2= ', ifn2)
print('ofn1= ', ofn1)
print('ofn2= ', ofn2)
shape = (4, 721, 1440)
with open(ifn1, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
surface = np.flip(data, axis=1) # lat方向翻轉
np.save(ofn1, surface.astype(np.float32))
shape = (5, 13, 721, 1440)
with open(ifn2, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
upper = np.flip(data, axis=2) # lat方向翻轉
np.save(ofn2, upper.astype(np.float32))
ifn1 = './data-input/asia/m13_su.bin'
ifn2 = './data-input/asia/m13_up.bin'
ofn1 = './data-input/asia/m13_input_surface_from_bin.npy'
ofn2 = './data-input/asia/m13_input_upper_from_bin.npy'
print('ifn1= ', ifn1)
print('ifn2= ', ifn2)
print('ofn1= ', ofn1)
print('ofn2= ', ofn2)
shape = (4, 721, 1440)
with open(ifn1, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
surface = np.flip(data, axis=1) # lat方向翻轉
np.save(ofn1, surface.astype(np.float32))
shape = (5, 13, 721, 1440)
with open(ifn2, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
upper = np.flip(data, axis=2) # lat方向翻轉
np.save(ofn2, upper.astype(np.float32))
ifn1 = './data-input/asia/m14_su.bin'
ifn2 = './data-input/asia/m14_up.bin'
ofn1 = './data-input/asia/m14_input_surface_from_bin.npy'
ofn2 = './data-input/asia/m14_input_upper_from_bin.npy'
print('ifn1= ', ifn1)
print('ifn2= ', ifn2)
print('ofn1= ', ofn1)
print('ofn2= ', ofn2)
shape = (4, 721, 1440)
with open(ifn1, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
surface = np.flip(data, axis=1) # lat方向翻轉
np.save(ofn1, surface.astype(np.float32))
shape = (5, 13, 721, 1440)
with open(ifn2, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
upper = np.flip(data, axis=2) # lat方向翻轉
np.save(ofn2, upper.astype(np.float32))
ifn1 = './data-input/asia/m15_su.bin'
ifn2 = './data-input/asia/m15_up.bin'
ofn1 = './data-input/asia/m15_input_surface_from_bin.npy'
ofn2 = './data-input/asia/m15_input_upper_from_bin.npy'
print('ifn1= ', ifn1)
print('ifn2= ', ifn2)
print('ofn1= ', ofn1)
print('ofn2= ', ofn2)
shape = (4, 721, 1440)
with open(ifn1, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
surface = np.flip(data, axis=1) # lat方向翻轉
np.save(ofn1, surface.astype(np.float32))
shape = (5, 13, 721, 1440)
with open(ifn2, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
upper = np.flip(data, axis=2) # lat方向翻轉
np.save(ofn2, upper.astype(np.float32))
ifn1 = './data-input/asia/m16_su.bin'
ifn2 = './data-input/asia/m16_up.bin'
ofn1 = './data-input/asia/m16_input_surface_from_bin.npy'
ofn2 = './data-input/asia/m16_input_upper_from_bin.npy'
print('ifn1= ', ifn1)
print('ifn2= ', ifn2)
print('ofn1= ', ofn1)
print('ofn2= ', ofn2)
shape = (4, 721, 1440)
with open(ifn1, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
surface = np.flip(data, axis=1) # lat方向翻轉
np.save(ofn1, surface.astype(np.float32))
shape = (5, 13, 721, 1440)
with open(ifn2, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
upper = np.flip(data, axis=2) # lat方向翻轉
np.save(ofn2, upper.astype(np.float32))
ifn1 = './data-input/asia/m17_su.bin'
ifn2 = './data-input/asia/m17_up.bin'
ofn1 = './data-input/asia/m17_input_surface_from_bin.npy'
ofn2 = './data-input/asia/m17_input_upper_from_bin.npy'
print('ifn1= ', ifn1)
print('ifn2= ', ifn2)
print('ofn1= ', ofn1)
print('ofn2= ', ofn2)
shape = (4, 721, 1440)
with open(ifn1, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
surface = np.flip(data, axis=1) # lat方向翻轉
np.save(ofn1, surface.astype(np.float32))
shape = (5, 13, 721, 1440)
with open(ifn2, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
upper = np.flip(data, axis=2) # lat方向翻轉
np.save(ofn2, upper.astype(np.float32))
ifn1 = './data-input/asia/m18_su.bin'
ifn2 = './data-input/asia/m18_up.bin'
ofn1 = './data-input/asia/m18_input_surface_from_bin.npy'
ofn2 = './data-input/asia/m18_input_upper_from_bin.npy'
print('ifn1= ', ifn1)
print('ifn2= ', ifn2)
print('ofn1= ', ofn1)
print('ofn2= ', ofn2)
shape = (4, 721, 1440)
with open(ifn1, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
surface = np.flip(data, axis=1) # lat方向翻轉
np.save(ofn1, surface.astype(np.float32))
shape = (5, 13, 721, 1440)
with open(ifn2, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
upper = np.flip(data, axis=2) # lat方向翻轉
np.save(ofn2, upper.astype(np.float32))
ifn1 = './data-input/asia/m19_su.bin'
ifn2 = './data-input/asia/m19_up.bin'
ofn1 = './data-input/asia/m19_input_surface_from_bin.npy'
ofn2 = './data-input/asia/m19_input_upper_from_bin.npy'
print('ifn1= ', ifn1)
print('ifn2= ', ifn2)
print('ofn1= ', ofn1)
print('ofn2= ', ofn2)
shape = (4, 721, 1440)
with open(ifn1, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
surface = np.flip(data, axis=1) # lat方向翻轉
np.save(ofn1, surface.astype(np.float32))
shape = (5, 13, 721, 1440)
with open(ifn2, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
upper = np.flip(data, axis=2) # lat方向翻轉
np.save(ofn2, upper.astype(np.float32))
ifn1 = './data-input/asia/m20_su.bin'
ifn2 = './data-input/asia/m20_up.bin'
ofn1 = './data-input/asia/m20_input_surface_from_bin.npy'
ofn2 = './data-input/asia/m20_input_upper_from_bin.npy'
print('ifn1= ', ifn1)
print('ifn2= ', ifn2)
print('ofn1= ', ofn1)
print('ofn2= ', ofn2)
shape = (4, 721, 1440)
with open(ifn1, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
surface = np.flip(data, axis=1) # lat方向翻轉
np.save(ofn1, surface.astype(np.float32))
shape = (5, 13, 721, 1440)
with open(ifn2, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
upper = np.flip(data, axis=2) # lat方向翻轉
np.save(ofn2, upper.astype(np.float32))
ifn1 = './data-input/asia/m21_su.bin'
ifn2 = './data-input/asia/m21_up.bin'
ofn1 = './data-input/asia/m21_input_surface_from_bin.npy'
ofn2 = './data-input/asia/m21_input_upper_from_bin.npy'
print('ifn1= ', ifn1)
print('ifn2= ', ifn2)
print('ofn1= ', ofn1)
print('ofn2= ', ofn2)
shape = (4, 721, 1440)
with open(ifn1, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
surface = np.flip(data, axis=1) # lat方向翻轉
np.save(ofn1, surface.astype(np.float32))
shape = (5, 13, 721, 1440)
with open(ifn2, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
upper = np.flip(data, axis=2) # lat方向翻轉
np.save(ofn2, upper.astype(np.float32))
ifn1 = './data-input/asia/m22_su.bin'
ifn2 = './data-input/asia/m22_up.bin'
ofn1 = './data-input/asia/m22_input_surface_from_bin.npy'
ofn2 = './data-input/asia/m22_input_upper_from_bin.npy'
print('ifn1= ', ifn1)
print('ifn2= ', ifn2)
print('ofn1= ', ofn1)
print('ofn2= ', ofn2)
shape = (4, 721, 1440)
with open(ifn1, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
surface = np.flip(data, axis=1) # lat方向翻轉
np.save(ofn1, surface.astype(np.float32))
shape = (5, 13, 721, 1440)
with open(ifn2, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
upper = np.flip(data, axis=2) # lat方向翻轉
np.save(ofn2, upper.astype(np.float32))
ifn1 = './data-input/asia/m23_su.bin'
ifn2 = './data-input/asia/m23_up.bin'
ofn1 = './data-input/asia/m23_input_surface_from_bin.npy'
ofn2 = './data-input/asia/m23_input_upper_from_bin.npy'
print('ifn1= ', ifn1)
print('ifn2= ', ifn2)
print('ofn1= ', ofn1)
print('ofn2= ', ofn2)
shape = (4, 721, 1440)
with open(ifn1, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
surface = np.flip(data, axis=1) # lat方向翻轉
np.save(ofn1, surface.astype(np.float32))
shape = (5, 13, 721, 1440)
with open(ifn2, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
upper = np.flip(data, axis=2) # lat方向翻轉
np.save(ofn2, upper.astype(np.float32))
ifn1 = './data-input/asia/m24_su.bin'
ifn2 = './data-input/asia/m24_up.bin'
ofn1 = './data-input/asia/m24_input_surface_from_bin.npy'
ofn2 = './data-input/asia/m24_input_upper_from_bin.npy'
print('ifn1= ', ifn1)
print('ifn2= ', ifn2)
print('ofn1= ', ofn1)
print('ofn2= ', ofn2)
shape = (4, 721, 1440)
with open(ifn1, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
surface = np.flip(data, axis=1) # lat方向翻轉
np.save(ofn1, surface.astype(np.float32))
shape = (5, 13, 721, 1440)
with open(ifn2, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
upper = np.flip(data, axis=2) # lat方向翻轉
np.save(ofn2, upper.astype(np.float32))
ifn1 = './data-input/asia/m25_su.bin'
ifn2 = './data-input/asia/m25_up.bin'
ofn1 = './data-input/asia/m25_input_surface_from_bin.npy'
ofn2 = './data-input/asia/m25_input_upper_from_bin.npy'
print('ifn1= ', ifn1)
print('ifn2= ', ifn2)
print('ofn1= ', ofn1)
print('ofn2= ', ofn2)
shape = (4, 721, 1440)
with open(ifn1, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
surface = np.flip(data, axis=1) # lat方向翻轉
np.save(ofn1, surface.astype(np.float32))
shape = (5, 13, 721, 1440)
with open(ifn2, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
upper = np.flip(data, axis=2) # lat方向翻轉
np.save(ofn2, upper.astype(np.float32))
ifn1 = './data-input/asia/m26_su.bin'
ifn2 = './data-input/asia/m26_up.bin'
ofn1 = './data-input/asia/m26_input_surface_from_bin.npy'
ofn2 = './data-input/asia/m26_input_upper_from_bin.npy'
print('ifn1= ', ifn1)
print('ifn2= ', ifn2)
print('ofn1= ', ofn1)
print('ofn2= ', ofn2)
shape = (4, 721, 1440)
with open(ifn1, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
surface = np.flip(data, axis=1) # lat方向翻轉
np.save(ofn1, surface.astype(np.float32))
shape = (5, 13, 721, 1440)
with open(ifn2, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
upper = np.flip(data, axis=2) # lat方向翻轉
np.save(ofn2, upper.astype(np.float32))
ifn1 = './data-input/asia/m27_su.bin'
ifn2 = './data-input/asia/m27_up.bin'
ofn1 = './data-input/asia/m27_input_surface_from_bin.npy'
ofn2 = './data-input/asia/m27_input_upper_from_bin.npy'
print('ifn1= ', ifn1)
print('ifn2= ', ifn2)
print('ofn1= ', ofn1)
print('ofn2= ', ofn2)
shape = (4, 721, 1440)
with open(ifn1, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
surface = np.flip(data, axis=1) # lat方向翻轉
np.save(ofn1, surface.astype(np.float32))
shape = (5, 13, 721, 1440)
with open(ifn2, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
upper = np.flip(data, axis=2) # lat方向翻轉
np.save(ofn2, upper.astype(np.float32))
ifn1 = './data-input/asia/m28_su.bin'
ifn2 = './data-input/asia/m28_up.bin'
ofn1 = './data-input/asia/m28_input_surface_from_bin.npy'
ofn2 = './data-input/asia/m28_input_upper_from_bin.npy'
print('ifn1= ', ifn1)
print('ifn2= ', ifn2)
print('ofn1= ', ofn1)
print('ofn2= ', ofn2)
shape = (4, 721, 1440)
with open(ifn1, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
surface = np.flip(data, axis=1) # lat方向翻轉
np.save(ofn1, surface.astype(np.float32))
shape = (5, 13, 721, 1440)
with open(ifn2, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
upper = np.flip(data, axis=2) # lat方向翻轉
np.save(ofn2, upper.astype(np.float32))
ifn1 = './data-input/asia/m29_su.bin'
ifn2 = './data-input/asia/m29_up.bin'
ofn1 = './data-input/asia/m29_input_surface_from_bin.npy'
ofn2 = './data-input/asia/m29_input_upper_from_bin.npy'
print('ifn1= ', ifn1)
print('ifn2= ', ifn2)
print('ofn1= ', ofn1)
print('ofn2= ', ofn2)
shape = (4, 721, 1440)
with open(ifn1, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
surface = np.flip(data, axis=1) # lat方向翻轉
np.save(ofn1, surface.astype(np.float32))
shape = (5, 13, 721, 1440)
with open(ifn2, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
upper = np.flip(data, axis=2) # lat方向翻轉
np.save(ofn2, upper.astype(np.float32))
ifn1 = './data-input/asia/m30_su.bin'
ifn2 = './data-input/asia/m30_up.bin'
ofn1 = './data-input/asia/m30_input_surface_from_bin.npy'
ofn2 = './data-input/asia/m30_input_upper_from_bin.npy'
print('ifn1= ', ifn1)
print('ifn2= ', ifn2)
print('ofn1= ', ofn1)
print('ofn2= ', ofn2)
shape = (4, 721, 1440)
with open(ifn1, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
surface = np.flip(data, axis=1) # lat方向翻轉
np.save(ofn1, surface.astype(np.float32))
shape = (5, 13, 721, 1440)
with open(ifn2, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
upper = np.flip(data, axis=2) # lat方向翻轉
np.save(ofn2, upper.astype(np.float32))
ifn1 = './data-input/asia/m31_su.bin'
ifn2 = './data-input/asia/m31_up.bin'
ofn1 = './data-input/asia/m31_input_surface_from_bin.npy'
ofn2 = './data-input/asia/m31_input_upper_from_bin.npy'
print('ifn1= ', ifn1)
print('ifn2= ', ifn2)
print('ofn1= ', ofn1)
print('ofn2= ', ofn2)
shape = (4, 721, 1440)
with open(ifn1, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
surface = np.flip(data, axis=1) # lat方向翻轉
np.save(ofn1, surface.astype(np.float32))
shape = (5, 13, 721, 1440)
with open(ifn2, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
upper = np.flip(data, axis=2) # lat方向翻轉
np.save(ofn2, upper.astype(np.float32))
ifn1 = './data-input/asia/m32_su.bin'
ifn2 = './data-input/asia/m32_up.bin'
ofn1 = './data-input/asia/m32_input_surface_from_bin.npy'
ofn2 = './data-input/asia/m32_input_upper_from_bin.npy'
print('ifn1= ', ifn1)
print('ifn2= ', ifn2)
print('ofn1= ', ofn1)
print('ofn2= ', ofn2)
shape = (4, 721, 1440)
with open(ifn1, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
surface = np.flip(data, axis=1) # lat方向翻轉
np.save(ofn1, surface.astype(np.float32))
shape = (5, 13, 721, 1440)
with open(ifn2, 'rb') as f:
  data = np.fromfile(f, dtype=np.float32).reshape(shape)
upper = np.flip(data, axis=2) # lat方向翻轉
np.save(ofn2, upper.astype(np.float32))


#================
sys.exit(0)
#=======================================

