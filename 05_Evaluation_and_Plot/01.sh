#!/bin/sh
# ylc

MAINDIR=${PWD}
cd $MAINDIR
inputdir=inout
obs_txt="Mawar0528.txt"  # 原始觀測檔
start=2023052800 #格式是yyyymmddhh
date=20230528 #格式是yyyymmdd
mkdir -p $inputdir

empty_files=()

for i in $(seq -w 1 32); do
    mem=m${i}_newtrack_${date}_1005hPa
    file=${inputdir}/${mem}
    txtfile="${file}.txt"

    # 檢查是否為空檔案
    if [ ! -s "$txtfile" ]; then
        echo "⚠️ 空檔案：${mem}"
        empty_files+=("${mem}")
        continue
    fi

    echo ${mem}

    # 處理文件，準備成 .log
    awk '{print $1}' ${file}.txt > ${file}_1.log
    awk '{print $2}' ${file}.txt > ${file}_2.log
    paste ${file}_2.log ${file}_1.log > ${file}_3.log
    rm ${file}_1.log ${file}_2.log
    awk '{print $0,"0 0 0 0 0"}' ${file}_3.log > ${file}.log
    rm ${file}_3.log
    sed -i '1i  lat       lon       y         x         k       min SLP  max wind' ${file}.log

    # 偵測有幾行資料
    linecount=$(wc -l < "$obs_txt")
    log_lines=$(wc -l < "${file}.txt")

    if [ "$log_lines" -lt "$linecount" ]; then
        short_obs="${obs_txt%.txt}_${log_lines}.txt"
        head -n "$log_lines" "$obs_txt" > "$short_obs"
        current_obs="$short_obs"
        current_rowt="$log_lines"
    else
        current_obs="$obs_txt"
        current_rowt="$linecount"
    fi

    # 呼叫修正腳本並動態指定參數
    sh 02.sh "$file" "$current_obs" "$current_rowt" "$start"

    # 後處理
    awk '{print $14}' ${file} | awk '{for(i=0;++i<=NF;)a[i]=a[i]?a[i] FS $i:$i}END{for(i=0;i++<NF;)print a[i]}' >> ${inputdir}/total.log
done

for i in $(seq -w 1 32); do
    infile="./inout/m${i}_newtrack_${date}_1005hPa"
    outfile="./inout/${date}_m${i}_1005hPa_terror.txt"

    # 擷取每一行最後三個數值的第一個（也就是欄位 17）
    awk '{print $14}' "$infile" > "$outfile"

    echo "✅ 已建立 $outfile，共 $(wc -l < $outfile) 筆資料"
done

if [ ${#empty_files[@]} -gt 0 ]; then
    echo "🔍 以下是空檔案清單："
    for f in "${empty_files[@]}"; do
        echo "$f"
    done
else
    echo "✅ 所有檔案皆有資料"
fi
