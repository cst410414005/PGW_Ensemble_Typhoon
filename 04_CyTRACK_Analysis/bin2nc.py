import sys
from xgrads import open_CtlDataset
import os
os.system("sync")  # 確保變更已寫入

# 取得 Bash 傳入的變數
i = sys.argv[1]  # 取得 m01, m02...
time_step = int(sys.argv[2])  # 轉換為整數
IC = sys.argv[3]  # 取得起始日期 (YYYYMMDD 格式)

# 解析日期 (YYYYMMDD)
year = IC[:4]
month = IC[4:6]
day = int(IC[6:8])

# **計算跨天日期**
date_offset = time_step // 24
new_day = day + date_offset

# **處理跨月**
if month == "09" and new_day > 30:
    month = "10"
    new_day = new_day - 30

# **確保日期是兩位數**
formatted_date = f"{year}{month}{new_day:02d}"

# **計算時間 (`00, 06, 12, 18`)**
time_map = {0: "00", 6: "06", 12: "12", 18: "18"}
nc_time = time_map[time_step % 24]

# 設定輸出目錄
output_dir = f"/jet/tgeo/output_data-bin/cytrack/ERA5_data/{IC}/m{i}"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# **處理 `upper` 資料**
dataset_upper = open_CtlDataset('bin2nc_upper.ctl')
dataset_upper = dataset_upper.rename({
    "lat": "latitude",
    "lon": "longitude",
    "lev": "level",
    "Z": "z",
    "Q": "q",
    "T": "t",
    "U": "u",
    "V": "v"
})
dataset_upper = dataset_upper.assign_coords({
    "latitude": dataset_upper["latitude"],
    "longitude": dataset_upper["longitude"]
})
dataset_upper["z"].attrs["units"] = "m**2 s**-2"
dataset_upper["z"].attrs["long_name"] = "Geopotential"
dataset_upper["z"].attrs["standard_name"] = "geopotential"
dataset_upper.to_netcdf(f'{output_dir}/upper_{formatted_date}_{nc_time}.nc')

# **處理 `surface` 資料**
dataset_surface = open_CtlDataset('bin2nc_surface.ctl')
dataset_surface = dataset_surface.rename({
    "lat": "latitude",
    "lon": "longitude",
    "lev": "level",
    "mslsfc": "msl",
    "no10usfc": "u10",
    "no10vsfc": "v10",
    "no2tsfc": "t2m"
})
dataset_surface = dataset_surface.assign_coords({
    "latitude": dataset_surface["latitude"],
    "longitude": dataset_surface["longitude"]
})

#dataset_surface["time"].attrs["units"] = "hours since 1900-01-01 00:00:00.0"
#dataset_surface["time"].attrs["calendar"] = "gregorian"
#dataset_surface["time"].attrs["long_name"] = "time"
dataset_surface["msl"].attrs["units"] = "Pa"
dataset_surface["msl"].attrs["long_name"] = "Mean sea level pressure"
dataset_surface["msl"].attrs["standard_name"] = "air_pressure_at_mean_sea_level"
dataset_surface["u10"].attrs["units"] = "m s**-1"
dataset_surface["u10"].attrs["long_name"] = "10 metre U wind component"
dataset_surface["v10"].attrs["units"] = "m s**-1"
dataset_surface["v10"].attrs["long_name"] = "10 metre V wind component"
dataset_surface.to_netcdf(f'{output_dir}/surface_{formatted_date}_{nc_time}.nc')

# **輸出確認**
print(f"Upper → /m{i}/upper_{formatted_date}_{nc_time}.nc", flush=True)
print(f"Surface → /m{i}/surface_{formatted_date}_{nc_time}.nc", flush=True)
