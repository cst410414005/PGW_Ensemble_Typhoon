echo "Part1開始"

#date格式=yyyymmddhh，記得hh!
date=2023072912
#file格式=mmdd
file=072912

/work1/tgeo/ensemble/2024-0108-PGen/01-WRF-RANDOM-ens-IC/01.sh "$date" "$file"

echo "Part1結束"

echo "Part2開始"

/work1/tgeo/ensemble/2024-0108-PGen/02-PG-ens-IC/02.sh "$date" "$file"

echo "Part2結束"

echo "去JET囉 σ'∀')σ"
