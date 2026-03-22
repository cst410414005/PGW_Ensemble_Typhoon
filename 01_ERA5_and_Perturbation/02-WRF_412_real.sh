#!/bin/bash
#
####################################################################
echo "=== bash $0 $*  ==="
####################################################################
MAINDIR=${PWD}

INIDATE=$1
ENDDATE=$2
ND=$3
seedarray1=$4
Es=$5
ofn=$6
MPH=7
CUP=2
PBL=1
SSP=1

YY[1]=`echo $INIDATE | cut -c1-4`
YY[2]=`echo $ENDDATE | cut -c1-4`
MM[1]=`echo $INIDATE | cut -c5-6`
MM[2]=`echo $ENDDATE | cut -c5-6`
DD[1]=`echo $INIDATE | cut -c7-8`
DD[2]=`echo $ENDDATE | cut -c7-8`
HH[1]=`echo $INIDATE | cut -c9-10`
HH[2]=`echo $ENDDATE | cut -c9-10`
 
WRFMODEL=/work1/rtwrf/WRFV412/WRF
DADIR=/work1/rtwrf/WRFV412/WRFDA
#where is your WPS oputdata (user need to edit) 
WPSOUT=/work1/tgeo/ensemble/2024-0108-PGen/01-WRF-RANDOM-ens-IC/072912/WPS
#Create WRF data dir (user need to edit)
MODELDIR=/work1/tgeo/ensemble/2024-0108-PGen/01-WRF-RANDOM-ens-IC/072912/0WRF
OUTPUTDIR=/work1/tgeo/ensemble/2024-0108-PGen/01-WRF-RANDOM-ens-IC/072912/wrfinput

echo " cp run dir ... ..."
if [ ! -e ${MODELDIR} ];then
mkdir -p ${MODELDIR}
fi
cd $MODELDIR
rm -rf * 
 for x in $(ls ${WRFMODEL}/run )
 do 
# ln -s ${WRFMODEL}/run/$x ./
cp ${WRFMODEL}/run/$x ./
 done

rm -rf $MODELDIR/namelist.input
ln -s $WPSOUT/met_em* ./

echo " cat namelist.input ... ..."
cat > namelist.input << NLEOF
 &time_control
 run_days                            = 0,
 run_hours                           = 72,
 run_minutes                         = 0,
 run_seconds                         = 0,
 start_year                          = ${YY[1]}, ${YY[1]}, ${YY[1]},
 start_month                         = ${MM[1]}, ${MM[1]}, ${MM[1]},
 start_day                           = ${DD[1]}, ${DD[1]}, ${DD[1]},
 start_hour                          = ${HH[1]}, ${HH[1]}, ${HH[1]},
 start_minute                        = 00, 00, 00,
 start_second                        = 00, 00, 00,
 end_year                            = ${YY[2]}, ${YY[2]}, ${YY[2]},
 end_month                           = ${MM[2]}, ${MM[2]}, ${MM[2]},
 end_day                             = ${DD[2]}, ${DD[2]}, ${DD[2]},
 end_hour                            = ${HH[2]}, ${HH[2]}, ${HH[2]},
 end_minute                          = 00, 00, 00,
 end_second                          = 00, 00, 00,
 interval_seconds                    = 21600
 input_from_file                     = .true.,.true.,.true.,
 history_interval                    = 180, 60, 60,
 frames_per_outfile                  = 1, 1, 1,
 restart                             = .false.,
 restart_interval                    = 1440,
 io_form_history                     = 2
 io_form_restart                     = 2
 io_form_input                       = 2
 io_form_boundary                    = 2
 debug_level                         = 0
 auxinput1_inname                    = "met_em.d<domain>.<date>"
 write_input                         = F
 inputout_interval                   = 360
 input_outname                       = "wrf_3dvar_input_d<domain>_<date>"
 inputout_begin_h                    = 6,  6,  6,
 inputout_end_h                      = 6,  6,  6,
 fine_input_stream                   = 0, 2, 2,
 io_form_auxinput2                   = 2
 /
auxinput4_inname                    = "wrflowinp_d<domain>"
auxinput4_interval                  = 1440
io_form_auxinput4                  = 2

 &domains
 time_step                           = 144,
 time_step_fract_num                 = 0,
 time_step_fract_den                 = 1,
 max_dom                             = $ND,
 s_we                                = 1,   1,   1,
 e_we                                = 720, 340, 250,
 s_sn                                = 1,   1,   1,
 e_sn                                = 361, 289, 301,
 s_vert                              = 1,  1,   1,
 e_vert                              = 14, 14, 14,
 num_metgrid_levels                  = 38
 num_metgrid_soil_levels 	     = 0
 dx                                  = 27000.0
 dy                                  = 27000.0
 grid_id                             = 1, 2, 3,    
 parent_id                           = 0, 1, 2,   
 i_parent_start                      = 1, 45, 197,
 j_parent_start                      = 1, 52, 124,   
 parent_grid_ratio                   = 1, 3, 3,   
 parent_time_step_ratio              = 1, 3, 3,
 feedback                            = 1,
 smooth_option                       = 2
 p_top_requested                     = 3000
 interp_type                         = 1
 lowest_lev_from_sfc                 = .false.
 lagrange_order                      = 1
 force_sfc_in_vinterp                = 1
 zap_close_levels                    = 500
 sfcp_to_sfcp                        = .false.
 adjust_heights                      = .false.
 eta_levels                          =  1.0, 0.925, 0.85, 0.7, 0.6, 0.5, 0.4, 0.3, 0.25, 0.2, 0.15, 0.1, 0.05, 0.0
/
 e_vert                              = 30, 30, 30,
 eta_levels                          =  1.0, 0.99092, 0.98164, 0.972151, 0.962442, 0.952498, 0.942305, 0.931849, 0.921115, 0.910091, 0.898762, 0.875117, 0.850019, 0.823269, 0.794612, 0.763726, 0.73021, 0.693544, 0.653023, 0.607629, 0.55571, 0.526456, 0.494271, 0.458332, 0.417468, 0.369911, 0.312655, 0.222059, 0.13515, 0.0

 &physics
 mp_physics                          = $MPH, $MPH, $MPH,
 ra_lw_physics                       = 1, 1, 1,  
 ra_sw_physics                       = 1, 1, 1,  
 radt                                = 27, 9, 3,  
 sf_sfclay_physics                   = $SSP, $SSP, $SSP,  
 sf_surface_physics                  = 1, 1, 1,  
 bl_pbl_physics                      = $PBL, $PBL, $PBL,
 bldt                                = 0, 0, 0,  
 cu_physics                          = $CUP, $CUP, 0,
 cudt                                = 0, 0, 0,   
 isfflx                              = 1,
 ifsnow                              = 0,
 icloud                              = 1,
 surface_input_source                = 1,
 num_soil_layers                     = 5,
 num_land_cat                        = 21,
 sf_urban_physics                    = 0,
 mp_zero_out                         = 0,
 maxiens                             = 1,
 maxens                              = 3,
 maxens2                             = 3,
 maxens3                             = 16,
 ensdim                              = 144,
 /
 sst_update                          = 1,

 &fdda
 /

 &dynamics
 w_damping                           = 1,
 diff_opt                            = 1,1,1
 km_opt                              = 4,4,4
 diff_6th_opt                        = 0,
 diff_6th_factor                     = 0.12,
 damp_opt                            = 0,
 base_temp                           = 290.
 zdamp                               = 5000.,  5000.,  5000.,
 dampcoef                            = 0.01,   0.01,   0.01,
 khdif                               = 0,      0,      0,
 kvdif                               = 0,      0,      0,
 non_hydrostatic                     = .true., .true., .true.,
 moist_adv_opt                       = 0,      0,      0,
 scalar_adv_opt                      = 0,      0,      0,
 iso_temp                            = 0.,
 /

 &bdy_control
 spec_bdy_width                      = 5,
 spec_zone                           = 1,
 relax_zone                          = 4,
 specified                           = .true., .false.,.false.,
 nested                              = .false., .true., .true.,
 /

 &grib2
 /

 &namelist_quilt
 nio_tasks_per_group = 0,
 nio_groups = 1,
 /

 &wrfvar5
 put_rand_seed = .true.,
 /

 &wrfvar7
 cv_options            =3,
 as1                   =0.25,1.0,1.5,
 as2                   =0.25,1.0,1.5,
 as3                   =0.25,1.0,1.5,
 as4                   =0.25,1.0,1.5,
 as5                   =0.25,1.0,1.5,
 /

 
 &wrfvar11
 seed_array1=${seedarray1}
 seed_array2=<seed_array2>
 /

 &wrfvar17
 analysis_type ="RANDOMCV",
 /

 &wrfvar18
 analysis_date="${YY[1]}-${MM[1]}-${DD[1]}_${HH[1]}:00:00.0000",
 /


NLEOF

#
# RUN WRF
#

rm -rf pbs.deck

cat > pbs_real.deck <<REALEOF
#!/bin/bash
#PBS -N REALN381-$INIDATE
#PBS -e real.err
#PBS -o real.log
#PBS -q wrf
#PBS -l nodes=1:ppn=24
##

module purge
module load pgi_poe/auto lib/netcdf/4.3.2/pgi_14/x86_64
export LD_LIBRARY_PATH=/aracbox/mpi/openmpi/1.8.4/pgi_14/x86_64/lib:/aracbox/lib/netcdf/4.3.2/pgi_14/x86_64/lib:/aracbox/pgi/Compiler/linux86-64/14.10/lib:/opt/libpng-1.6.18/lib

ulimit -s unlimited

cd $MODELDIR
/aracbox/mpi/openmpi/1.8.4/pgi_14/x86_64/bin/mpiexec ./real.exe
exit
REALEOF

##run qsub
#qsub pbs_real.deck

echo " run real ... ..."
cd $MODELDIR
./real.exe
#cat > WRF_real_check_file.dat << EOF
#  WRF_real was complete.
#EOF

echo " run WRF DA ... ..."

 cd $MODELDIR
 mv LANDUSE.TBL LANDUSE.TBL.WRF
 ln -sf  ${DADIR}/var/run/be.dat.cv3 ./be.dat
 ln -sf  ${DADIR}/run/LANDUSE.TBL ./LANDUSE.TBL
 cp -L  ${DADIR}/var/build/da_wrfvar.exe ./da_wrfvar.exe
 cp -L  ./wrfinput_d01 ./fg
 mv namelist.input namelist.input.real
 cp /work1/tgeo/ensemble/2024-0108-PGen/01-WRF-RANDOM-ens-IC/ob.ascii .  #不參與計算，只需要檔案而已
 mkdir -p ${OUTPUTDIR}

 EEs=`seq -f "%02g" 1 ${Es}`
 for E in ${EEs} ;do
   echo " -- E= "${E}
   cd $MODELDIR
   rm -rf wrfvar_output namelist.input
   cp namelist.input.real namelist.input
 # seedarray2=$((10#$E*900000))
   seedarray2=$E
   sed -i 's/<seed_array2>/'${seedarray2}'/' namelist.input
   ./da_wrfvar.exe
   ofne=${OUTPUTDIR}/m${E}_${ofn}
   mv $MODELDIR/wrfvar_output ${ofne}
   echo " -- ofn= "${ofne}
 done


echo "=== END bash $0 $*  ==="
exit
