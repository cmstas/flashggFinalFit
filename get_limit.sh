#!/usr/bin/env bash

set -x

source /cvmfs/cms.cern.ch/cmsset_default.sh
source /vols/grid/cms/setup.sh

#trees=/home/hep/mdk16/PhD/ggtt/CMSSW_10_2_0/src/HHToGGTT/output_trees
trees=/home/hep/mdk16/PhD/ggtt/ParamNN/outputTrees
m=$1
#nCats=$2

#cd flashggFinalFit
source setup.sh

pushd $trees/2018
  #echo *${m}*
  #echo (*${m}* | wc -w)
  let nCats=$(echo *${m}* | wc -w)/3
  echo "Detected ${nCats} categories" 
  hadd -f radionm${m}.root radionm${m}_125*.root
  hadd -f Data.root Data*radionm${m}*.root
  hadd -f VH.root VH*radionm${m}cat*.root
popd

pushd Trees2WS
 python trees2ws.py --inputConfig config_ggtt.py --inputTreeFile ${trees}/2018/radionm${m}.root --inputMass 125 --productionMode radionm${m} --year 2018 
 python trees2ws_data.py --inputConfig config_ggtt.py --inputTreeFile ${trees}/2018/Data.root
 python trees2ws.py --inputConfig config_ggtt.py --inputTreeFile ${trees}/2018/VH.root --inputMass 125 --productionMode VH --year 2018
popd

pushd $trees
 mkdir -p ws/data_2018
 mkdir -p ws/signal_2018

 cp 2018/ws/Data.root ws/data_2018/allData.root
 cp 2018/ws_radionm${m}/radionm${m}_radionm${m}.root ws/signal_2018/output_radionm${m}_M125_13TeV_pythia8_radionm${m}.root
 cp 2018/ws_VH/VH_VH.root ws/signal_2018/output_VH_M125_13TeV_pythia8_VH.root
popd

pushd Signal
 sed -i "s/radionm500/radionm${m}/g" tools/XSBRMap.py
 sed -i "s/radionm500/radionm${m}/g" tools/replacementMap.py

 python RunSignalScripts.py --inputConfig config_ggtt.py --mode fTest --modeOpts "--doPlots"
 #python RunSignalScripts.py --inputConfig config_ggtt.py --mode signalFit --groupSignalFitJobsByCat --modeOpts "--skipSystematics --skipVertexScenarioSplit  --doPlots"
 python RunSignalScripts.py --inputConfig config_ggtt.py --mode signalFit --groupSignalFitJobsByCat --modeOpts "--skipSystematics --skipVertexScenarioSplit"
 python RunPackager.py --cats auto --exts test_2018 --batch local --massPoints 125 --year 2018 --inputWSDir ${trees}/ws/signal_2018/ #--mergeYears
 
 pushd outdir_packaged
  for ((i = 0 ; i < ${nCats} ; i++)); do
   mv CMS-HGG_sigfit_packaged_radionm${m}cat${i}_2018.root CMS-HGG_sigfit_packaged_radionm${m}cat${i}.root 
  done
 popd

 for ((i = 0 ; i < ${nCats} ; i++)); do
   python RunPlotter.py --procs radionm${m} --cats radionm${m}cat${i} --years 2018 --ext packaged
 done
 for ((i = 0 ; i < ${nCats} ; i++)); do
   python RunPlotter.py --procs VH --cats radionm${m}cat${i} --years 2018 --ext packaged
 done
 
 python RunPlotter.py --procs radionm${m},VH --cats all --years 2018 --ext packaged
 python RunPlotter.py --procs VH --cats all --years 2018 --ext packaged
 python RunPlotter.py --procs all --cats all --years 2018 --ext packaged

 pushd outdir_packaged
  for ((i = 0 ; i <= ${nCats} ; i++)); do
    mv CMS-HGG_sigfit_packaged_radionm${m}cat${i}.root CMS-HGG_sigfit_packaged_radionm${m}cat${i}_2018.root
  done
 popd

 sed -i "s/radionm${m}/radionm500/g" tools/XSBRMap.py
 sed -i "s/radionm${m}/radionm500/g" tools/replacementMap.py
popd

pushd Background
  python RunBackgroundScripts.py --inputConfig config_ggtt.py --mode fTestParallel
popd

pushd Datacard
 python RunYields.py --inputWSDirMap 2018=${trees}/ws/signal_2018 --cats auto --procs auto --batch local #--mergeYears
 python makeDatacard.py --years 2018 --ext test --prune
 echo "VH_scaler rateParam * VH_*_hgg 1" >> Datacard.txt
 echo "nuisance edit freeze VH_scaler" >> Datacard.txt
popd

pushd Combine
 mkdir Models
 mkdir Models/signal
 mkdir Models/background
 cp ../Signal/outdir_packaged/CMS-HGG*.root ./Models/signal/
 cp ../Background/outdir_test/CMS-HGG*.root ./Models/background/
 cp ../Datacard/Datacard.txt Datacard.txt

 pushd Models/background
  for ((i = 0 ; i < ${nCats} ; i++)); do
    mv CMS-HGG_multipdf_radionm${m}cat${i}.root CMS-HGG_multipdf_radionm${m}cat${i}_2018.root
  done
 popd

 #python RunText2Workspace.py --mode mu_inclusive --dryRun
 #./t2w_jobs/t2w_mu_inclusive.sh
 python RunText2Workspace.py --mode  ggtt_w_resonant_bkg --dryRun
 ./t2w_jobs/t2w_ggtt_w_resonant_bkg.sh

 #combine --expectSignal 1 -t -1 --redefineSignalPOI r --cminDefaultMinimizerStrategy 0 -M AsymptoticLimits -m 125 -d Datacard_mu_inclusive.root -n _AsymptoticLimit_r --freezeParameters MH --run=blind > combine_results.txt
 #combine --expectSignal 1 -t -1 --redefineSignalPOI r --cminDefaultMinimizerStrategy 0 -M MultiDimFit --algo grid --points 100 -m 125 -d Datacard_mu_inclusive.root -n _Scan_r --freezeParameters MH --rMin 0 --rMax 5
 #python plotLScan.py higgsCombine_Scan_r.MultiDimFit.mH125.root 

 combine --expectSignal 1 -t -1 --redefineSignalPOI r --cminDefaultMinimizerStrategy 0 -M AsymptoticLimits -m 125 -d Datacard_ggtt_w_resonant_bkg.root -n _AsymptoticLimit_r --freezeParameters MH --run=blind > combine_results.txt
 combine --expectSignal 1 -t -1 --redefineSignalPOI r --cminDefaultMinimizerStrategy 0 -M AsymptoticLimits -m 125 -d Datacard_ggtt_w_resonant_bkg.root -n _AsymptoticLimit_r --freezeParameters MH --run=blind --setParameters VH_scaler=0 > combine_results_VH_scale_0.txt
 combine --expectSignal 1 -t -1 --redefineSignalPOI r --cminDefaultMinimizerStrategy 0 -M AsymptoticLimits -m 125 -d Datacard_ggtt_w_resonant_bkg.root -n _AsymptoticLimit_r --freezeParameters MH --run=blind --setParameters VH_scaler=2 > combine_results_VH_scale_2.txt
 #combine --expectSignal 1 -t -1 --redefineSignalPOI r --cminDefaultMinimizerStrategy 0 -M MultiDimFit --algo grid --points 100 -m 125 -d Datacard_ggtt_w_resonant_bkg.root -n _Scan_r --freezeParameters MH --rMin 0 --rMax 5
 #python plotLScan.py higgsCombine_Scan_r.MultiDimFit.mH125.root
  
 tail combine_results.txt
popd

mkdir -p CollectedPlots/radionm${m}
cp -r Signal/outdir_test_2018/fTest/Plots 	CollectedPlots/radionm${m}/SignalfTest
cp -r Signal/outdir_test_2018/signalFit/Plots 	CollectedPlots/radionm${m}/SignalFit
cp -r Signal/outdir_packaged/Plots 		CollectedPlots/radionm${m}/SignalPackaged
cp -r Background/outdir_test/bkgfTest-Data 	CollectedPlots/radionm${m}/BackgroundfTest
cp Combine/combine_results*.txt 			CollectedPlots/radionm${m}/
cp Combine/NLL_scan* 				CollectedPlots/radionm${m}/
cp Combine/higgsCombine_AsymptoticLimit_r.AsymptoticLimits.mH125.root CollectedPlots/radionm${m}/
