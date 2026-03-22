function fwrite(args)
  'reinit'
  rc=gsfallow('on')

  i=1
  E = subwrd(args,i) ; i=i+1
*-----------------------------------------------
;*if3
  ifn1.1 = 'm'E'_surface.ctl'
  ifn1.2 = 'm'E'_upper.ctl'

;*m00
  ifn2.1 = 'm00_surface.ctl'
  ifn2.2 = 'm00_upper.ctl'

;*全球模式
  ifn3.1 = '23072912.sur.ctl'
  ifn3.2 = '23072912.pre.ctl'

  ofn.1 = './data-input/072912/m'E'_su.bin'
  ofn.2 = './data-input/072912/m'E'_up.bin'
*-----------------------------------------------
;*for ifn1
  Vs1.1 = 'mslsfc no10usfc no10vsfc no2tsfc'
  Vs1.2 = 'z q t u v'
  Ls1.1 = '1000'
  Ls1.2 = '1000  925  850  700  600  500  400  300  250  200  150  100  50'

;*for m00
  Vs2.1 = 'mslsfc no10usfc no10vsfc no2tsfc'
  Vs2.2 = 'z q t u v'
  Ls2.1 = '1000'
  Ls2.2 = '1000  925  850  700  600  500  400  300  250  200  150  100  50'

;*for 全球
  Vs3.1 = 'MSLsfc no10Usfc no10Vsfc no2Tsfc'    ;*unit: Pa,  m/s,  m/s,  K
  Vs3.2 = 'Zprs Qprs Tprs Uprs Vprs'          ;*unit: m2/s2,  kg/kg,  K,  m/s,  m/s
  Ls3.1 = '1'
  Ls3.2 = '1000  925  850  700  600  500  400  300  250  200  150  100  50'
*-----------------------------------------------
;*main run
  '!mkdir -p ./data-input'

;*i = 1 for sur, i = 2 for pre
  i = 1 ; while( i<=2 )
    say 'i= 'i
   p('set gxout fwrite')
   p('set fwrite 'ofn.i'')

    v = 1 ; while(1)
      vv1 = subwrd(Vs1.i, v)
      vv2 = subwrd(Vs2.i, v)
      vv3 = subwrd(Vs3.i, v)
      if(vv1 = '') ; break ; endif

      l = 1 ; while(1)
        ll1 = subwrd(Ls1.i, l)
        ll2 = subwrd(Ls2.i, l)
        ll3 = subwrd(Ls3.i, l)
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

      p('allclose')
        'xopen -t 'ifn3.i
        'set_lola all'
      p('set lev 'll3'')
      p('define v3 = 'vv3'')

      p('define a = const(v1, 0, -u) - const(v2, 0, -u) + const(v3, 0, -u)')
      p('d a')
      l = l + 1 ;  endwhile

    v = v + 1 ;  endwhile

   p('disable fwrite')
  i = i + 1 ; endwhile
*---------------------------------------------------------

'quit'
