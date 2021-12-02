#!/usr/bin/env bash

set -x
#set -e

#trees=/home/hep/mdk16/PhD/ggtt/CMSSW_10_2_0/src/HHToGGTT/output_trees
trees=/home/hep/mdk16/PhD/ggtt/ParamNN/outputTrees

pushd $trees
 rm -r ws
 rm -r 2018/ws*
 find 2018/ -type f -not -name "*TeV*" -exec rm {} \;
popd

cd flashggFinalFit

pushd Signal
 rm -r outdir_test_2018
 rm -r outdir_packaged
popd 

pushd Background
 rm -r outdir_test
popd

pushd Datacard
 rm -r yields_test
 rm Datacard.txt
popd

pushd Combine
 rm -r Models
 rm -r runFits_mu_inclusive
 rm -r t2w_jobs
 rm Datacard.txt 
 rm *.root
popd
