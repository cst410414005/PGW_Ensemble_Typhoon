#!/bin/bash
## 由wrfinput
#!/bin/bash
#============================================================================
#input
args=$*
echo "=== RUN of $0 $* ============================================="
#--------
if [[ $1 == "-h" ]] || [[ $1 == "" ]] || [[ $1 == "-help" ]];then
  HELP(){
  echo "指哪打哪的ARWpost輸出"
  echo "TuKaIKata(v1.1):"
  echo "  ARWpost.sh [ifn] [ofd] [ofn] [tim1] [tim2] [tint]"
  echo "             [-V fields]"
  echo "             [-L levs]"
  echo "             [-m mercator_defs]"
  echo "          ifn = wrfout/wrfinput的絕對路徑"
  echo "          ofd = 輸出的絕對路徑 or 相對路徑"
  echo "          ofn = 輸出的檔案名稱"
  echo "         tim1 = start_date       in namelist.ARWpost"
  echo "         tim2 = end_date         in namelist.ARWpost"
  echo "         tint = interval_seconds in namelist.ARWpost"
  echo "        files = fields           in namelist.ARWpost"
  echo "         levs = levs             in namelist.ARWpost"
  echo " mercator_defs= mercator_defs    in namelist.ARWpost(de=.false.)"
  echo ""
  echo "  ex: "
  echo "   ARWpost.sh /work/run/wrfout_d01 /work/ARWOUT d01 2024-07-20_00:00:00 2024-07-20_00:00:00 3600"
  exit
  }
  HELP
  exit
fi
#--------
#預設參數
#輸出變數場
files="U,V,W,PSFC,T2,Q2,U10,V10,umet,vmet,height,T,QVAPOR,u10m,v10m"
#fields='tc,U,V,W,U10,V10,PSFC,SST,geopt,slp,HGT,QVAPOR,pressure,dbz,rh,f,theta,LANDMASK,TSLB,LH,OLR,TSK,RAINC,RAINNC,GRDFLX,HFX,QFX'
#輸出氣壓層
levs="1000,850,500"
mercator_defs=".false."  #麥卡托嗎?


#必要參數
i=1
  ifn=`echo ${args} | awk '{ print $'$i' }'` ; i=$((i+1)) #input  name
  ofd=`echo ${args} | awk '{ print $'$i' }'` ; i=$((i+1)) #output dir
  ofn=`echo ${args} | awk '{ print $'$i' }'` ; i=$((i+1)) #output name
 tim1=`echo ${args} | awk '{ print $'$i' }'` ; i=$((i+1)) #ex: 2020-05-20_12:00:00
 tim2=`echo ${args} | awk '{ print $'$i' }'` ; i=$((i+1)) #ex: 2020-05-20_12:00:00
 tint=`echo ${args} | awk '{ print $'$i' }'` ; i=$((i+1)) #ex :21600

#選用參數
 arg="dummy"
  while [[ $arg != "" ]] ; do
  arg=`echo ${args} | awk '{ print $'$i' }'`
  i=$((i+1))
  if [[ $arg = -V ]] ;then  files=`echo ${args} | awk '{ print $'$i' }'`; i=$((i+1)); fi
  if [[ $arg = -L ]] ;then   levs=`echo ${args} | awk '{ print $'$i' }'`; i=$((i+1)); fi
  if [[ $arg = -m ]] ;then mercator_defs=`echo ${args} | awk '{ print $'$i' }'`; i=$((i+1)); fi
  done

  interp_method=1
  ARexe="/work1/tgeo/ensemble/2024-0108-PGen/02-PG-ens-IC/ifn1/ARWpost/ARWpost.exe"      #exe原始路徑  @MCS

#--------------------------------------
#檢查哨
pwdd=`pwd`
if [[ ${tim1} == "" ]] ;then
  echo "!!! You did not input tim1 ...exit... !!!"
  exit
fi
if [[ ${tim2} == "" ]] ;then
  tim2=${tim1}
fi
if [[ ${tint} == "" ]] ;then
  tint=21600
fi
#--------------------------------------

#================================================
#---   main run  ----------------------
mkdir -p ${ofd}
cd ${ofd}
#--------------------------------------
rm -f namelist.ARWpost
cat > namelist.ARWpost << EOF
&datetime
 start_date = '${tim1}',
 end_date   = '${tim2}',
 interval_seconds = ${tint},
/

&io
 input_root_name = '${ifn}'
 output_root_name = './${ofn}'
 plot = 'list'
 fields = '${files}'
 fields_file = 'myLIST'
 output_type = 'grads'
 mercator_defs = ${mercator_defs}
/
 split_output = .true.
 frames_per_outfile = 1

&interp
 extrapolate = .ture.
 interp_method = ${interp_method},
 interp_levels = ${levs}
/
EOF
#--------------------------------------
${ARexe}    #執行.exe
# rm namelist.ARWpost
#-----  main run end  -----------------

echo "ofn1=${ofd}/${ofn}.ctl"
echo "ofn2=${ofd}/${ofn}.dat"
#================================================
#=======================================================================
echo "=== RUN of $0 $* ============================================="

