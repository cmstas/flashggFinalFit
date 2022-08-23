#!/bin/bash
ulimit -s unlimited
set -e
cd /home/users/fsetti/ic_flashgg/CMSSW_10_2_13/src
export SCRAM_ARCH=slc7_amd64_gcc700
source /cvmfs/cms.cern.ch/cmsset_default.sh
eval `scramv1 runtime -sh`
cd /home/users/fsetti/ic_flashgg/CMSSW_10_2_13/src/flashggFinalFit/Datacard
export PYTHONPATH=$PYTHONPATH:/home/users/fsetti/ic_flashgg/CMSSW_10_2_13/src/flashggFinalFit/tools:/home/users/fsetti/ic_flashgg/CMSSW_10_2_13/src/flashggFinalFit/Datacard/tools

python /home/users/fsetti/ic_flashgg/CMSSW_10_2_13/src/flashggFinalFit/Datacard/makeYields.py --cat SR2 --procs auto --ext 10Apr2022 --mass 125 --inputWSDirMap 2016=/home/users/fsetti/ic_flashgg/CMSSW_10_2_13/src/flashggFinalFit/files_systs/10Apr2022//ws_signal_2016,2017=/home/users/fsetti/ic_flashgg/CMSSW_10_2_13/src/flashggFinalFit/files_systs/10Apr2022//ws_signal_2017,2018=/home/users/fsetti/ic_flashgg/CMSSW_10_2_13/src/flashggFinalFit/files_systs/10Apr2022//ws_signal_2018 --sigModelWSDir ./Models/signal --sigModelExt packaged --bkgModelWSDir ./Models/background --bkgModelExt multipdf  --mergeYears --skipZeroes --doSystematics
