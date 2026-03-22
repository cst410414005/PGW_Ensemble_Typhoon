file=072912

mkdir -p /work1/tgeo/ensemble/2024-0108-PGen/02-PG-ens-IC/ifn1/${file}

Es=`seq -f "%02g" 0 32`
ifd="/work1/tgeo/ensemble/2024-0108-PGen/01-WRF-RANDOM-ens-IC/${file}/wrfinput"
ofd="/work1/tgeo/ensemble/2024-0108-PGen/02-PG-ens-IC/ifn1/${file}"
for E in ${Es} ; do /work1/tgeo/ensemble/2024-0108-PGen/00.s/run-RANDOM-ens-IC-ARWpost.sh ${E} ${ifd} ${ofd}; done

gsmask="/work1/tgeo/ensemble/2024-0108-PGen/00.s/fwrite-grid_mask_as.gs"
LL="i,26,214,-23,57"
grads -bcl "${gsmask} -LL ${LL} -n ifn3 -o "`echo ${LL}|sed 's/,/./g'`" -q"

mkdir -p /work1/tgeo/ensemble/2024-0108-PGen/02-PG-ens-IC/data-input/${file}

gs="/work1/tgeo/ensemble/2024-0108-PGen/00.s/fwrite-chang_field_as.gs"
Es=`seq -f "%02g" 0 32`
for E in ${Es} ; do
grads -bcl "${gs} ${E}"
done

cp /work1/tgeo/ensemble/2024-0108-PGen/02-PG-ens-IC/data-input/${file}/* /jet/tgeo/ensemble/asia
cp /work1/tgeo/ensemble/2024-0108-PGen/01-WRF-RANDOM-ens-IC/ana/${file}/* /jet/tgeo/ensemble/asia
mkdir -p /jet/tgeo/ensemble/asia/data-input/${file}
