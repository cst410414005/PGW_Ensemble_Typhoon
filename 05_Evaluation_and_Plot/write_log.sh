#!/bin/sh
#ylc

MAINDIR=${PWD}
cd $MAINDIR

inputdir=inout

if [ ! -e $MAINDIR/$inputdir/ ];then
	mkdir $inputdir/
fi

for mem in PG_newtrack_20241112 ;do
  file=${inputdir}/${mem}
  line1=" lat       lon       y         x         k       min SLP  max wind"
  echo ${mem} 

  awk '{print $1}' ${file}.txt > ${file}_1.log
  awk '{print $2}' ${file}.txt > ${file}_2.log
  paste ${file}_2.log ${file}_1.log > ${file}_3.log
  rm ${file}_2.log ${file}_1.log
  awk '{print $0,"0 0 0 0 0"}' ${file}_3.log > ${file}.log
  rm ${file}_3.log 
  sed -i '1i  lat       lon       y         x         k       min SLP  max wind' ${file}.log
  sh 01-run-Fix_and_Dat.gs.sh ${file}
  awk '{print $14}' ${file}| awk '{for(i=0;++i<=NF;)a[i]=a[i]?a[i] FS $i:$i}END{for(i=0;i++<NF;)print a[i]}' >> ${inputdir}/total.log

done
