import os
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from scipy.stats import ttest_ind

# 所有參數組合
cases = ['Usagi', 'Kongrey', 'Krathon', 'Gaemi', 'Koinu', 'Haikui']
case_dates = {
    'Usagi': ['1112', '111212', '1113', '111312', '1114'],
    'Kongrey': ['1027', '102712', '1028', '102812', '1029'],
    'Krathon': ['0928', '092812', '092912', '0930'],
    'Gaemi': ['0720', '072012', '0721', '072112', '0722'],
    'Koinu': ['1001', '100112', '1002', '100212', '1003'],
    'Haikui': ['082912', '0830', '083012', '0831', '083112'],
    'Saola': ['0826', '082612', '0827', '082712', '0828'],
}
tests = ['scc', 'rmse', '']  # 空字串代表 ave
names = ['z', 't', 'q', 'u', 'v']
aas = ['200', '500', '850']  # 排序順序改為 200→500→850
E_range = [f"{i:02d}" for i in range(1, 33)]

# 📦 函式：畫出一張大圖（15 張子圖）
def draw_big_boxplot(all_dates, all_cases, test_prefix, title, filename):
    fig, axes = plt.subplots(nrows=3, ncols=5, figsize=(22, 14))
    plt.tight_layout(rect=[0, 0, 1, 0.97])
    for i, aa in enumerate(aas):  # 以高度層級為主軸
        for j, name in enumerate(names):
            red_data = [[] for _ in range(5)]
            blue_data = [[] for _ in range(5)]

            # 🔴 原始 ensemble 資料
            for case in all_cases:
                for date in all_dates[case]:
                    for E in E_range:
                        prefix = f"{test_prefix}_" if test_prefix else ""
                        filepath = f"{case}/{date}/{prefix}ave{name}{aa}_{date}_m{E}.txt"
                        if not os.path.exists(filepath):
                            continue
                        with open(filepath, 'r') as f:
                            lines = f.readlines()
                            values = [float(line.strip()) for line in lines if line.strip()]
                            if len(values) >= 21:
                                for d in range(5):
                                    red_data[d].append(values[d * 4 + 1 : d * 4 + 5])

            # 🔵 新資料夾資料（無 E 編號）
            for case in all_cases:
                for date in all_dates[case]:
                    prefix = f"{test_prefix}_" if test_prefix else ""
                    filepath = f"../PG_bin/{prefix}ave{name}{aa}_{date}.txt"
                    if not os.path.exists(filepath):
                        continue
                    with open(filepath, 'r') as f:
                        lines = f.readlines()
                        values = [float(line.strip()) for line in lines if line.strip()]
                        if len(values) >= 21:
                            for d in range(5):
                                blue_data[d].append(values[d * 4 + 1 : d * 4 + 5])

            red_flat = [sum(day, []) for day in red_data]
            blue_flat = [sum(day, []) for day in blue_data]

            ax = axes[i][j]
            if any(red_flat):
                ax.boxplot(
                    red_flat,
                    positions=[x + 0.2 for x in range(5)],
                    widths=0.35,
                    patch_artist=True,
                    boxprops=dict(facecolor='none', color='darkred'),
                    flierprops=dict(marker='o', markerfacecolor='none', markeredgecolor='darkred'),
                    medianprops=dict(color='darkred'),
                    whiskerprops=dict(color='darkred'),
                    capprops=dict(color='darkred')
                )
            if any(blue_flat):
                ax.boxplot(
                    blue_flat,
                    positions=[x - 0.2 for x in range(5)],
                    widths=0.35,
                    patch_artist=True,
                    boxprops=dict(facecolor='none', color='darkblue'),
                    flierprops=dict(marker='o', markerfacecolor='none', markeredgecolor='darkblue'),
                    medianprops=dict(color='darkblue'),
                    whiskerprops=dict(color='darkblue'),
                    capprops=dict(color='darkblue')
                )
            
            xtick_labels = []
            for d in range(5):
                r = red_flat[d]
                b = blue_flat[d]
                label = f"day{d+1}"
                if r and b:
                    stat, p = ttest_ind(r, b, equal_var=False)
                    if p < 0.05:
                        label += "**"
                    elif p < 0.1:
                        label += "*"
                xtick_labels.append(label)

            line_y = 1 if test_prefix == 'scc' else 0
            ax.axhline(line_y, color='gray', linestyle='--', linewidth=1)
            ax.set_xlim(-0.5, 4.5)
            ax.set_xticks(range(5))
            ax.set_xticklabels(xtick_labels)
            ax.set_title(f"{name}{aa}")
            
# 🔍 加入圖例（右上角）
    legend_elements = [
        Patch(facecolor='none', edgecolor='darkblue', label='Ctrl'),
        Patch(facecolor='none', edgecolor='darkred', label='Ens')
    ]
    fig.legend(handles=legend_elements, loc='upper right', fontsize=14)

    plt.tight_layout(rect=[0, 0, 1, 0.97])
    plt.savefig(filename, dpi=300)
    print(f"✅ 圖已儲存為 {filename}")

# 🔄 產生所有圖（3 類型 × 1 綜合 + 3 類型 × 3 case = 12 張）
for test_prefix in ['scc', 'rmse', '']:
    label = test_prefix or 'ave'
    draw_big_boxplot(case_dates, cases, test_prefix, f"All Cases - {label}", f"boxplot_all_{label}.png")

    for case in cases:
        draw_big_boxplot({case: case_dates[case]}, [case], test_prefix, f"{case} - {label}", f"boxplot_{case}_{label}.png")
