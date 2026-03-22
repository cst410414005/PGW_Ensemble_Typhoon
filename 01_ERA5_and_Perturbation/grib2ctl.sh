!/bin/bash

./grib2ctl.pl 230922.pre.download.grib > 230922.pre.ctl
./gribmap -i 230922.pre.ctl -0
