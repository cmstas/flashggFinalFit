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

get_last_cat() {
  for cat in $(grep "bin " $1 ) ; do
    last_cat=$cat
  done
  echo $last_cat
}

pushd Datacard
#  python makeDatacardGGTT_new.py -o Datacard_${procTemplate}_${m}.txt --n-in-sideband $indir/../CatOptim/N_in_sidebands.json --MH $mh --MX $mx --MY $my --procTemplate ${procTemplate} --prune --sig-syst systematics_all_merged.json
  if [ $dy_bkg_model = 0 -a $res_bkg_sys = 0 ]; then 
    python makeDatacardGGTT_new.py -o Datacard_${procTemplate}_${m}.txt --n-in-sideband $indir/../CatOptim/N_in_sidebands.json --MH $mh --MX $mx --MY $my --procTemplate ${procTemplate} --prune --do-res-bkg --sig-syst ${sig_model}/systematics.json 

  elif [ $dy_bkg_model = 0 -a $res_bkg_sys = 1 ]; then
    python makeDatacardGGTT_new.py -o Datacard_${procTemplate}_${m}.txt --n-in-sideband $indir/../CatOptim/N_in_sidebands.json --MH $mh --MX $mx --MY $my --procTemplate ${procTemplate} --prune --do-res-bkg --sig-syst ${sig_model}/systematics.json --res-bkg-syst ${res_bkg_model}/systematics.json 

  elif [ $dy_bkg_model = 1 -a $res_bkg_sys = 0 ]; then
    python makeDatacardGGTT_new.py -o Datacard_${procTemplate}_${m}.txt --n-in-sideband $indir/../CatOptim/N_in_sidebands.json --MH $mh --MX $mx --MY $my --procTemplate ${procTemplate} --prune --do-res-bkg --sig-syst ${sig_model}/systematics.json --doABCD 

  else
    python makeDatacardGGTT_new.py -o Datacard_${procTemplate}_${m}.txt --n-in-sideband $indir/../CatOptim/N_in_sidebands.json --MH $mh --MX $mx --MY $my --procTemplate ${procTemplate} --prune --do-res-bkg --sig-syst ${sig_model}/systematics.json --doABCD --res-bkg-syst ${res_bkg_model}/systematics.json

  fi
popd
