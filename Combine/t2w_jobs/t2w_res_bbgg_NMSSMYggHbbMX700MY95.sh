#!/bin/bash

cd /home/users/fsetti/flashggFinalFit_resonant/CMSSW_10_2_13/src/flashggFinalFit/Combine

eval `scramv1 runtime -sh`

text2workspace.py Datacard_NMSSMYggHbbMX700MY95.txt -o Datacard_NMSSMYggHbbMX700MY95_res_bbgg.root -m 95 higgsMassRange=92,98 -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel   --PO "map=.*/NMSSM*.*:r[1,0,20]"