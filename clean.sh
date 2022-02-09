#!/usr/bin/env bash

set -x
#set -e

#trees=/home/hep/mdk16/PhD/ggtt/CMSSW_10_2_0/src/HHToGGTT/output_trees
#trees=/home/hep/mdk16/PhD/ggtt/ParamNN/outputTrees
#trees=/home/hep/mdk16/PhD/ggtt/ResonantGGTT/tagging_output/NMSSM_XYH_Y_gg_H_tautau_MX_500_MY_100/outputTrees
trees=/home/hep/mdk16/PhD/ggtt/ResonantGGTT/tagging_output/radionM500_HHggTauTau/outputTrees

pushd $trees
 rm -r 2018/*/
popd

#cd flashggFinalFit

pushd Signal
 rm -r outdir*/
 rm config_ggtt_*.py*
 sed -i '/ggtt_resonant/d' tools/replacementMap.py
 sed -i -e :a -e '/^\n*$/{$d;N;ba' -e '}' tools/replacementMap.py #remove blank lines at end
 sed -i '/ggtt_resonant/d' tools/XSBRMap.py
 sed -i -e :a -e '/^\n*$/{$d;N;ba' -e '}' tools/XSBRMap.py #remove blank lines at end
popd 

pushd Background
 rm -r outdir*/
 rm config_ggtt_*.py*
popd

pushd Datacard
 rm -r yields*/
 rm Datacard*.txt
popd

pushd Combine
 rm -r Models
 rm -r runFits_mu_inclusive
 rm -r t2w_jobs
 rm Datacard*.txt 
 rm *.root
 rm combine_results*.txt
popd
