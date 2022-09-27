#!/bin/bash

cd /home/users/fsetti/flashggFinalFit_resonant/CMSSW_10_2_13/src/flashggFinalFit/Combine

eval `scramv1 runtime -sh`

text2workspace.py Datacard_NMSSMYggHbbMX650MY90.txt -o Datacard_NMSSMYggHbbMX650MY90_res_bbgg.root -m 90 higgsMassRange=87,93 -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel   --PO "map=.*/NMSSM*.*:r[1,0,20]"