import os
from datetime import datetime, timedelta

# === 🧩 使用者設定區（只改這裡） ===
case = "Mawar"
target_line = 9
date = "20230528"                            # 資料日期
start_time = "2023052800"                   # 起始時間（含）
end_time = "2023060206"                     # 結束時間（含）
models_to_process = range(1, 33)           # 要處理的模型編號（例如 range(1, 33) 表示 m01 到 m32）
wind_threshold = "1005hPa"                     # 風速門檻資料夾名稱（可改為 "13ms", "11ms"）
output_root = "/jet/tgeo/output_data-bin/cytrack/CyTRACK-1.0.3-6/testing_CyTRACK_PG"
# ✅ 目標位置與範圍（使用者輸入參考點 ±5 度）
input_file = f"/jet/tgeo/output_data-bin/asia_bin/{case}.txt"
with open(input_file) as f:
    ref_lon, ref_lat, *_ = map(float, f.readlines()[target_line - 1].split())
print(f"ref_lon={ref_lon}, ref_lat={ref_lat}")

lat_min, lat_max = ref_lat - 6, ref_lat + 6
lon_min, lon_max = ref_lon - 6, ref_lon + 6
# =========================================

def generate_time_axis(start_str, end_str, interval_hr=6):
    start = datetime.strptime(start_str, "%Y%m%d%H")
    end = datetime.strptime(end_str, "%Y%m%d%H")
    times = []
    while start <= end:
        times.append(start.strftime("%Y%m%d%H"))
        start += timedelta(hours=interval_hr)
    return times

def split_and_select_case(dat_file, model, date, start_time, end_time):
    base_output_dir = os.path.join(output_root, date, wind_threshold, model)
    os.makedirs(base_output_dir, exist_ok=True)

    with open(dat_file, "r") as file:
        lines = file.readlines()

    data_blocks = {}
    current_model = None
    matched_model_name = None

    for line in lines:
        parts = line.strip().split(", ")
        if len(parts) == 2:
            current_model = parts[0]
            data_blocks[current_model] = {}
        elif current_model:
            time_str = parts[0] + parts[1].zfill(2)
            data_blocks[current_model][time_str] = parts

    time_axis = generate_time_axis(start_time, end_time)
    invalid_cases = {}

    for model_name, records in data_blocks.items():
        model_txt_path = os.path.join(base_output_dir, f"{model}_{model_name}.txt")
        valid_coords = [r for r in records.values() if r[2] != "0" and r[3] != "0"]
        invalid_cases[model_name] = [(r[2], r[3]) for r in valid_coords[:3]]
        time_map = {r[0] + r[1].zfill(2): r for r in records}
        with open(model_txt_path, "w") as f:
            for t in time_axis:
                if t in records:
                    f.write(", ".join(records[t]) + "\n")
                else:
                    f.write(f"{t[:8]}, {t[8:]}, 0, 0, 0, 0, 0, 0, 0, UDCC, -99999, -99999, -99999\n")

        first_valid_record = next((r for r in records.values() if r[2] != "0" and r[3] != "0"), None)

        if first_valid_record:
            try:
                lat = float(first_valid_record[2])
                lon = float(first_valid_record[3])
                if lat_min <= lat <= lat_max and lon_min <= lon <= lon_max:
                    matched_model_name = f"{model}_{model_name}.txt"
            except Exception as e:
                print(f"⚠️ 模型 {model} 的 {model_name} 發生座標轉換錯誤：{e}")
        else:
            print(f"⚠️ 模型 {model} 的 {model_name} 無有效資料")

    return matched_model_name, invalid_cases

def generate_outputs(txt_file, model, date):
    base_output_dir = os.path.join(output_root, date, wind_threshold)

    if not os.path.exists(txt_file):
        print(f"錯誤：檔案 {txt_file} 不存在。")
        return

    with open(txt_file, "r") as f:
        lines = f.readlines()

    records = [line.strip().split(", ") for line in lines]
    time_axis = generate_time_axis(start_time, end_time)[:21]  # ⛔️ 限制只輸出前 21 筆

    time_record_map = {r[0] + r[1].zfill(2): r for r in records}

    # PG_{model}_track_{date}.txt
    track_path = os.path.join(base_output_dir, f"PG_{model}_track_{date}.txt")
    with open(track_path, "w") as f:
        for i, t in enumerate(time_axis, start=1):
            r = time_record_map.get(t)
            if r:
                f.write(f"{r[3].strip()}\t{r[2].strip()}\t{i}\n")
            else:
                f.write(f"0\t0\t{i}\n")

    # PG_{model}_mslp_{date}.txt
    mslp_path = os.path.join(base_output_dir, f"PG_{model}_mslp_{date}.txt")
    with open(mslp_path, "w") as f:
        for t in time_axis:
            r = time_record_map.get(t)
            value = r[4].strip() if r else "0"
            f.write(f"{value}\n")

    # PG_{model}_maxwind_{date}.txt
    maxwind_path = os.path.join(base_output_dir, f"PG_{model}_maxwind_{date}.txt")
    with open(maxwind_path, "w") as f:
        for t in time_axis:
            r = time_record_map.get(t)
            try:
                kmh = float(r[5].strip()) if r else 0.0
                ms = kmh * 0.27778
                f.write(f"{ms:.2f}\n")
            except:
                f.write("0.00\n")

# === 🚀 主程式區 ===
for i in models_to_process:
    model = f"m{str(i).zfill(2)}"
    dat_file = os.path.join(
        output_root, date, wind_threshold, model, "CyTRACK_output",
        f"CyTRACK_WP_{start_time}-{end_time}_CUSTOM_TC.dat"
    )
    print(f"🔧 拆分並補齊 {model} ...")
    matched_models = {}
    unmatched_models = {}
    matched_txt, invalid_cases = split_and_select_case(dat_file, model, date, start_time, end_time)
    if matched_txt:
        txt_path = os.path.join(output_root, date, wind_threshold, model, matched_txt)
        matched_models[model] = txt_path
        generate_outputs(txt_path, model, date)
    else:
        unmatched_models[model] = invalid_cases

    for model, path in matched_models.items():
        rel_path = path.split("/CyTRACK_PG/")[-1]
        print(f"{model} -> {rel_path}")

    for model, cases in unmatched_models.items():
        print(f"{model}無符合的成員:")
        for name, coords in cases.items():
            print(f"{name} 的前三筆有效資料：")
            for lat, lon in coords:
                print(f"lat={lat}, lon={lon}")
            print()
