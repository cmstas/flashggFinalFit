#!/usr/bin/env bash

#set -e
#
#cd /home/users/yagu/XYH/FinalFit/CMSSW_10_2_13/src/flashggFinalFit
source /cvmfs/cms.cern.ch/cmsset_default.sh
source setup.sh

trees=/home/users/yagu/XYH/XtoYH_pNN/Outputs/trained/outputTrees
sig_model=/home/users/yagu/XYH/XtoYH_pNN/Interpolation
res_bkg_model=/home/users/iareed/XtoYH_pNN/Outputs_forIan/Graviton/ResonantBkg
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
# get_mh() {
#   echo 125
# }
# lumiMap="lumiMap = {'2016':36.31, '2017':41.48, '2018':59.83, 'combined':137.65, 'merged':137.65}"

#low mass Y->gg settings
mggl=55
mggh=1000
plot_blinding_region="68,135"
get_mh () {
  echo $(get_my $1)
}
do_scan=1
step_sf=1
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
  masses="mx280my90"
done
echo "Detected mass points:" $masses

#for year in $bkg_years ; do
#  pushd ${trees}/${year}
#    for m in $masses ; do
#      let nCats=$(echo Data*${m}* | wc -w)
#      let nCR=$(echo Data*${m}*cr_* | wc -w)
#      echo "Detected $nCR control regions"
#      let nCats=${nCats}-${nCR}
#      echo "Detected ${nCats} categories"
#      popd
#      break 2
#    done
#done

for year in $sig_years ; do
    for m in $masses ; do
      echo ${PWD}
    . ./get_limit_hadd_tree2ws.sh $res_bkg_model $proc_template $year $m $mggl $mggh
    #. ./get_limit_hadd_tree2ws.sh $trees $proc_template $year $m $mggl $mggh
    done
done
echo 1

