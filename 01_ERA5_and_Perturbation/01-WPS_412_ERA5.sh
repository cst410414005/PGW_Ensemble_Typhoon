#!/bin/bash
#for WRF WPS, ERA5 data be used
#./01-WPS_412_ERA5.sh $time_1 $time_2
##############################
pwdd=$PWD
MAINDIR=${pwdd}
#WPSOUT is the WPS runing dir 
WPSOUT=/work1/tgeo/ensemble/2024-0108-PGen/01-WRF-RANDOM-ens-IC/072912/WPS
#WPSMODEL is the WPS program dir setting in system (don't change) 
WPSMODEL=/work1/rtwrf/WRFV412/WPS
#ECDIR is the ana data dir (user need to edit)
ECDIR=/work1/tgeo/ensemble/2024-0108-PGen/01-WRF-RANDOM-ens-IC/ana/072912
I=0
interval_seconds=21600

I=0
 for D in $1 $2
 do 
 I=$(($I+1))
 YY[$I]=`echo $D | cut -c1-4`
 MM[$I]=`echo $D | cut -c5-6`
 DD[$I]=`echo $D | cut -c7-8`
 HH[$I]=`echo $D | cut -c9-10` 
 done

ND=1

if [ ! -e ${WPSOUT} ];then
 mkdir -p ${WPSOUT}
fi

cd $WPSOUT
rm -rf * 

#link file: link_grib.csh Vtable geogrid.exe ungrib.exe metgrid.exe GEOGRID.TBL METGRID.TBL plotgrids.exe
ln -sf ${WPSMODEL}/geogrid.exe ./
ln -sf ${WPSMODEL}/geogrid/GEOGRID.TBL ./
ln -sf ${WPSMODEL}/link_grib.csh ./
ln -sf ${WPSMODEL}/metgrid.exe ./
ln -sf ${WPSMODEL}/metgrid/METGRID.TBL ./
ln -sf ${WPSMODEL}/ungrib.exe ./
ln -sf ${WPSMODEL}/ungrib/Variable_Tables/Vtable.ERA-interim.pl ./Vtable


# ECDIR PATH, IF PATH OR FILENAME DIFFERENT, user need to edit
./link_grib.csh $ECDIR/*pre*.grib
cat > namelist.wps << NLEOF
&share
 wrf_core = 'ARW',
 max_dom = $ND,
 start_date = '${YY[1]}-${MM[1]}-${DD[1]}_${HH[1]}:00:00', 
 end_date   = '${YY[2]}-${MM[2]}-${DD[2]}_${HH[2]}:00:00', 
 interval_seconds = ${interval_seconds},
 io_form_geogrid = 2,
 opt_output_from_geogrid_path = '$WPSOUT/',
 debug_level = 0,
/

&geogrid
 parent_id         = 1,
 parent_grid_ratio =  1,
 i_parent_start    = 1,
 j_parent_start    = 1,
 e_we          = 720
 e_sn          = 361
 geog_data_res = 'default'
 map_proj =  'mercator',
 dx = 27000
 dy = 27000
 truelat1 = 23.0
 ref_lat = 23.0
 ref_lon = 120.0
 geog_data_path = '/work1/rtwrf/geog',
 opt_geogrid_tbl_path = '${WPSOUT}',
/


&ungrib
 out_format = 'WPS',
 prefix = 'PRE',

&metgrid
 fg_name = 'PRE','SUR',
 io_form_metgrid = 2,
 opt_output_from_metgrid_path = '${WPSOUT}',
 opt_metgrid_tbl_path = '${WPSOUT}',
/

&mod_levs
 press_pa = 201300 , 200100 , 100000 ,
             95000 ,  90000 ,
             85000 ,  80000 ,
             75000 ,  70000 ,
             65000 ,  60000 ,
             55000 ,  50000 ,
             45000 ,  40000 ,
             35000 ,  30000 ,
             25000 ,  20000 ,
             15000 ,  10000 ,
              5000 ,   1000
 /
NLEOF

#
# RUN WPS
#
#####PRE#####
  ./geogrid.exe
  ./ungrib.exe
  cp namelist.wps namelist.wps.pre
#####SUR#####
  rm Vtable
  cp ${WPSMODEL}/ungrib/Variable_Tables/Vtable.ERA-interim.ml ./Vtable
  iss=`cat namelist.wps | nl -b a | grep 'prefix =' | awk '{print $1}'`
  sed -i ${iss}s/PRE/SUR/g namelist.wps
  rm GRIBFILE.A*
  ./link_grib.csh $ECDIR/*sur*.grib
  ./ungrib.exe
  cp namelist.wps namelist.wps.sur
#####metgrid#####
  ./metgrid.exe
