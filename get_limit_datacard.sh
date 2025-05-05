#!/usr/bin/env bash

set -e

sig_model=$1
res_bkg_model=$2
m=$3
mh=$4
mx=$5
my=$6
dy_bkg_model=$7
procTemplate=$8
indir=$9
res_bkg_sys=${10}
useMassGrid_Interp=${11}
temp_part=${12}

get_last_cat() {
  for cat in $(grep "bin " $1 ) ; do
    last_cat=$cat
  done
  echo $last_cat
}

pushd Datacard
  if [ $dy_bkg_model = 0 -a $res_bkg_sys = 0 ]; then 
    python makeDatacardGGTT_new.py -o Datacard_${procTemplate}_${m}.txt --n-in-sideband $indir/../CatOptim/N_in_sidebands.json --MH $mh --MX $mx --MY $my --procTemplate ${procTemplate} --prune --do-res-bkg --sig-syst ${sig_model}/systematics.json 

  elif [ $dy_bkg_model = 0 -a $res_bkg_sys = 1 ]; then
    python makeDatacardGGTT_new.py -o Datacard_${procTemplate}_${m}.txt --n-in-sideband $indir/../CatOptim/N_in_sidebands.json --MH $mh --MX $mx --MY $my --procTemplate ${procTemplate} --prune --do-res-bkg --sig-syst ${sig_model}/systematics.json --res-bkg-syst ${res_bkg_model}/systematics.json 

  elif [ $dy_bkg_model = 1 -a $res_bkg_sys = 0 ]; then
    python makeDatacardGGTT_new.py -o Datacard_${procTemplate}_${m}.txt --n-in-sideband $indir/../CatOptim/N_in_sidebands.json --MH $mh --MX $mx --MY $my --procTemplate ${procTemplate} --prune --do-res-bkg --sig-syst ${sig_model}/systematics.json --doABCD 

  else
#    python makeDatacardGGTT_new.py -o Datacard_${procTemplate}_${m}.txt --n-in-sideband $indir/../CatOptim/N_in_sidebands.json --MH $mh --MX $mx --MY $my --procTemplate ${procTemplate} --prune --do-res-bkg --sig-syst ${sig_model}/systematics.json --doABCD --res-bkg-syst ${res_bkg_model}/systematics.json
    if [ -n "$useMassGrid_Interp" ]; then
      python makeDatacardGGTT_new.py -o Datacard_${procTemplate}_${m}.txt --n-in-sideband $indir/../../CatOptim_2sigma_$useMassGrid_Interp/N_in_sidebands_for_extra_masses.json --MH $mh --MX $mx --MY $my --procTemplate ${procTemplate} --prune --do-res-bkg --sig-syst ${sig_model}/systematics.json --doABCD --res-bkg-syst ${res_bkg_model}/systematics.json --useMassGrid_Interp $useMassGrid_Interp --temp_part $temp_part
    fi
  fi
popd
