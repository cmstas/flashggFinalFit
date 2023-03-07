#!/bin/bash

cd /home/users/iareed/CMSSW_10_2_13/src/flashggFinalFit/Combine

eval `scramv1 runtime -sh`

text2workspace.py Datacard.txt -o Datacard_2HDM_M350.root -m 125 higgsMassRange=122,128 -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel   --PO "map=.*/2HDMbbM350.*:r[1,0,2]"   --PO "map=.*/2HDMWWM350.*:r[1,0,2]"   --PO "map=.*/2HDMTAUTAUM350.*:r[1,0,2]"