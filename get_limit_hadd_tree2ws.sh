#!/usr/bin/env bash

set -e
#set -x

cd /home/users/iareed/CMSSW_10_2_13/src/flashggFinalFit

source /cvmfs/cms.cern.ch/cmsset_default.sh
#source /vols/grid/cms/setup.sh
source setup.sh

mh=125

trees=$1
proc_template=$2
year=$3
m=$4

mggl=$5
mggh=$6

proc=${proc_template}${m}

pushd ${trees}/${year}
  rm -rf ${m}
  mkdir ${m}
  hadd -f ${m}/Data.root Data*${proc}*.root
popd

pushd Trees2WS     
  python trees2ws_data.py --inputConfig config_ggtt.py --inputTreeFile ${trees}/${year}/${m}/Data.root --mgg-range $mggl $mggh
popd

pushd ${trees}/${year}/${m}
  mv ws ws_data
  mkdir -p ws/data_${year}
  cp ws_data/Data.root ws/data_${year}/allData.root
  #echo ".q" | root -b ws/data_${year}/allData.root
popd

