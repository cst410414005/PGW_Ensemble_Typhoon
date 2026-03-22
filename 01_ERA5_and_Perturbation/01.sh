#date格式=yyyymmddhh，記得hh!
date=2023072912
#file格式=mmdd
file=072912

mkdir -p /work1/tgeo/ensemble/2024-0108-PGen/01-WRF-RANDOM-ens-IC/ana/${file}
cp /work1/tgeo/data-ERA5/23${file}.* /work1/tgeo/ensemble/2024-0108-PGen/01-WRF-RANDOM-ens-IC/ana/${file}

shwps="/work1/tgeo/ensemble/2024-0108-PGen/00.s/RUN-WPS+real/01-WPS_412_ERA5.sh"
${shwps} ${date} ${date} #WPS

shrel="/work1/tgeo/ensemble/2024-0108-PGen/00.s/RUN-WPS+real/02-WRF_412_real.sh"
Es=32 
${shrel} ${date} ${date} 1 ${date} ${Es} wrfinput_d01

cp /work1/tgeo/ensemble/2024-0108-PGen/01-WRF-RANDOM-ens-IC/${file}/WRF/wrfinput_d01 /work1/tgeo/ensemble/2024-0108-PGen/01-WRF-RANDOM-ens-IC/${file}/wrfinput
mv /work1/tgeo/ensemble/2024-0108-PGen/01-WRF-RANDOM-ens-IC/${file}/wrfinput/wrfinput_d01 /work1/tgeo/ensemble/2024-0108-PGen/01-WRF-RANDOM-ens-IC/${file}/wrfinput/m00_wrfinput_d01
