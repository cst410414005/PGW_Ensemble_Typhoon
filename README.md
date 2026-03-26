# 🌀 PGW_Ensemble_Typhoon
**盤古天氣模型之熱帶氣旋系集預報系統 (Ensemble Forecasting for Tropical Cyclones based on Pangu-Weather)**

本專案結合數值模式製作擾動的方式與人工智慧氣象模式，建構一套適合西北太平洋熱帶氣旋系集預報模式。

## 🛠️ 核心工作與主要使用工具
* 資料處理與視覺化：Python (`xarray`, `netCDF4`, `pandas`, `matplotlib`, `cartopy`)
* 氣旋追蹤與定位：CyTRACK
* 氣象模式與同化：WRF (WPS, real), WRFDA (Random CV)
* 系統環境與自動化：Linux 終端機環境, Bash Shell Scripting, GrADS

## 📂 專案架構 

本專案的資料夾與程式碼結構按照工作流程步驟進行劃分：

```text
PGW_Ensemble_Typhoon/
├── 01_ERA5_and_Perturbation/   # 獲得ERA5初始場與生成WRFDA隨機擾動
├── 02_IC_Synthesis/            # 擷取並合成擾動場與ERA5環境場成盤古模式初始場 (.gs)
├── 03_Pangu_Simulation/        # 格式轉換與批次運作Pangu-Weather模式 (.py, .sh)
├── 04_CyTRACK_Analysis/        # CyTRACK 客觀氣旋追蹤與特徵擷取 (.py)
├── 05_Evaluation_and_Plot/     # 誤差對齊、統計檢定與視覺化圖表產出 (.sh, .py, .gs)
└── README.md
```

## ⚙️ 工作流程 
Step 1: 下載初始場與生成擾動 (01_ERA5_and_Perturbation)  
透過API自動化下載ERA5氣壓層與地面層資料，並轉換為GrADS可讀取格式。利用WRFDA的RandomCV結合特定隨機種子(seed)，將每個初始場產出32組隨機擾動場。

Step 2: 合成系集成員初始場 (02_IC_Synthesis)  
擷取1/4地球的擾動範圍疊加至ERA5再分析環境場，則為提供給盤古模式進行預報所需之初始檔。

Step 3: 運作盤古模式 (03_Pangu_Simulation)  
執行跨架構資料轉換 (.bin to .npy)，於獨立環境中執行Pangu-Weather CPU模式，批次產出32個系集成員的120小時之預報。

Step 4: 追蹤氣旋 (04_CyTRACK_Analysis)  
轉換網格資料為NetCDF4格式，運用CyTRACK演算法與濾波，鎖定並擷取各系集成員之軌跡及氣旋詳細數據。

Step 5: 計算誤差與統計視覺化 (05_Evaluation_and_Plot)  
對齊資料與觀測之時間序列，並過濾極端離群值，以量化路徑與強度(MSLP/最大風速)誤差。執行獨立樣本t檢定(T-test)評估差異顯著性，自動繪製誤差盒鬚圖與系集路徑圖。

## 📖 致謝與引用 
**本專案致力於資料前處理、結合擾動與再分析資料、批次進行盤古系集與統計視覺化，盤古模式與Cytrack均受惠於學術界的卓越貢獻。**

**Pangu-Weather (盤古天氣模式)**：  
來自華為雲 (Huawei Cloud) 團隊發表於《Nature》之研究：  
Bi, K., Xie, L., Zhang, H., Chen, X., Gu, X., & Tian, Q. (2023). Accurate medium-range global weather forecasting with 3D neural networks. Nature, 619, 533–538. https://doi.org/10.1038/s41586-023-06185-3  
GitHub Repository: https://github.com/198808xc/Pangu-Weather

**Pangu-Weather Inference Implementation (環境設定與實作)**：  
本專案之盤古模式的CPU運作環境，參考並改寫自以下教學專案（基於198808xc之精簡版架構）：  
GitHub Repository: https://github.com/yungyun0721/AI_global_forecast_model_for_education

**CyTRACK (氣旋追蹤工具)**：  
本專案之熱帶氣旋定位與擷取氣旋強度特徵，採用EphysLab團隊開發之Python工具箱 CyTRACK：  
Pérez-Alarcón, A., Coll-Hidalgo, P., Trigo, R. M., Nieto, R., & Gimeno, L. (2024). CyTRACK: An open-source and user-friendly python toolbox for detecting and tracking cyclones. Environmental Modelling & Software, 176, 106027. https://doi.org/10.1016/j.envsoft.2024.106027  
GitHub Repository: https://github.com/apalarcon/CyTRACK
