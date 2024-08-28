#!/bin/bash

cd /home/users/iareed/CMSSW_10_2_13/src/flashggFinalFit/Combine

eval `scramv1 runtime -sh`

text2workspace.py Datacard_Tprime_M500_pre_app.txt -o Datacard_Tprime_M500.root -m 125.38 higgsMassRange=122,128 -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel   --PO "map=.*/Tprime_ggbb_M500.*:r[1,0,200]"   --PO "map=.*/Tprime_ggWW_M500.*:r[1,0,200]"   --PO "map=.*/Tprime_ggTauTau_M500.*:r[1,0,200]"