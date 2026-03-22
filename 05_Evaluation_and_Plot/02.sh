#!/bin/sh

sim_log=/jet/tgeo/output_data-bin/terror/$1.log
fix_txt="$1"
obs_txt="$2"
rowt="$3"
start="$4"
int_t=6

set -x
grads -bcl "FixTYLog.gs ${obs_txt} ${sim_log} ${fix_txt} ${start} ${rowt} ${int_t} -q 1"
set +x
