#!/bin/sh
#ylc
#
#./run-FixTYLog.gs.sh
################################################################
obs_txt="Usagi1112.txt" #input  觀測
sim_log=/jet/tgeo/output_data-bin/terror/$1.log  #input  RIP找出來的路徑
#sim_log=/jet/tgeo/output_data-bin/terror/PG_track_0720.log
fix_txt="$1"                   #output
#fix_txt="PG_track_0720"
start=2024111200               #模擬初始時間
rowt=19                        #有幾行
int_t=6                        #.log檔裡的時間間距


set -x
grads -bcl "FixTYLog.gs ${obs_txt} ${sim_log} ${fix_txt} ${start} ${rowt} ${int_t} -q 1"
set +x
