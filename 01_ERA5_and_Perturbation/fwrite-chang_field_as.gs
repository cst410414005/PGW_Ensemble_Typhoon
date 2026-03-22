*==============================================================================
function fwrite(args)
  'reinit'
  rc=gsfallow('on')
  ;*chelp=subwrd(args,1);if(args='')|( chelp = '-help')|( chelp = '-h' );help();return;endif
*==========================================================
  i=1
  E = subwrd(args,i) ; i=i+1
  file = 072912
;*E = '01'

;*自製網格資料
  ifn1.1 = '/work1/tgeo/ensemble/2024-0108-PGen/02-PG-ens-IC/ifn1/'file'/m'E'_wrfinput_d01.ctl'
  ifn1.2 = '/work1/tgeo/ensemble/2024-0108-PGen/02-PG-ens-IC/ifn1/'file'/m'E'_wrfinput_d01.ctl'

;*全球模式
  ifn2.1 = '/work1/tgeo/ensemble/2024-0108-PGen/01-WRF-RANDOM-ens-IC/ana/'file'/23'file'.sur.ctl'
  ifn2.2 = '/work1/tgeo/ensemble/2024-0108-PGen/01-WRF-RANDOM-ens-IC/ana/'file'/23'file'.pre.ctl'
 
;*要置換的位置
  ifn3 = '/work1/tgeo/ensemble/2024-0108-PGen/02-PG-ens-IC/ifn3/i.26.214.-23.57.ctl' 
*  ifn3 = './ifn3/i.0.360.-90.90.ctl'

  ofn.1 = '/work1/tgeo/ensemble/2024-0108-PGen/02-PG-ens-IC/data-input/'file'/m'E'_sur.bin'
  ofn.2 = '/work1/tgeo/ensemble/2024-0108-PGen/02-PG-ens-IC/data-input/'file'/m'E'_pre.bin'

*---------------------------------------------------------
;*for ifn1
  Vs1.1 = '(slp*100) U10 V10 T2'                             ;*unit: hPa to Pa  , m/s, m/s,  K
  Vs1.2 = '(height*9806.65) QVAPOR/(1+QVAPOR) tk umet vmet'     ;*unit: km to m2/s2, kg/kg - 混合比 to 比濕,  K,  m/s,  m/s
  Ls1.1 = '1000'
  Ls1.2 = '1000  925  850  700  600  500  400  300  250  200  150  100  50'

;*for ifn2
  Vs2.1 = 'MSLsfc no10Usfc no10Vsfc no2Tsfc'    ;*unit: Pa,  m/s,  m/s,  K
  Vs2.2 = 'Zprs Qprs Tprs Uprs Vprs'          ;*unit: m2/s2,  kg/kg,  K,  m/s,  m/s
  Ls2.1 = '1'
  Ls2.2 = '1000  925  850  700  600  500  400  300  250  200  150  100  50'


*---------------------------------------------------------
;*main run
  '!mkdir -p ./data-input'

;*get change info
 p('allclose')
  'xopen -t 'ifn3''
 p('define mask = mask1')

;*i = 1 for sur, i = 2 for pre
  i = 1 ; while( i<=2 )
    say 'i= 'i
   p('allclose')
     'xopen -t 'ifn3''
   p('set gxout fwrite')
   p('set fwrite 'ofn.i'')

    v = 1 ; while(1)
      vv1 = subwrd(Vs1.i, v)
      vv2 = subwrd(Vs2.i, v)
      if(vv1 = '') ; break ; endif

      l = 1 ; while(1)
        ll1 = subwrd(Ls1.i, l)
        ll2 = subwrd(Ls2.i, l)
        if(ll1 = '') ; break ; endif

      p('allclose')
        'xopen -t 'ifn1.i
        'set_lola all'
      p('set lev 'll1'')
      p('define v1 = 'vv1'')

      p('allclose')
        'xopen -t 'ifn2.i
        'set_lola all'
      p('set lev 'll2'')
      p('define v2 = 'vv2'')

      p('define ret = (lterp(const(v1, 0, -u), mask) * mask) + (lterp(const(v2, 0, -u), mask) * ((mask-1) * -1))')
      p('d ret')
      l = l + 1 ;  endwhile

    v = v + 1 ;  endwhile

   p('disable fwrite')
  i = i + 1 ; endwhile
*---------------------------------------------------------

  'quit'
  exit
*==========================================================
return
*==============================================================================
