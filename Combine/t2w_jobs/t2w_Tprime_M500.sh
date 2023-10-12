#!/bin/bash

cd /home/users/iareed/CMSSW_10_2_13/src/flashggFinalFit/Combine

eval `scramv1 runtime -sh`

text2workspace.py Datacard.txt -o Datacard_Tprime_M500.root -m 125 higgsMassRange=122,128 -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel   --PO "map=.*/TprimeBBM500.*:r[1,0,2]"   --PO "map=.*/TprimeWWM500.*:r[1,0,2]"   --PO "map=.*/TprimeTAUTAUM500.*:r[1,0,2]"