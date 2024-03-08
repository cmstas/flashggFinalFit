#!/bin/bash

cd /home/users/iareed/CMSSW_10_2_13/src/flashggFinalFit/Combine

eval `scramv1 runtime -sh`

text2workspace.py Datacard.txt -o Datacard_ttHHggXX.root -m 125.38 higgsMassRange=122,128 -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel   --PO "map=.*/ttHH_ggbb.*:r[1,0,200]"   --PO "map=.*/ttHH_ggWW.*:r[1,0,200]"   --PO "map=.*/ttHH_ggTauTau.*:r[1,0,200]"