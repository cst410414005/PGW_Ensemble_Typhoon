print("""\
01      天兔            Usagi           24111200-24111400 0
02      康芮            Kongrey         24102700-24102900 28 30 32 34 36
03      山陀兒          Krathon         24092800-24093000 32 34 36 38 40
04      凱米            Gaemi           24072000-24072200 0
05      小犬            Koinu           23100100-23100300 0
06      海葵            Haikui          23082912-23083112 38 40 42 44 46
07      蘇拉            Saola           23082600-23082800 24 26 28 30 32
08      卡努            Khanun          23072912-23073112 38 40 42 44 46
09      杜蘇芮          Doksuri         23072212-24072412 10 12 14 16 18
10      瑪娃            Mawar           23052600-23052800 24 26 28 30 32
""")

case = input("請輸入 case 名稱（如上）：").strip()
IC_date = input("請輸入 IC_date（格式 yyyymmdd）：").strip()
skip_lines = int(input("請輸入要跳過的前幾列："))

output_folder = "."

for var_type in ["mslp", "maxwind"]:
    if var_type == "mslp":
        kongrey_file = f"{case}_mslp.txt"
        file_prefix = "newmslp"
        output_prefix = "mslp"
    else:  # maxwind
        kongrey_file = f"{case}_wind.txt"
        file_prefix = "newmax"
        output_prefix = "maxwind"

    for i in range(1, 33):
        model = f"m{str(i).zfill(2)}"
        model_file = f"{model}_{file_prefix}_{IC_date}_1005hPa.txt"
        output_file = f"{output_folder}/{output_prefix}_{IC_date}_{model}_1005hPa.txt"

        try:
            with open(model_file, "r", encoding="utf-8") as f:
                model_vals = [float(line.strip()) for line in f if line.strip()]
            N = len(model_vals)

            with open(kongrey_file, "r", encoding="utf-8") as f:
                kongrey_all = [float(line.strip()) for line in f if line.strip()]
            if skip_lines + N > len(kongrey_all):
                print(f"⚠️ {model_file} 要求的第 {skip_lines+1} 到第 {skip_lines+N} 列超出 {kongrey_file} 總列數 {len(kongrey_all)}，跳過")
                continue

            kongrey_segment = kongrey_all[skip_lines:skip_lines + N]
            result = [(round(k - m, 2) if k != 0 else -999.99) for k, m in zip(model_vals, kongrey_segment)]

            with open(output_file, "w", encoding="utf-8") as f:
                for val in result:
                    f.write(f"{val:.2f}\n")

            print(f"✅ [{var_type}] 已輸出差值結果至 {output_file}（共 {N} 筆）")

        except FileNotFoundError as e:
            print(f"🚫 找不到檔案：{e.filename}，跳過")
        except ValueError:
            print(f"🚫 資料格式錯誤，檢查 {kongrey_file} 或 {model_file} 是否有非數值內容")
