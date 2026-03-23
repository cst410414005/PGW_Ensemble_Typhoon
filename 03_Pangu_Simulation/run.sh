python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements_cpu.txt

python bin2npy_as.py

cd /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/input_data

ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m01_input_surface_from_bin.npy ./m01_input_surface.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m01_input_upper_from_bin.npy ./m01_input_upper.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m02_input_surface_from_bin.npy ./m02_input_surface.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m02_input_upper_from_bin.npy ./m02_input_upper.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m03_input_surface_from_bin.npy ./m03_input_surface.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m03_input_upper_from_bin.npy ./m03_input_upper.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m04_input_surface_from_bin.npy ./m04_input_surface.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m04_input_upper_from_bin.npy ./m04_input_upper.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m05_input_surface_from_bin.npy ./m05_input_surface.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m05_input_upper_from_bin.npy ./m05_input_upper.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m06_input_surface_from_bin.npy ./m06_input_surface.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m06_input_upper_from_bin.npy ./m06_input_upper.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m07_input_surface_from_bin.npy ./m07_input_surface.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m07_input_upper_from_bin.npy ./m07_input_upper.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m08_input_surface_from_bin.npy ./m08_input_surface.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m08_input_upper_from_bin.npy ./m08_input_upper.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m09_input_surface_from_bin.npy ./m09_input_surface.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m09_input_upper_from_bin.npy ./m09_input_upper.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m10_input_surface_from_bin.npy ./m10_input_surface.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m10_input_upper_from_bin.npy ./m10_input_upper.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m11_input_surface_from_bin.npy ./m11_input_surface.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m11_input_upper_from_bin.npy ./m11_input_upper.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m12_input_surface_from_bin.npy ./m12_input_surface.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m12_input_upper_from_bin.npy ./m12_input_upper.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m13_input_surface_from_bin.npy ./m13_input_surface.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m13_input_upper_from_bin.npy ./m13_input_upper.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m14_input_surface_from_bin.npy ./m14_input_surface.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m14_input_upper_from_bin.npy ./m14_input_upper.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m15_input_surface_from_bin.npy ./m15_input_surface.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m15_input_upper_from_bin.npy ./m15_input_upper.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m16_input_surface_from_bin.npy ./m16_input_surface.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m16_input_upper_from_bin.npy ./m16_input_upper.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m17_input_surface_from_bin.npy ./m17_input_surface.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m17_input_upper_from_bin.npy ./m17_input_upper.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m18_input_surface_from_bin.npy ./m18_input_surface.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m18_input_upper_from_bin.npy ./m18_input_upper.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m19_input_surface_from_bin.npy ./m19_input_surface.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m19_input_upper_from_bin.npy ./m19_input_upper.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m20_input_surface_from_bin.npy ./m20_input_surface.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m20_input_upper_from_bin.npy ./m20_input_upper.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m21_input_surface_from_bin.npy ./m21_input_surface.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m21_input_upper_from_bin.npy ./m21_input_upper.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m22_input_surface_from_bin.npy ./m22_input_surface.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m22_input_upper_from_bin.npy ./m22_input_upper.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m23_input_surface_from_bin.npy ./m23_input_surface.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m23_input_upper_from_bin.npy ./m23_input_upper.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m24_input_surface_from_bin.npy ./m24_input_surface.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m24_input_upper_from_bin.npy ./m24_input_upper.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m25_input_surface_from_bin.npy ./m25_input_surface.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m25_input_upper_from_bin.npy ./m25_input_upper.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m26_input_surface_from_bin.npy ./m26_input_surface.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m26_input_upper_from_bin.npy ./m26_input_upper.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m27_input_surface_from_bin.npy ./m27_input_surface.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m27_input_upper_from_bin.npy ./m27_input_upper.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m28_input_surface_from_bin.npy ./m28_input_surface.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m28_input_upper_from_bin.npy ./m28_input_upper.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m29_input_surface_from_bin.npy ./m29_input_surface.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m29_input_upper_from_bin.npy ./m29_input_upper.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m30_input_surface_from_bin.npy ./m30_input_surface.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m30_input_upper_from_bin.npy ./m30_input_upper.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m31_input_surface_from_bin.npy ./m31_input_surface.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m31_input_upper_from_bin.npy ./m31_input_upper.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m32_input_surface_from_bin.npy ./m32_input_surface.npy
ln -sf /home/cst/AI_global_forecast_model_for_education/Pangu-Weather-for-copy/data-input/asia/m32_input_upper_from_bin.npy ./m32_input_upper.npy

cd ..

echo "開始跑盤古"

python inference.py

echo "開始轉檔"

Ts=(`seq 0 20`)
As=("surface upper")
for A in ${As[*]}; do
for T in ${Ts[*]}; do
python3.9 PGout2bin1.py ${A} ${T}
done
done
