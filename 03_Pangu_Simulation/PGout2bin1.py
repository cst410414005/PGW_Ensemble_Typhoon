import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import sys
import struct
plt.ioff()

#type = 'upper'
#type = 'surface'
type = sys.argv[1]

#T = 0
T = int(sys.argv[2])
S = 6 * T

#================
input_data_dir  = './output_data/'
output_data_dir = './output_data-bin'
ifn = f'{input_data_dir}/m01_output_{type}_{T}.npy'
ofn = f'{output_data_dir}/m01_output_{type}_{S:03d}.bin'
print('ifn= ',ifn)
print('ofn= ',ofn)

#================
if type == 'upper':
  vo = 5
  zo = 13
elif type == 'surface':
  vo = 4
  zo = 1

#================
#
if not os.path.isdir(output_data_dir):
    os.mkdir(output_data_dir)
#讀檔
print('load...')
data = np.load(ifn)
data.shape = data.shape
print('data.shape= ', data.shape)

# 將陣列儲存為二進制檔案, 直接寫出

with open(ofn, 'wb') as f:
  data.tofile(f) 
input_data_dir  = './output_data/'
output_data_dir = './output_data-bin'
ifn = f'{input_data_dir}/m02_output_{type}_{T}.npy'
ofn = f'{output_data_dir}/m02_output_{type}_{S:03d}.bin'
print('ifn= ',ifn)
print('ofn= ',ofn)

#================
if type == 'upper':
  vo = 5
  zo = 13
elif type == 'surface':
  vo = 4
  zo = 1

#================
#
if not os.path.isdir(output_data_dir):
    os.mkdir(output_data_dir)
#讀檔
print('load...')
data = np.load(ifn)
data.shape = data.shape
print('data.shape= ', data.shape)

# 將陣列儲存為二進制檔案, 直接寫出
with open(ofn, 'wb') as f:
  data.tofile(f)
input_data_dir  = './output_data/'
output_data_dir = './output_data-bin'
ifn = f'{input_data_dir}/m03_output_{type}_{T}.npy'
ofn = f'{output_data_dir}/m03_output_{type}_{S:03d}.bin'
print('ifn= ',ifn)
print('ofn= ',ofn)

#================
if type == 'upper':
  vo = 5
  zo = 13
elif type == 'surface':
  vo = 4
  zo = 1

#================
#
if not os.path.isdir(output_data_dir):
    os.mkdir(output_data_dir)
#讀檔
print('load...')
data = np.load(ifn)
data.shape = data.shape
print('data.shape= ', data.shape)

# 將陣列儲存為二進制檔案, 直接寫出
with open(ofn, 'wb') as f:
  data.tofile(f)
input_data_dir  = './output_data/'
output_data_dir = './output_data-bin'
ifn = f'{input_data_dir}/m04_output_{type}_{T}.npy'
ofn = f'{output_data_dir}/m04_output_{type}_{S:03d}.bin'
print('ifn= ',ifn)
print('ofn= ',ofn)

#================
if type == 'upper':
  vo = 5
  zo = 13
elif type == 'surface':
  vo = 4
  zo = 1

#================
#
if not os.path.isdir(output_data_dir):
    os.mkdir(output_data_dir)
#讀檔
print('load...')
data = np.load(ifn)
data.shape = data.shape
print('data.shape= ', data.shape)

# 將陣列儲存為二進制檔案, 直接寫出
with open(ofn, 'wb') as f:
  data.tofile(f)
input_data_dir  = './output_data/'
output_data_dir = './output_data-bin'
ifn = f'{input_data_dir}/m05_output_{type}_{T}.npy'
ofn = f'{output_data_dir}/m05_output_{type}_{S:03d}.bin'
print('ifn= ',ifn)
print('ofn= ',ofn)

#================
if type == 'upper':
  vo = 5
  zo = 13
elif type == 'surface':
  vo = 4
  zo = 1

#================
#
if not os.path.isdir(output_data_dir):
    os.mkdir(output_data_dir)
#讀檔
print('load...')
data = np.load(ifn)
data.shape = data.shape
print('data.shape= ', data.shape)

# 將陣列儲存為二進制檔案, 直接寫出
with open(ofn, 'wb') as f:
  data.tofile(f)
input_data_dir  = './output_data/'
output_data_dir = './output_data-bin'
ifn = f'{input_data_dir}/m06_output_{type}_{T}.npy'
ofn = f'{output_data_dir}/m06_output_{type}_{S:03d}.bin'
print('ifn= ',ifn)
print('ofn= ',ofn)

#================
if type == 'upper':
  vo = 5
  zo = 13
elif type == 'surface':
  vo = 4
  zo = 1

#================
#
if not os.path.isdir(output_data_dir):
    os.mkdir(output_data_dir)
#讀檔
print('load...')
data = np.load(ifn)
data.shape = data.shape
print('data.shape= ', data.shape)

# 將陣列儲存為二進制檔案, 直接寫出
with open(ofn, 'wb') as f:
  data.tofile(f)
input_data_dir  = './output_data/'
output_data_dir = './output_data-bin'
ifn = f'{input_data_dir}/m07_output_{type}_{T}.npy'
ofn = f'{output_data_dir}/m07_output_{type}_{S:03d}.bin'
print('ifn= ',ifn)
print('ofn= ',ofn)

#================
if type == 'upper':
  vo = 5
  zo = 13
elif type == 'surface':
  vo = 4
  zo = 1

#================
#
if not os.path.isdir(output_data_dir):
    os.mkdir(output_data_dir)
#讀檔
print('load...')
data = np.load(ifn)
data.shape = data.shape
print('data.shape= ', data.shape)

# 將陣列儲存為二進制檔案, 直接寫出
with open(ofn, 'wb') as f:
  data.tofile(f)
input_data_dir  = './output_data/'
output_data_dir = './output_data-bin'
ifn = f'{input_data_dir}/m08_output_{type}_{T}.npy'
ofn = f'{output_data_dir}/m08_output_{type}_{S:03d}.bin'
print('ifn= ',ifn)
print('ofn= ',ofn)

#================
if type == 'upper':
  vo = 5
  zo = 13
elif type == 'surface':
  vo = 4
  zo = 1

#================
#
if not os.path.isdir(output_data_dir):
    os.mkdir(output_data_dir)
#讀檔
print('load...')
data = np.load(ifn)
data.shape = data.shape
print('data.shape= ', data.shape)

# 將陣列儲存為二進制檔案, 直接寫出
with open(ofn, 'wb') as f:
  data.tofile(f)
input_data_dir  = './output_data/'
output_data_dir = './output_data-bin'
ifn = f'{input_data_dir}/m09_output_{type}_{T}.npy'
ofn = f'{output_data_dir}/m09_output_{type}_{S:03d}.bin'
print('ifn= ',ifn)
print('ofn= ',ofn)

#================
if type == 'upper':
  vo = 5
  zo = 13
elif type == 'surface':
  vo = 4
  zo = 1

#================
#
if not os.path.isdir(output_data_dir):
    os.mkdir(output_data_dir)
#讀檔
print('load...')
data = np.load(ifn)
data.shape = data.shape
print('data.shape= ', data.shape)

# 將陣列儲存為二進制檔案, 直接寫出
with open(ofn, 'wb') as f:
  data.tofile(f)
input_data_dir  = './output_data/'
output_data_dir = './output_data-bin'
ifn = f'{input_data_dir}/m10_output_{type}_{T}.npy'
ofn = f'{output_data_dir}/m10_output_{type}_{S:03d}.bin'
print('ifn= ',ifn)
print('ofn= ',ofn)

#================
if type == 'upper':
  vo = 5
  zo = 13
elif type == 'surface':
  vo = 4
  zo = 1

#================
#
if not os.path.isdir(output_data_dir):
    os.mkdir(output_data_dir)
#讀檔
print('load...')
data = np.load(ifn)
data.shape = data.shape
print('data.shape= ', data.shape)

# 將陣列儲存為二進制檔案, 直接寫出
with open(ofn, 'wb') as f:
  data.tofile(f)
input_data_dir  = './output_data/'
output_data_dir = './output_data-bin'
ifn = f'{input_data_dir}/m11_output_{type}_{T}.npy'
ofn = f'{output_data_dir}/m11_output_{type}_{S:03d}.bin'
print('ifn= ',ifn)
print('ofn= ',ofn)

#================
if type == 'upper':
  vo = 5
  zo = 13
elif type == 'surface':
  vo = 4
  zo = 1

#================
#
if not os.path.isdir(output_data_dir):
    os.mkdir(output_data_dir)
#讀檔
print('load...')
data = np.load(ifn)
data.shape = data.shape
print('data.shape= ', data.shape)

# 將陣列儲存為二進制檔案, 直接寫出
with open(ofn, 'wb') as f:
  data.tofile(f)
input_data_dir  = './output_data/'
output_data_dir = './output_data-bin'
ifn = f'{input_data_dir}/m12_output_{type}_{T}.npy'
ofn = f'{output_data_dir}/m12_output_{type}_{S:03d}.bin'
print('ifn= ',ifn)
print('ofn= ',ofn)

#================
if type == 'upper':
  vo = 5
  zo = 13
elif type == 'surface':
  vo = 4
  zo = 1

#================
#
if not os.path.isdir(output_data_dir):
    os.mkdir(output_data_dir)
#讀檔
print('load...')
data = np.load(ifn)
data.shape = data.shape
print('data.shape= ', data.shape)

# 將陣列儲存為二進制檔案, 直接寫出
with open(ofn, 'wb') as f:
  data.tofile(f)
input_data_dir  = './output_data/'
output_data_dir = './output_data-bin'
ifn = f'{input_data_dir}/m13_output_{type}_{T}.npy'
ofn = f'{output_data_dir}/m13_output_{type}_{S:03d}.bin'
print('ifn= ',ifn)
print('ofn= ',ofn)

#================
if type == 'upper':
  vo = 5
  zo = 13
elif type == 'surface':
  vo = 4
  zo = 1

#================
#
if not os.path.isdir(output_data_dir):
    os.mkdir(output_data_dir)
#讀檔
print('load...')
data = np.load(ifn)
data.shape = data.shape
print('data.shape= ', data.shape)

# 將陣列儲存為二進制檔案, 直接寫出
with open(ofn, 'wb') as f:
  data.tofile(f)
input_data_dir  = './output_data/'
output_data_dir = './output_data-bin'
ifn = f'{input_data_dir}/m14_output_{type}_{T}.npy'
ofn = f'{output_data_dir}/m14_output_{type}_{S:03d}.bin'
print('ifn= ',ifn)
print('ofn= ',ofn)

#================
if type == 'upper':
  vo = 5
  zo = 13
elif type == 'surface':
  vo = 4
  zo = 1

#================
#
if not os.path.isdir(output_data_dir):
    os.mkdir(output_data_dir)
#讀檔
print('load...')
data = np.load(ifn)
data.shape = data.shape
print('data.shape= ', data.shape)

# 將陣列儲存為二進制檔案, 直接寫出
with open(ofn, 'wb') as f:
  data.tofile(f)
input_data_dir  = './output_data/'
output_data_dir = './output_data-bin'
ifn = f'{input_data_dir}/m15_output_{type}_{T}.npy'
ofn = f'{output_data_dir}/m15_output_{type}_{S:03d}.bin'
print('ifn= ',ifn)
print('ofn= ',ofn)

#================
if type == 'upper':
  vo = 5
  zo = 13
elif type == 'surface':
  vo = 4
  zo = 1

#================
#
if not os.path.isdir(output_data_dir):
    os.mkdir(output_data_dir)
#讀檔
print('load...')
data = np.load(ifn)
data.shape = data.shape
print('data.shape= ', data.shape)

# 將陣列儲存為二進制檔案, 直接寫出
with open(ofn, 'wb') as f:
  data.tofile(f)
input_data_dir  = './output_data/'
output_data_dir = './output_data-bin'
ifn = f'{input_data_dir}/m16_output_{type}_{T}.npy'
ofn = f'{output_data_dir}/m16_output_{type}_{S:03d}.bin'
print('ifn= ',ifn)
print('ofn= ',ofn)

#================
if type == 'upper':
  vo = 5
  zo = 13
elif type == 'surface':
  vo = 4
  zo = 1

#================
#
if not os.path.isdir(output_data_dir):
    os.mkdir(output_data_dir)
#讀檔
print('load...')
data = np.load(ifn)
data.shape = data.shape
print('data.shape= ', data.shape)

# 將陣列儲存為二進制檔案, 直接寫出
with open(ofn, 'wb') as f:
  data.tofile(f)
input_data_dir  = './output_data/'
output_data_dir = './output_data-bin'
ifn = f'{input_data_dir}/m17_output_{type}_{T}.npy'
ofn = f'{output_data_dir}/m17_output_{type}_{S:03d}.bin'
print('ifn= ',ifn)
print('ofn= ',ofn)

#================
if type == 'upper':
  vo = 5
  zo = 13
elif type == 'surface':
  vo = 4
  zo = 1

#================
#
if not os.path.isdir(output_data_dir):
    os.mkdir(output_data_dir)
#讀檔
print('load...')
data = np.load(ifn)
data.shape = data.shape
print('data.shape= ', data.shape)

# 將陣列儲存為二進制檔案, 直接寫出
with open(ofn, 'wb') as f:
  data.tofile(f)
input_data_dir  = './output_data/'
output_data_dir = './output_data-bin'
ifn = f'{input_data_dir}/m18_output_{type}_{T}.npy'
ofn = f'{output_data_dir}/m18_output_{type}_{S:03d}.bin'
print('ifn= ',ifn)
print('ofn= ',ofn)

#================
if type == 'upper':
  vo = 5
  zo = 13
elif type == 'surface':
  vo = 4
  zo = 1

#================
#
if not os.path.isdir(output_data_dir):
    os.mkdir(output_data_dir)
#讀檔
print('load...')
data = np.load(ifn)
data.shape = data.shape
print('data.shape= ', data.shape)

# 將陣列儲存為二進制檔案, 直接寫出
with open(ofn, 'wb') as f:
  data.tofile(f)
input_data_dir  = './output_data/'
output_data_dir = './output_data-bin'
ifn = f'{input_data_dir}/m19_output_{type}_{T}.npy'
ofn = f'{output_data_dir}/m19_output_{type}_{S:03d}.bin'
print('ifn= ',ifn)
print('ofn= ',ofn)

#================
if type == 'upper':
  vo = 5
  zo = 13
elif type == 'surface':
  vo = 4
  zo = 1

#================
#
if not os.path.isdir(output_data_dir):
    os.mkdir(output_data_dir)
#讀檔
print('load...')
data = np.load(ifn)
data.shape = data.shape
print('data.shape= ', data.shape)

# 將陣列儲存為二進制檔案, 直接寫出
with open(ofn, 'wb') as f:
  data.tofile(f)
input_data_dir  = './output_data/'
output_data_dir = './output_data-bin'
ifn = f'{input_data_dir}/m20_output_{type}_{T}.npy'
ofn = f'{output_data_dir}/m20_output_{type}_{S:03d}.bin'
print('ifn= ',ifn)
print('ofn= ',ofn)

#================
if type == 'upper':
  vo = 5
  zo = 13
elif type == 'surface':
  vo = 4
  zo = 1

#================
#
if not os.path.isdir(output_data_dir):
    os.mkdir(output_data_dir)
#讀檔
print('load...')
data = np.load(ifn)
data.shape = data.shape
print('data.shape= ', data.shape)

# 將陣列儲存為二進制檔案, 直接寫出
with open(ofn, 'wb') as f:
  data.tofile(f)
input_data_dir  = './output_data/'
output_data_dir = './output_data-bin'
ifn = f'{input_data_dir}/m21_output_{type}_{T}.npy'
ofn = f'{output_data_dir}/m21_output_{type}_{S:03d}.bin'
print('ifn= ',ifn)
print('ofn= ',ofn)

#================
if type == 'upper':
  vo = 5
  zo = 13
elif type == 'surface':
  vo = 4
  zo = 1

#================
#
if not os.path.isdir(output_data_dir):
    os.mkdir(output_data_dir)
#讀檔
print('load...')
data = np.load(ifn)
data.shape = data.shape
print('data.shape= ', data.shape)

# 將陣列儲存為二進制檔案, 直接寫出
with open(ofn, 'wb') as f:
  data.tofile(f)
input_data_dir  = './output_data/'
output_data_dir = './output_data-bin'
ifn = f'{input_data_dir}/m22_output_{type}_{T}.npy'
ofn = f'{output_data_dir}/m22_output_{type}_{S:03d}.bin'
print('ifn= ',ifn)
print('ofn= ',ofn)

#================
if type == 'upper':
  vo = 5
  zo = 13
elif type == 'surface':
  vo = 4
  zo = 1

#================
#
if not os.path.isdir(output_data_dir):
    os.mkdir(output_data_dir)
#讀檔
print('load...')
data = np.load(ifn)
data.shape = data.shape
print('data.shape= ', data.shape)

# 將陣列儲存為二進制檔案, 直接寫出
with open(ofn, 'wb') as f:
  data.tofile(f)
input_data_dir  = './output_data/'
output_data_dir = './output_data-bin'
ifn = f'{input_data_dir}/m23_output_{type}_{T}.npy'
ofn = f'{output_data_dir}/m23_output_{type}_{S:03d}.bin'
print('ifn= ',ifn)
print('ofn= ',ofn)

#================
if type == 'upper':
  vo = 5
  zo = 13
elif type == 'surface':
  vo = 4
  zo = 1

#================
#
if not os.path.isdir(output_data_dir):
    os.mkdir(output_data_dir)
#讀檔
print('load...')
data = np.load(ifn)
data.shape = data.shape
print('data.shape= ', data.shape)

# 將陣列儲存為二進制檔案, 直接寫出
with open(ofn, 'wb') as f:
  data.tofile(f)
input_data_dir  = './output_data/'
output_data_dir = './output_data-bin'
ifn = f'{input_data_dir}/m24_output_{type}_{T}.npy'
ofn = f'{output_data_dir}/m24_output_{type}_{S:03d}.bin'
print('ifn= ',ifn)
print('ofn= ',ofn)

#================
if type == 'upper':
  vo = 5
  zo = 13
elif type == 'surface':
  vo = 4
  zo = 1

#================
#
if not os.path.isdir(output_data_dir):
    os.mkdir(output_data_dir)
#讀檔
print('load...')
data = np.load(ifn)
data.shape = data.shape
print('data.shape= ', data.shape)

# 將陣列儲存為二進制檔案, 直接寫出
with open(ofn, 'wb') as f:
  data.tofile(f)
input_data_dir  = './output_data/'
output_data_dir = './output_data-bin'
ifn = f'{input_data_dir}/m25_output_{type}_{T}.npy'
ofn = f'{output_data_dir}/m25_output_{type}_{S:03d}.bin'
print('ifn= ',ifn)
print('ofn= ',ofn)

#================
if type == 'upper':
  vo = 5
  zo = 13
elif type == 'surface':
  vo = 4
  zo = 1

#================
#
if not os.path.isdir(output_data_dir):
    os.mkdir(output_data_dir)
#讀檔
print('load...')
data = np.load(ifn)
data.shape = data.shape
print('data.shape= ', data.shape)

# 將陣列儲存為二進制檔案, 直接寫出
with open(ofn, 'wb') as f:
  data.tofile(f)
input_data_dir  = './output_data/'
output_data_dir = './output_data-bin'
ifn = f'{input_data_dir}/m26_output_{type}_{T}.npy'
ofn = f'{output_data_dir}/m26_output_{type}_{S:03d}.bin'
print('ifn= ',ifn)
print('ofn= ',ofn)

#================
if type == 'upper':
  vo = 5
  zo = 13
elif type == 'surface':
  vo = 4
  zo = 1

#================
#
if not os.path.isdir(output_data_dir):
    os.mkdir(output_data_dir)
#讀檔
print('load...')
data = np.load(ifn)
data.shape = data.shape
print('data.shape= ', data.shape)

# 將陣列儲存為二進制檔案, 直接寫出
with open(ofn, 'wb') as f:
  data.tofile(f)
input_data_dir  = './output_data/'
output_data_dir = './output_data-bin'
ifn = f'{input_data_dir}/m27_output_{type}_{T}.npy'
ofn = f'{output_data_dir}/m27_output_{type}_{S:03d}.bin'
print('ifn= ',ifn)
print('ofn= ',ofn)

#================
if type == 'upper':
  vo = 5
  zo = 13
elif type == 'surface':
  vo = 4
  zo = 1

#================
#
if not os.path.isdir(output_data_dir):
    os.mkdir(output_data_dir)
#讀檔
print('load...')
data = np.load(ifn)
data.shape = data.shape
print('data.shape= ', data.shape)

# 將陣列儲存為二進制檔案, 直接寫出
with open(ofn, 'wb') as f:
  data.tofile(f)
input_data_dir  = './output_data/'
output_data_dir = './output_data-bin'
ifn = f'{input_data_dir}/m28_output_{type}_{T}.npy'
ofn = f'{output_data_dir}/m28_output_{type}_{S:03d}.bin'
print('ifn= ',ifn)
print('ofn= ',ofn)

#================
if type == 'upper':
  vo = 5
  zo = 13
elif type == 'surface':
  vo = 4
  zo = 1

#================
#
if not os.path.isdir(output_data_dir):
    os.mkdir(output_data_dir)
#讀檔
print('load...')
data = np.load(ifn)
data.shape = data.shape
print('data.shape= ', data.shape)

# 將陣列儲存為二進制檔案, 直接寫出
with open(ofn, 'wb') as f:
  data.tofile(f)
input_data_dir  = './output_data/'
output_data_dir = './output_data-bin'
ifn = f'{input_data_dir}/m29_output_{type}_{T}.npy'
ofn = f'{output_data_dir}/m29_output_{type}_{S:03d}.bin'
print('ifn= ',ifn)
print('ofn= ',ofn)

#================
if type == 'upper':
  vo = 5
  zo = 13
elif type == 'surface':
  vo = 4
  zo = 1

#================
#
if not os.path.isdir(output_data_dir):
    os.mkdir(output_data_dir)
#讀檔
print('load...')
data = np.load(ifn)
data.shape = data.shape
print('data.shape= ', data.shape)

# 將陣列儲存為二進制檔案, 直接寫出
with open(ofn, 'wb') as f:
  data.tofile(f)
input_data_dir  = './output_data/'
output_data_dir = './output_data-bin'
ifn = f'{input_data_dir}/m30_output_{type}_{T}.npy'
ofn = f'{output_data_dir}/m30_output_{type}_{S:03d}.bin'
print('ifn= ',ifn)
print('ofn= ',ofn)

#================
if type == 'upper':
  vo = 5
  zo = 13
elif type == 'surface':
  vo = 4
  zo = 1

#================
#
if not os.path.isdir(output_data_dir):
    os.mkdir(output_data_dir)
#讀檔
print('load...')
data = np.load(ifn)
data.shape = data.shape
print('data.shape= ', data.shape)

# 將陣列儲存為二進制檔案, 直接寫出
with open(ofn, 'wb') as f:
  data.tofile(f)
input_data_dir  = './output_data/'
output_data_dir = './output_data-bin'
ifn = f'{input_data_dir}/m31_output_{type}_{T}.npy'
ofn = f'{output_data_dir}/m31_output_{type}_{S:03d}.bin'
print('ifn= ',ifn)
print('ofn= ',ofn)

#================
if type == 'upper':
  vo = 5
  zo = 13
elif type == 'surface':
  vo = 4
  zo = 1

#================
#
if not os.path.isdir(output_data_dir):
    os.mkdir(output_data_dir)
#讀檔
print('load...')
data = np.load(ifn)
data.shape = data.shape
print('data.shape= ', data.shape)

# 將陣列儲存為二進制檔案, 直接寫出
with open(ofn, 'wb') as f:
  data.tofile(f)
input_data_dir  = './output_data/'
output_data_dir = './output_data-bin'
ifn = f'{input_data_dir}/m32_output_{type}_{T}.npy'
ofn = f'{output_data_dir}/m32_output_{type}_{S:03d}.bin'
print('ifn= ',ifn)
print('ofn= ',ofn)

#================
if type == 'upper':
  vo = 5
  zo = 13
elif type == 'surface':
  vo = 4
  zo = 1

#================
#
if not os.path.isdir(output_data_dir):
    os.mkdir(output_data_dir)
#讀檔
print('load...')
data = np.load(ifn)
data.shape = data.shape
print('data.shape= ', data.shape)

# 將陣列儲存為二進制檔案, 直接寫出
with open(ofn, 'wb') as f:
  data.tofile(f)
 





# 將陣列儲存為二進制檔案, 逐層寫出
#with open(ofn, 'wb') as f:
#  for i in range(vo):
#    for j in range(zo):
#      print(i, j)
#      if type == 'upper':
#        out = np.flip(data[ i, j, :, :], axis=0) #倒序
#      else:
#        out = np.flip(data[ i, :, :], axis=0)
#      out.tofile(f)
#================
sys.exit(0)

