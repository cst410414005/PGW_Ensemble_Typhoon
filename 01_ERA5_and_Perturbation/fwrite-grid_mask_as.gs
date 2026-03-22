* This script creates a grid mask by setting specific regions in the grid to 1 and others to 0.
*
* Usage:
*   fwrite [-i input_file] [-n output_directory] [-o output_file] [-LL coordinates] [-q]
* Options:
*   -q                 Quit after processing without displaying further information.
*   -i input_file      Specify the input file path (default: '/work1/ox/work/SW_DA/01-down/01-ERA5_850/04-for_WRF/2020-05-20_12.pre.grib.ctl').
*   -n output_directory  Specify the output directory (default: current directory).
*   -o output_file     Specify the output file name (default: 'out').
*   -LL coordinates    Specify the longitude and latitude coordinates (default: 'i,90,135,0,40').

function fwrite(args)
  rc=gsfallow('on') ; 'reinit'
*===================================
   quit=0 ; ndio='none' 
   ifn1 = '/work1/tgeo/ensemble/2024-0108-PGen/01-WRF-RANDOM-ens-IC/ana/072912/23072912.sur.ctl'
   ndir  = './ifn3/'
   ofn  = 'out'
   LL   = 'i,26,214,-23,57'
  i=1
   arg = "dummy"
   while( arg != "" )
    arg = subwrd( args, i )
    i = i + 1
    if( arg='-q')    ; quit=1                     ; endif
    if( arg = '-i')  ; ifn1=subwrd(args,i); i=i+1 ; endif
    if( arg = '-n')  ; ndir=subwrd(args,i); i=i+1 ; endif
    if( arg = '-o')  ;  ofn=subwrd(args,i); i=i+1 ; endif
    if( arg = '-LL') ;   LL=subwrd(args,i); i=i+1 ; endif
   endwhile

;*---------------------------
 outfnctl=ndir'/'ofn'.ctl'
 outfndat=ndir'/'ofn'.bin'

;*---------------------------
say 'INFO: '
say ' ifn1= 'ifn1
say ' ofn1= 'outfndat
say ' ofn2= 'outfnctl

;*---------------------------
;*run
  'xopen 'ifn1''
  'set z 1'
  'sl 'LL'' 
  lo1 = qdims('lonmin')
  lo2 = qdims('lonmax')
  la1 = qdims('latmin')
  la2 = qdims('latmax')

  'sl all'
  ;*for ctl-----
  xx1 = qdims('xmin')
  xx2 = qdims('xmax')
  yy1 = qdims('ymin')
  yy2 = qdims('ymax')
  xint=qctlinfo( 1,xdef, 4)
  yint=qctlinfo( 1,ydef, 4)
  lon1=qdims('lonmin')
  lat1=qdims('latmin')
  ;*for ctl end-----
p('define mask1 = if(lon,>=,'lo1',if(lon,<=,'lo2',if(lat,>=,'la1',if(lat,<=,'la2',1,0),0),0),0)')

;*---------------------------
;*output
   '!mkdir -p 'ndir''
   '!rm -f 'outfndat''
   'set gxout fwrite'
   'set fwrite 'outfndat''
   'sl all'
 p('d mask1')

  clev='1000' 
  xs = xx2-xx1+1
  ys = yy2-yy1+1
  zs = 1
  ts = 1
  time1 = '01jan1900'
  nvars = 1
  ic=1
  cctl.ic = ' dset ^'ofn'.bin'                   ;ic=ic+1
  cctl.ic = ' title fwrite-grid_mask_by_GrADS'   ;ic=ic+1
  cctl.ic = ' undef -9.99E+08'                   ;ic=ic+1
  cctl.ic = ' xdef 'xs' Linear 'lon1' 'xint''    ;ic=ic+1
  cctl.ic = ' ydef 'ys' Linear 'lat1' 'yint''    ;ic=ic+1
  cctl.ic = ' zdef 'zs' levels 'clev''           ;ic=ic+1
  cctl.ic = ' tdef 'ts' linear 'time1' 1dy'      ;ic=ic+1
  cctl.ic = ' '                                  ;ic=ic+1
  cctl.ic = ' vars 'nvars''                      ;ic=ic+1
  cctl.ic = '  mask1 1 99 [1/0]'                 ;ic=ic+1
  cctl.ic = ' endvars'                           ;ic=ic+1
  cctl.ic = ''                                   ;ic=ic+1

  ico=ic-1
  '!rm -f 'outfnctl''
  ic=1;while(ic<=ico)
     if(cctl.ic='');break;endif
     if(ic=1); res=write(outfnctl,cctl.1)
      else;    res=write(outfnctl,cctl.ic,append)
     endif
  ic=ic+1;endwhile
  res=close(outfnctl)
;*---------------------------
say 'OUT:' 
say ' ofn1= 'outfndat
say ' ofn2= 'outfnctl

*===================================
  if(quit);'quit';endif
return
