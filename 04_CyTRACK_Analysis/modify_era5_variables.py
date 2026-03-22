#!/usr/bin/env python3
#===========================================================================================
import xarray as xr
import numpy as np
import os

# -----------------
# PARAMETERS - 可控變數
# -----------------
INPUT_FILE = 'surface_m01_20230724_12.nc'
OUTPUT_FILE = 'surface_m01_20230729_18.nc'
MSL_MULTIPLIER = 1E9    # msl變數的放大倍數
WIND_DIVISOR = 1E9      # u10和v10變數的縮小倍數

# 確保檔案存在
if not os.path.exists(INPUT_FILE):
    print(f"Error: Input file '{INPUT_FILE}' not found!")
    exit(1)

# -----------------
# OPEN - 讀取原始檔案
# -----------------
print(f"Reading original file: {INPUT_FILE}")
ds = xr.open_dataset(INPUT_FILE)

print("Original dataset information:")
print(f"    Dimensions: {dict(ds.sizes)}")  # 修正：使用sizes替代dims
print(f"    Variables: {list(ds.data_vars)}")
print(f"    Coordinates: {list(ds.coords)}")

# 檢查原始數值範圍
print("\nOriginal variable ranges:")
print(f"    mslsfc: {float(ds.mslsfc.min()):.2f} to {float(ds.mslsfc.max()):.2f} {ds.mslsfc.attrs.get('units', 'unknown')}")
print(f"    no10usfc: {float(ds.no10usfc.min()):.3f} to {float(ds.no10usfc.max()):.3f} {ds.no10usfc.attrs.get('units', 'unknown')}")
print(f"    no10vsfc: {float(ds.no10vsfc.min()):.3f} to {float(ds.no10vsfc.max()):.3f} {ds.no10vsfc.attrs.get('units', 'unknown')}")

#breakpoint()  # 檢查原始資料

# -----------------
# DEFINE - 複製並修改資料集
# -----------------
print("\nCreating modified dataset...")

# 複製原始資料集
newds = ds.copy(deep=True)

# 修改msl：放大1E9倍
print(f"Modifying mslsfc: multiplying by {MSL_MULTIPLIER:.0e}")
newds['mslsfc'] = newds['mslsfc'] * MSL_MULTIPLIER

# 修改u10：縮小1E9倍
print(f"Modifying no10usfc: dividing by {WIND_DIVISOR:.0e}")  
newds['no10usfc'] = newds['no10usfc'] / WIND_DIVISOR

# 修改v10：縮小1E9倍
print(f"Modifying no10vsfc: dividing by {WIND_DIVISOR:.0e}")
newds['no10vsfc'] = newds['no10vsfc'] / WIND_DIVISOR

# 檢查修改後的數值範圍
print("\nModified variable ranges:")
print(f"    new_mslsfc: {float(newds.mslsfc.min()):.2e} to {float(newds.mslsfc.max()):.2e} {newds.mslsfc.attrs.get('units', 'unknown')}")
print(f"    new_no10usfc: {float(newds.no10usfc.min()):.6f} to {float(newds.no10usfc.max()):.6f} {newds.no10usfc.attrs.get('units', 'unknown')}")
print(f"    new_no10vsfc: {float(newds.no10vsfc.min()):.6f} to {float(newds.no10vsfc.max()):.6f} {newds.no10vsfc.attrs.get('units', 'unknown')}")

# 驗證變化
mslsfc_ratio = float(newds.mslsfc.mean()) / float(ds.mslsfc.mean())
no10usfc_ratio = float(newds.no10usfc.mean()) / float(ds.no10usfc.mean())
no10vsfc_ratio = float(newds.no10vsfc.mean()) / float(ds.no10vsfc.mean())

print(f"\nVerification - actual change ratios:")
print(f"    mslsfc change ratio: {mslsfc_ratio:.2e} (should be ~{MSL_MULTIPLIER:.0e})")
print(f"    no10usfc change ratio: {no10usfc_ratio:.2e} (should be ~{1/WIND_DIVISOR:.0e})")
print(f"    no10vsfc change ratio: {no10vsfc_ratio:.2e} (should be ~{1/WIND_DIVISOR:.0e})")

# 檢查資料型態是否保持
print(f"\nData types:")
print(f"    original mslsfc dtype: {ds.mslsfc.dtype}")
print(f"    modified mslsfc dtype: {newds.mslsfc.dtype}")
print(f"    original no10usfc dtype: {ds.no10usfc.dtype}")
print(f"    modified no10usfc dtype: {newds.no10usfc.dtype}")

#breakpoint()  # 檢查修改後的資料

# -----------------
# WRITE AND SAVE - 保存修改後的檔案
# -----------------
print(f"\nSaving modified dataset to: {OUTPUT_FILE}")

# 更新全域屬性，記錄修改歷史
if 'history' in newds.attrs:
    original_history = newds.attrs['history']
    newds.attrs['history'] = f"Modified by Python script - msl*{MSL_MULTIPLIER:.0e}, u10,v10/{WIND_DIVISOR:.0e}; Original: {original_history}"
else:
    newds.attrs['history'] = f"Modified by Python script - msl*{MSL_MULTIPLIER:.0e}, u10,v10/{WIND_DIVISOR:.0e}"

# 保存為netCDF檔案
try:
    newds.to_netcdf(OUTPUT_FILE)
    print(f"Successfully saved modified dataset to: {OUTPUT_FILE}")
    
    # 檢查輸出檔案大小
    input_size = os.path.getsize(INPUT_FILE) / (1024**2)  # MB
    output_size = os.path.getsize(OUTPUT_FILE) / (1024**2)  # MB
    print(f"File sizes:")
    print(f"    Input file: {input_size:.2f} MB")
    print(f"    Output file: {output_size:.2f} MB")
    
except Exception as e:
    print(f"Error saving file: {e}")

# -----------------
# VERIFY - 驗證保存的檔案
# -----------------
print(f"\nVerifying saved file...")
try:
    verify_ds = xr.open_dataset(OUTPUT_FILE)
    print("Verification successful!")
    print(f"    Saved file dimensions: {dict(verify_ds.sizes)}")
    print(f"    Saved file variables: {list(verify_ds.data_vars)}")
    
    # 快速檢查數值
    print(f"    Saved mslsfc range: {float(verify_ds.mslsfc.min()):.2e} to {float(verify_ds.mslsfc.max()):.2e}")
    print(f"    Saved no10usfc range: {float(verify_ds.no10usfc.min()):.6f} to {float(verify_ds.no10usfc.max()):.6f}")
    print(f"    Saved no10vsfc range: {float(verify_ds.no10vsfc.min()):.6f} to {float(verify_ds.no10vsfc.max()):.6f}")
    
    # 檢查是否保持了原始的屬性
    print(f"\nAttribute preservation check:")
    print(f"    msl attributes: {list(verify_ds.mslsfc.attrs.keys())}")
    print(f"    u10 attributes: {list(verify_ds.no10usfc.attrs.keys())}")
    print(f"    v10 attributes: {list(verify_ds.no10vsfc.attrs.keys())}")
    
    verify_ds.close()
except Exception as e:
    print(f"Error verifying file: {e}")

# 關閉資料集
ds.close()
newds.close()

print("\nProcessing completed successfully!")
#breakpoint()  # 最終檢查

#===========================================================================================
