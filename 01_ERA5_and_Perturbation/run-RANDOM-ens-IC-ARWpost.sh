#!/bin/bash

E=$1
ifd=$2
ofd=$3

sh="/work1/tgeo/ensemble/2024-0108-PGen/00.s/ARWpost.sh"
T="2023-07-29_12:00:00"
V="height,QVAPOR,tk,umet,vmet,slp,U10,V10,T2"
L="1000,925,850,700,600,500,400,300,250,200,150,100,50"
m=".T."  #麥卡托投影

ifn="${ifd}/m${E}_wrfinput_d01"
ofn="m${E}_wrfinput_d01"

${sh} ${ifn} ${ofd} ${ofn} ${T} ${T} 3600 -V ${V} -L ${L} -m ${m}

exit
