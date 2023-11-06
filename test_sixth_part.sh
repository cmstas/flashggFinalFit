#!/usr/bin/env bash

set -e

#cd /home/hep/mdk16/PhD/ggtt/finalfits_try2/CMSSW_10_2_13/src/flashggFinalFit
cd /home/users/yagu/XYH/FinalFit/CMSSW_10_2_13/src/flashggFinalFit 
source /cvmfs/cms.cern.ch/cmsset_default.sh
source setup.sh

# trees=/home/hep/mdk16/PhD/ggtt/ResonantGGTT/Outputs/Y_tautau/outputTrees
# sig_model=/home/hep/mdk16/PhD/ggtt/ResonantGGTT/Outputs/Y_tautau/Interpolation
# res_bkg_model=/home/hep/mdk16/PhD/ggtt/ResonantGGTT/Outputs/Y_tautau/ResonantBkg

# trees=/home/hep/mdk16/PhD/ggtt/ResonantGGTT/Outputs/Graviton/outputTrees
# sig_model=/home/hep/mdk16/PhD/ggtt/ResonantGGTT/Outputs/Graviton/Interpolation
# res_bkg_model=/home/hep/mdk16/PhD/ggtt/ResonantGGTT/Outputs/Graviton/ResonantBkg

# trees=/home/hep/mdk16/PhD/ggtt/ResonantGGTT/Outputs/Radion/outputTrees
# sig_model=/home/hep/mdk16/PhD/ggtt/ResonantGGTT/Outputs/Radion/Interpolation
# res_bkg_model=/home/hep/mdk16/PhD/ggtt/ResonantGGTT/Outputs/Radion/ResonantBkg

# trees=/home/hep/mdk16/PhD/ggtt/ResonantGGTT/Outputs/Y_gg_High_Mass/outputTrees
# sig_model=/home/hep/mdk16/PhD/ggtt/ResonantGGTT/Outputs/Y_gg_High_Mass/Interpolation
# res_bkg_model=/home/hep/mdk16/PhD/ggtt/ResonantGGTT/Outputs/Y_gg_High_Mass/ResonantBkg

trees=/home/users/yagu/XYH/XtoYH_pNN/Outputs/trained/outputTrees
#/home/hep/mdk16/PhD/ggtt/ResonantGGTT/Outputs/Y_gg_Low_Mass/outputTrees
sig_model=/home/users/yagu/XYH/XtoYH_pNN/Interpolation
#/home/hep/mdk16/PhD/ggtt/ResonantGGTT/Outputs/Y_gg_Low_Mass/Interpolation
res_bkg_model=/home/users/yagu/XYH/XtoYH_pNN/Outputs/Graviton/ResonantBkg
#/home/hep/mdk16/PhD/ggtt/ResonantGGTT/Outputs/Y_gg_Low_Mass/ResonantBkg
#dy_bkg_model=/home/hep/mdk16/PhD/ggtt/ResonantGGTT/RelicDYEstimation

sig_years="2016 2017 2018"
bkg_years="combined"

proc_template="ggttres"

wait_batch() {
  while [[ -n $(qstat -xml | grep "${1}") ]]; do
    echo $(qstat -xml | grep "${1}" | wc -l) "batch jobs remaining..."
    echo $(qstat -xml -s r | grep "${1}" | wc -l) "batch jobs running..."
    sleep 10
  done
}

get_mx() {
  echo $1 | cut -d'x' -f2 | cut -d'm' -f1
}
get_my() {
  echo $1 | cut -d'y' -f2
}

#graviton, radion, Y->tautau settings
# mggl=100
# mggh=180
# plot_blinding_region="115,135"
 get_mh() {
   echo 125
 }
# lumiMap="lumiMap = {'2016':36.31, '2017':41.48, '2018':59.83, 'combined':137.65, 'merged':137.65}"

#low mass Y->gg settings
mggl=65
#mggh=150
mggh=1000
plot_blinding_region="68,135"
#get_mh () {
#  echo $(get_my $1)
#}
do_scan=0
step_sf=0
lumiMap="lumiMap = {'2016':36.31, '2017':41.48, '2018':54.67, 'combined':132.46, 'merged':132.46}"
do_dy_bkg=0

#high mass Y->gg settings
# mggl=100
# mggh=1000
# plot_blinding_region="115,900"
# get_mh () {
#   echo $(get_my $1)
# }
# do_scan=1
# step_sf=1
# lumiMap="lumiMap = {'2016':36.31, '2017':41.48, '2018':59.83, 'combined':137.65, 'merged':137.65}"

sed -i "/lumiMap/s/.*/${lumiMap}/" tools/commonObjects.py

for year in $bkg_years ; do
  masses=$(python detect_mass_points.py ${trees}/${year})
done
echo "Detected mass points:" $masses

for year in $bkg_years ; do
  pushd ${trees}/${year}
    for m in $masses ; do
      let nCats=$(echo Data*${m}* | wc -w)
      let nCR=$(echo Data*${m}*cr_* | wc -w)
      echo "Detected $nCR control regions"
      let nCats=${nCats}-${nCR} 
      echo "Detected ${nCats} categories"
      popd
      break 2
    done
done

# wait_batch get_limit_hadd_tree2ws

#ls -lh /home/hep/mdk16/PhD/ggtt/ResonantGGTT/Outputs/Y_gg_Low_Mass/LimitVsMinNum/10/outputTrees/combined/*/ws/data_combined/*

for m in $masses ; do
  echo $(get_mx $m)
  echo $(get_my $m)
done

pushd Combine
 set +e
 set -e


 for m in $masses ; do
  if [[ -n $do_scan ]]; then 
    #python get_mH_for_scan.py ${step_sf} ${m} ${masses}
    #mh_to_scan=$(python get_mH_for_scan.py ${step_sf} ${m} ${masses})
    mh_to_scan=$(get_mh $m)
  else
    mh_to_scan=$(get_mh $m)
  fi

  for mh_scan in $mh_to_scan ; do
    echo $mh_scan
    . ../get_limit_combine.sh $mggl $mggh $(get_mx $m) $(get_my $m) $mh_scan
    #qsub -q hep.q -l h_rt=7200 ../get_limit_combine.sh $mggl $mggh $(get_mx $m) $(get_my $m) $mh_scan
    #qsub -q hep.q -l h_rt=1800 -pe hep.pe 8 ../get_limit_combine.sh $mggl $mggh $(get_mx $m) $(get_my $m) $mh_scan
  done
 done

# wait_batch get_limit_combine

 grep 'r <' combine_results_ggtt_resonant_*.txt > combine_results_summary.txt
popd

set +e

mkdir -p Outputs/CollectedPlots
cp -r Background/plots Outputs/CollectedPlots/Background/
mkdir -p Outputs/CollectedPlots/Combine
mkdir -p Outputs/CollectedPlots/Combine/Datacard
cp Combine/Datacard* Outputs/CollectedPlots/Combine/Datacard
mkdir -p Outputs/CollectedPlots/Combine/Results
cp Combine/combine_results* Outputs/CollectedPlots/Combine/Results
cp -r Combine/Models Outputs/CollectedPlots/Combine/Models
mkdir -p Outputs/CollectedPlots/Combine/Impacts
cp Combine/impacts* Outputs/CollectedPlots/Combine/Impacts/
mkdir -p Outputs/CollectedPlots/Combine/NLL_Scans
cp Combine/NLL_Scan* Outputs/CollectedPlots/Combine/NLL_Scans
mkdir -p Outputs/CollectedPlots/Background/DY
cp Combine/ggttres*cr*.png Outputs/CollectedPlots/Background/DY
