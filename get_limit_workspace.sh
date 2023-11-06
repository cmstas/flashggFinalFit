#!/usr/bin/env bash

set -e

cd /home/users/yagu/XYH/FinalFit/CMSSW_10_2_13/src/flashggFinalFit

source /cvmfs/cms.cern.ch/cmsset_default.sh
#source /vols/grid/cms/setup.sh
source setup.sh

mh=125

mggl=$1
mggh=$2
mx=$3
my=$4
mh=$5

m="mx${mx}my${my}"
mo="mx${mx}my${my}mh${mh}"

pushd Combine
  python RunText2Workspace.py --mode  ggtt_resonant --dryRun --ext _ggtt_resonant_${m} --common_opts "-m ${mh} higgsMassRange=${mggl},${mggh} --channel-masks" --batch local
  ./t2w_jobs/t2w_ggtt_resonant_ggtt_resonant_${m}.sh
#popd
