time=20230528
output="terror_Ens_1005hPa_${time}.txt"
> "$output"  # 清空舊檔或初始化
empty_files=()

threshold=1600

for i in $(seq -w 1 32); do
    infile="${time}_m${i}_1005hPa_terror.txt"
    if [ ! -s "$infile" ]; then
	    echo "⚠️ 空檔案：m${i}_1005hPa"
	    empty_files+=("m${i}_1005hPa")
	    continue
    fi

    timestep=0
    while IFS= read -r val; do
	if awk "BEGIN {exit !($val <= $threshold)}"; then
        	echo -e "${timestep}\t${val}" >> "$output"
	fi
        timestep=$((timestep + 6))
    done < "$infile"
done

echo "✅ 已完成合併成 $output（總行數 $(wc -l < $output) ）"

if [ ${#empty_files[@]} -gt 0 ]; then
    echo "📂 以下是空檔案（未合併）："
    for f in "${empty_files[@]}"; do
        echo "$f"
    done
else
    echo "🎉 所有檔案皆有資料，無缺漏"
fi


