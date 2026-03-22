import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
from matplotlib.lines import Line2D

# 關閉互動模式
plt.ioff()

# ==========================================
# 1. 設定區域 (User Configuration)
# ==========================================
TRACK_FOLDER = './'
SUFFIX = "_1005hPa"

# A4 直向尺寸 (11 x 16 incha)
DPI_SETTING = 330
FIG_SIZE_A4_PORTRAIT = (11, 16)

# 地圖範圍緩衝區 (單位: 度)
MAP_BUFFER = 2.0

# 10 個個案清單
case_dates = {
    'Usagi':   ['20241112', '2024111212', '20241113', '2024111312', '20241114'],
    'Kongrey': ['20241027', '2024102712', '20241028', '2024102812', '20241029'],
    'Krathon': ['20240928', '2024092812', '20240929', '2024092912', '20240930'],
    'Gaemi':   ['20240720', '2024072012', '20240721', '2024072112', '20240722'],
    'Koinu':   ['20231001', '2023100112', '20231002', '2023100212', '20231003'],
    'Haikui':  ['2023082912', '20230830', '2023083012', '20230831', '2023083112'],
    'Saola':   ['20230826', '2023082612', '20230827', '2023082712', '20230828'],
    'Khanun':  ['2023072912', '20230730', '2023073012', '20230731', '2023073112'],
    'Doksuri': ['2023072212', '20230723', '2023072312', '20230724', '2023072412'],
    'Mawar':   ['20230526', '2023052612', '20230527', '2023052712', '20230528'],
}

cases = list(case_dates.keys())

# ==========================================
# 2. 全域資料準備
# ==========================================
model_list = [f"{i:02d}" for i in range(1, 33)]

try:
    coast = pd.read_csv('coast.csv')
    has_coast = True
except FileNotFoundError:
    print("⚠️ 警告: 找不到 coast.csv")
    has_coast = False

# ==========================================
# 3. 核心功能函式
# ==========================================

def determine_color(filename):
    fname = os.path.basename(filename)
    if fname.startswith("PG_mean_track"): return 'red'
    elif fname.startswith("PG_newtrack"): return 'blue'
    elif fname.startswith("m") and "_newtrack_" in fname: return 'gray'
    else: return 'black'

def load_track(filepath):
    lons, lats = [], []
    if os.path.exists(filepath):
        with open(filepath, 'r') as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) != 3: continue
                lon, lat = map(float, parts[:2])
                if lon == 0 and lat == 0: continue
                lons.append(lon)
                lats.append(lat)
    return lons, lats

def calculate_bounds(case_name, dates):
    min_lon, max_lon = 360, 0
    min_lat, max_lat = 90, -90
    has_data = False

    for date in dates:
        gray_files = [os.path.join(TRACK_FOLDER, f"m{model}_newtrack_{date}{SUFFIX}.txt") for model in model_list]
        black_file = os.path.join(TRACK_FOLDER, f"{case_name}.txt")
        blue_file  = os.path.join(TRACK_FOLDER, f"PG_newtrack_{date}{SUFFIX}.txt")
        red_file   = os.path.join(TRACK_FOLDER, f"PG_mean_track_{date}{SUFFIX}.txt")
        all_files = gray_files + [blue_file, red_file, black_file]

        for file in all_files:
            lons, lats = load_track(file)
            if lons and lats:
                has_data = True
                min_lon = min(min_lon, min(lons))
                max_lon = max(max_lon, max(lons))
                min_lat = min(min_lat, min(lats))
                max_lat = max(max_lat, max(lats))

    if not has_data:
        return 115, 130, 15, 30

    return (min_lon - MAP_BUFFER), (max_lon + MAP_BUFFER), (min_lat - MAP_BUFFER), (max_lat + MAP_BUFFER)

def draw_tracks_on_ax(ax, case_name, date, label_text, ic_num, bounds):
    lon_min, lon_max, lat_min, lat_max = bounds

    gray_files = [os.path.join(TRACK_FOLDER, f"m{model}_newtrack_{date}{SUFFIX}.txt") for model in model_list]
    black_file = os.path.join(TRACK_FOLDER, f"{case_name}.txt")
    blue_file  = os.path.join(TRACK_FOLDER, f"PG_newtrack_{date}{SUFFIX}.txt")
    red_file   = os.path.join(TRACK_FOLDER, f"PG_mean_track_{date}{SUFFIX}.txt")
    all_files = gray_files + [blue_file, red_file, black_file]

    if has_coast:
        ax.plot(coast['lon_map'], coast['lat_map'], color='k', linewidth=0.5)

    for file in all_files:
        lons, lats = load_track(file)
        if lons and lats:
            color = determine_color(file)
            if color == 'gray':
                lw, alpha, zorder = 0.8, 0.6, 1
            else:
                lw, alpha, zorder = 1.5, 1.0, 10

            ax.plot(lons, lats, color=color, linewidth=lw, alpha=alpha, zorder=zorder)
            ax.scatter(lons, lats, color=color, s=10, zorder=zorder)

            if color == 'gray':
                fname = os.path.basename(file)
                label = fname.split('_')[0]
                ax.text(lons[-1] + 0.1, lats[-1] + 0.1, label, color='gray', fontsize=6, alpha=0.8)

    ax.set_xlim(lon_min, lon_max)
    ax.set_ylim(lat_min, lat_max)
    ax.grid(True, linestyle='--', alpha=0.5)

    # === 修改重點：日期顯示格式 ===
    # 如果日期長度是 8 (例如 20241112)，則補上 00；否則維持原樣
    display_date = date + "00" if len(date) == 8 else date

    ax.set_title(f"IC{ic_num}: {display_date}", fontsize=14, fontweight='bold', loc='center')
    ax.set_title(label_text, fontsize=16, fontweight='bold', loc='left')

# ==========================================
# 4. 主程式迴圈
# ==========================================

print(f"🚀 開始批次繪圖程序 (AllTrack)...")

legend_lines = [
    Line2D([0], [0], color='black', marker='o', markersize=4, linestyle='-', linewidth=1.5, label='Observation'),
    Line2D([0], [0], color='red', marker='o', markersize=4, linestyle='-', linewidth=1.5, label='Ens Mean'),
    Line2D([0], [0], color='blue', marker='o', markersize=4, linestyle='-', linewidth=1.5, label='Control (PG)'),
    Line2D([0], [0], color='gray', marker='o', markersize=4, linestyle='-', linewidth=1, label='Ens Member'),
]

sub_labels = ['(a)', '(b)', '(c)', '(d)', '(e)']

for case in cases:
    dates = case_dates.get(case, [])
    if not dates: continue
    print(f"   處理: {case} ...")

    bounds = calculate_bounds(case, dates)

    fig, axes = plt.subplots(nrows=3, ncols=2, figsize=FIG_SIZE_A4_PORTRAIT)
    axes_flat = axes.flatten()

    fig.suptitle(f"{case} Tracks", fontsize=20, fontweight='bold', y=0.98)

    for i in range(5):
        ax = axes_flat[i]
        is_left_col = (i % 2 == 0)

        if i < len(dates):
            date = dates[i]
            label = sub_labels[i]
            draw_tracks_on_ax(ax, case, date, label, i+1, bounds)

            if is_left_col:
                ax.set_ylabel("Latitude", fontsize=12)
            if i == 4 or i == 3:
                ax.set_xlabel("Longitude", fontsize=12)
        else:
            ax.axis('off')

    ax_last = axes_flat[5]
    ax_last.axis('off')

    fig.legend(handles=legend_lines,
               loc='upper right',
               bbox_to_anchor=(0.99, 0.98),
               fontsize=10,
               title="Track Source",
               title_fontsize=12,
               frameon=True,
               edgecolor='black')

    plt.tight_layout(rect=[0, 0, 1, 0.95])

    out_path = os.path.join(TRACK_FOLDER, f"alltrack_{case}.png")
    plt.savefig(out_path, dpi=DPI_SETTING)
    plt.close()
    print(f"   ✅ 已儲存: {out_path}")

print("🎉 AllTrack 完成！")
