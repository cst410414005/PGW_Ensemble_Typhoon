function FixTYLog( args )
**-----------------------------------------------
**------------------------------------------------
*for inf1
*17: 2015080300  16.2 N 144.0 E  940 MB  180 KM   45 M/s   60 KM
*for inf2
*  lat       lon       y         x         k       min SLP  max wind
* 15.510   144.189    34.125   146.625    44.000   986.933    35.449
*...
**------------------------------------------------
* FixTYLog.gs [obs.txt] [sim.log] [ofn.txt] [start_time] [rowt] [wrfout_time_int] <-dno delete no data time>
*==============================================================================
  rc = gsfallow( 'on' )
    _ivar='v1.1'
    if( args = '' ) | ( args = '-help' ) | ( args = '-h' )
      help(); return
    endif
*  say 'run FixTYLog.gs...'
***** Default value *****
*遺失值要寫多少?
  mis_vu = -999.999
  dno    = 'T'
  quit   = 1
***** Arguement *****
* 必要參數
 i=1
 ifn1 = subwrd(args,i) ; i=i+1
 ifn2 = subwrd(args,i) ; i=i+1
 ofn1 = subwrd(args,i) ; i=i+1
 date = subwrd(args,i) ; i=i+1
 rowt = subwrd(args,i) ; i=i+1
 int_t= subwrd(args,i) ; i=i+1
* 選用參數
 arg = "dummy"
 while( arg != "" )
  arg = subwrd( args, i )
  i = i + 1
     if( arg = '-dno') ; dno=subwrd(args,i); i=i+1; endif
     if( arg = '-quit' | arg='-qu'| arg='-q') ; quit=subwrd(args,i) ; i=i+1; endif
 endwhile

 
*say ifn1
*say ifn2
*say ofn1
*say date
*say rowt
*say int_t
*say dno
*exit

**------------------------------------------------
say '';say ' 1.read...'
  ifn = ifn1
  say '  read file <- 'ifn
   i = 1 ; while( 1 )
     aa.i=read(ifn)
*say aa.i
     readz.i=subwrd(aa.i,1)
     aa.i=sublin(aa.i,2)
     aa1.i=aa.i
     if(readz.i=2)
       cc=close(ifn)
      say '   close('cc') '
      break
     endif
*     say aa1.i
     tt_o.i   = subwrd(aa1.i, 2) + 0
     lat_o.i  = subwrd(aa1.i, 3)
     lon_o.i  = subwrd(aa1.i, 5)
     pa_o.i   = subwrd(aa1.i, 7)
     wind_o.i = subwrd(aa1.i, 11)
*   say tt_o.i',' lat_o.i','lon_o.i','pa_o.i','wind_o.i
   i = i + 1; endwhile
   row_o = i - 1  
  
  ifn = ifn2
  say '  read file <- 'ifn
   k = 0
   i = 1 ; while( 1 )
     aa.i=read(ifn)
     readz.i=subwrd(aa.i,1)
     aa.i=sublin(aa.i,2)
     aa2.i=aa.i
     if(readz.i=2)
       cc=close(ifn)
*      say '   close('cc') '
      break
     endif
*     say aa2.i
     lat_so.i  = subwrd(aa2.i, 1)
     lon_so.i  = subwrd(aa2.i, 2)
     pa_so.i   = subwrd(aa2.i, 6)
     wind_so.i = subwrd(aa2.i, 7)
*   say  lat_so.i','lon_so.i','pa_so.i','wind_so.i
    if( lat_so.i = 'lat' )
      k = k + 1
      row_a.k = i
    endif
   i = i + 1; endwhile
   row_so = i - 1
*   say row_a.1','row_a.2

* *把要的一段整理出來
i = row_a.1 + 1 
k = 1 ; while ( k <= rowt )
    
    lat_s.k  = lat_so.i
    lon_s.k  = lon_so.i
    pa_s.k   = pa_so.i
    wind_s.k = wind_so.i
    phr.k    = ( k - 1 ) * int_t
    'date.gs 'date' 0 'phr.k''
    tt_s.k     = result + 0

*  先寫成 -1, 找不到tt_s相同者 -999
    lat_o2.k  = mis_vu 
    lon_o2.k  = mis_vu
    pa_o2.k   = mis_vu
    wind_o2.k = mis_vu
    dr.k      = mis_vu
    dp.k      = mis_vu
    dv.k      = mis_vu
    jo = 1 ; while( jo <= row_o )
      if( tt_o.jo = tt_s.k )
        lat_o2.k  = lat_o.jo
        lon_o2.k  = lon_o.jo
        pa_o2.k   = pa_o.jo
        wind_o2.k = wind_o.jo
        dr.k      = distance( lon_o2.k, lat_o2.k, lon_s.k, lat_s.k )
        dp.k      = pa_s.k - pa_o2.k
        dv.k      = wind_s.k - wind_o2.k
      endif
    jo = jo + 1 ;endwhile

*   時間點模擬也都些成missins value
*     if( lat_o2.k = mis_vu )
*       lat_s.k = mis_vu
*       lon_s.k = mis_vu
*       pa_s.k  = mis_vu
*       wind_s.k= mis_vu
*     endif

*  整理格式
   cphr.k    = printf('%02d',phr.k)
   ctt.k     = tt_s.k
   clat_s.k  = math_format('%8.3f', lat_s.k)
   clon_s.k  = math_format('%8.3f', lon_s.k)
   cpa_s.k   = math_format('%8.3f', pa_s.k)
   cwind_s.k = math_format('%8.3f', wind_s.k)
   clat_o2.k = math_format('%8.3f', lat_o2.k)
   clon_o2.k = math_format('%8.3f', lon_o2.k)
   cpa_o2.k  = math_format('%8.3f', pa_o2.k)
   cwind_o2.k= math_format('%8.3f', wind_o2.k) 
   cdr.k     = math_format('%8.3f', dr.k)
   cdp.k     = math_format('%8.3f', dp.k)
   cdv.k     = math_format('%8.3f', dv.k) 
   
*  say 'k='k
*  say '  ' clat_s.k'  'clon_s.k'  'cpa_s.k'  'cwind_s.k'  'cphr.k'  'ctt.k
*  say '  ' clat_o2.k'  'clon_o2.k'  'cpa_o2.k'  'cwind_o2.k
*  say '  ' cdr.k'  'cdp.k'  'cdv.k
i = i + 1
k = k + 1 ; endwhile


say '';say ' 3.write...'
say '  ofn1 ='ofn1
"!rm -rf "ofn1""
 k = 1 ; while( k <= rowt )
 if(dno='T')&(clat_o2.k=mis_vu);k=k+1;continue;endif
   ccwrite = cphr.k' 'ctt.k
   ccwrite = ccwrite % ' | 'clat_s.k' 'clon_s.k' 'cpa_s.k' 'cwind_s.k
   ccwrite = ccwrite % ' |  'clat_o2.k' 'clon_o2.k' 'cpa_o2.k' 'cwind_o2.k
   ccwrite = ccwrite % ' |  'cdr.k' 'cdp.k' 'cdv.k
   res = write(ofn1, ccwrite, append)
 k = k + 1 ;endwhile

if(quit);'quit';endif
exit
return

*====================================================================
*====================================================================
*
*help
*
function help()
 say ' Name:'
 say '   FixTYLog.gs 計算wrf模擬颱風與觀測之間的差異 '
 say '   var = '_ivar
 say ' '
 say ' Usage:'
 say '  FixTYLog.gs [obs.txt] [sim.log] [ofn.txt]'
 say '              [start_time] [rowt] [wrfout_time_int]'
 say '              [-dno delete]'
 say '              [-q quit]'
 say '              obs.txt   = TY_track.txt'
 say '              sim.log   = track.log'
 say '              ofn.txt   = name_out_file.txt'
 say '              start_time= YYYYMMDDHH 10位數字'
 say '              rowt      = wrfout有幾個時間點?'
 say '              wrfout_time_int=在sim.log裡的時間間隔(hr)'           
 say '              delete    = T/F'           
 say '              quit      = 1/0'           
 say ' '
 say ' '
 say ' 2018.09 YakultSmoothie'
 say ' '
return

*====================================================================
*===================================================================
