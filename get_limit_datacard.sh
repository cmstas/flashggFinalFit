#!/usr/bin/env bash

set -e

cd /home/users/yagu/XYH/FinalFit/CMSSW_10_2_13/src/flashggFinalFit

source /cvmfs/cms.cern.ch/cmsset_default.sh
#source /vols/grid/cms/setup.sh
source setup.sh

sig_model=$1
res_bkg_model=$2
m=$3
mh=$4
mx=$5
my=$6
dy_bkg_model=$7

get_last_cat() {
  for cat in $(grep "bin " $1 ) ; do
    last_cat=$cat
  done
  echo $last_cat
}

pushd Datacard
  #python makeDatacardGGTT_new.py -o Datacard_ggtt_resonant_${m}_all_cats.txt --MH $mh --MX $mx --MY $my --sig-syst ${sig_model}/systematics.json --res-bkg-syst ${res_bkg_model}/systematics.json --prune --do-res-bkg
  #combineCards.py --xc=$(get_last_cat Datacard_ggtt_resonant_${m}_all_cats.txt) Datacard_ggtt_resonant_${m}_all_cats.txt > Datacard_ggtt_resonant_${m}.txt

  #python makeDatacardGGTT_new.py -o Datacard_ggtt_resonant_${m}.txt --MH $mh --MX $mx --MY $my --prune --sig-syst ${sig_model}/systematics.json --res-bkg-syst ${res_bkg_model}/systematics.json --do-res-bkg
  #python makeDatacardGGTT_new.py -o Datacard_ggtt_resonant_${m}.txt --MH $mh --MX $mx --MY $my --sig-syst ${sig_model}/systematics.json --res-bkg-syst ${res_bkg_model}/systematics.json --do-res-bkg

  if [[ -n $dy_bkg_model ]]; then 
    echo "doABCD"
    python makeDatacardGGTT_new.py -o Datacard_ggtt_resonant_${m}.txt --MH $mh --MX $mx --MY $my --prune --do-res-bkg

    #python makeDatacardGGTT_new.py -o Datacard_ggtt_resonant_${m}.txt --MH $mh --MX $mx --MY $my --prune --sig-syst ${sig_model}/systematics.json --res-bkg-syst ${res_bkg_model}/systematics.json --do-res-bkg
    #python makeDatacardGGTT_new.py -o Datacard_ggtt_resonant_${m}.txt --MH $mh --MX $mx --MY $my --prune --sig-syst ${sig_model}/systematics.json --res-bkg-syst ${res_bkg_model}/systematics.json --doABCD
  else
    python makeDatacardGGTT_new.py -o Datacard_ggtt_resonant_${m}.txt --MH $mh --MX $mx --MY $my --prune --sig-syst ${sig_model}/systematics.json --res-bkg-syst ${res_bkg_model}/systematics.json --do-res-bkg --doABCD
    #python makeDatacardGGTT_new.py -o Datacard_ggtt_resonant_${m}.txt --MH $mh --MX $mx --MY $my --prune --sig-syst ${sig_model}/systematics.json --res-bkg-syst ${res_bkg_model}/systematics.json
  fi
#popd
