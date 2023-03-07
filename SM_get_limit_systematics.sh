#!/usr/bin/env bash

set -x

source /cvmfs/cms.cern.ch/cmsset_default.sh
#source /vols/grid/cms/setup.sh

tag=SM_23Sep22_with_HHGGXX
#tag=SM_23Sep22_08Dec22
#tag=SM_12Dec22_global_test_14Dec22
#tag=BSM_13Oct22_M250_fixed_weights
#tag=BSM_13Oct22_M300_fixed_weights
#tag=BSM_13Oct22_M350_fixed_weights
trees=/home/users/iareed/ttHHggbb/coupling_scan/CMSSW_10_2_13/src/flashggFinalFit/files_systs/$tag/

cmsenv
source setup.sh

model_bkg(){
	pushd Trees2WS
	 python trees2ws_data.py --inputConfig syst_config_tthh.py --inputTreeFile $trees/Data/allData.root
	popd
	
	pushd Background
	 	rm -rf outdir_$tag
		sed -i "s/dummy/${tag}/g" config_tthh.py 

	  python RunBackgroundScripts.py --inputConfig config_tthh.py --mode fTestParallel

		sed -i "s/${tag}/dummy/g" config_tthh.py
	popd
}

#Construct Signal Models (one per year)
model_sig(){
        procs=("ttHHggbb" "ttHHggWW" "ttHHggTauTau" "ggH" "ttH" "VBFH" "VH" "HHGGbb" "HHGGWWsemileptonic" "HHGGWWdileptonic" "HHGGTauTau")
        #procs=("2HDMbbM250" "2HDMWWM250" "2HDMTAUTAUM250" "ttHHggbb" "ttHHggWW" "ttHHggTauTau" "ggH" "ttH" "VBFH" "VH" "HHGGbb" "HHGGWWsemileptonic" "HHGGWWdileptonic" "HHGGTauTau")
        #procs=("2HDMbbM300" "2HDMWWM300" "2HDMTAUTAUM300" "ttHHggbb" "ttHHggWW" "ttHHggTauTau" "ggH" "ttH" "VBFH" "VH" "HHGGbb" "HHGGWWsemileptonic" "HHGGWWdileptonic" "HHGGTauTau")
        #procs=("2HDMbbM350" "2HDMWWM350" "2HDMTAUTAUM350" "ttHHggbb" "ttHHggWW" "ttHHggTauTau" "ggH" "ttH" "VBFH" "VH" "HHGGbb" "HHGGWWsemileptonic" "HHGGWWdileptonic" "HHGGTauTau")
        #procs=("ttHHggbb" "ttH") #Min set for debugging
	for year in 2016 2017 2018
	#for year in 2016   #Careful: I was running into errors when debugging with only one year
	do
		rm -rf $trees/ws_signal_$year
		mkdir -p $trees/ws_signal_$year
		for proc in "${procs[@]}"
		do
			rm -rf $trees/$year/ws_$proc

			pushd Trees2WS
				python trees2ws.py --inputConfig syst_config_tthh.py --inputTreeFile $trees/$year/${proc}_125_13TeV.root --inputMass 125 --productionMode $proc --year $year --doSystematics
			popd

			mv $trees/$year/ws_$proc/${proc}_125_13TeV_$proc.root $trees/ws_signal_$year/output_${proc}_M125_13TeV_pythia8_${proc}.root 
		done

		pushd Signal	
		    rm -rf outdir_${tag}_$year
		    sed -i "s/dummy/${tag}/g" syst_config_tthh_$year.py

                    python RunSignalScripts.py --inputConfig syst_config_tthh_$year.py --mode fTest --modeOpts "--doPlots"
		    python RunSignalScripts.py --inputConfig syst_config_tthh_$year.py --mode calcPhotonSyst
		    python RunSignalScripts.py --inputConfig syst_config_tthh_$year.py --mode signalFit --groupSignalFitJobsByCat --modeOpts "--skipVertexScenarioSplit "

	            sed -i "s/${tag}/dummy/g" syst_config_tthh_$year.py
	    	popd
	done

	pushd Signal	
		rm -rf outdir_packaged
		python RunPackager.py --cats SR1 --exts ${tag}_2016,${tag}_2017,${tag}_2018 --batch local --massPoints 125 --mergeYears
		python RunPlotter.py --procs all --cats SR1 --years 2016,2017,2018 --ext packaged
		python RunPackager.py --cats SR2 --exts ${tag}_2016,${tag}_2017,${tag}_2018 --batch local --massPoints 125 --mergeYears
		python RunPlotter.py --procs all --cats SR2 --years 2016,2017,2018 --ext packaged
	popd
}

make_datacard(){
	pushd Datacard
	 rm -rf yields_$tag
         rm Datacard.txt

	 python RunYields.py --inputWSDirMap 2016=${trees}/ws_signal_2016,2017=${trees}/ws_signal_2017,2018=${trees}/ws_signal_2018 --cats auto --procs auto --batch local --mergeYears --skipZeroes --ext $tag --doSystematics 
   #python RunYields.py --inputWSDirMap 2016=${trees}/ws_signal_2016,2017=${trees}/ws_signal_2017,2018=${trees}/ws_signal_2018 --cats auto --procs "HHggTauTau,HHggWWdileptonic,ggH,ttH,VH,VBFH" --batch local --mergeYears --ext $tag --doSystematics --skipZeroes

	 python makeDatacard.py --years 2016,2017,2018 --ext $tag --prune --pruneThreshold 0.00001 --doSystematics
         cp Datacard.txt Datacard_${tag}.txt
	popd
}

run_combine(){
	pushd Combine
		rm -rf Models
		mkdir -p Models
		mkdir -p Models/signal
		mkdir -p Models/background
		cp ../Signal/outdir_packaged/CMS-HGG*.root ./Models/signal/
		cp ../Background/outdir_$tag/CMS-HGG*.root ./Models/background/
		cp ../Datacard/Datacard.txt Datacard.txt
	
		python RunText2Workspace.py --mode  ttHHggXX --dryRun
		./t2w_jobs/t2w_ttHHggXX.sh

		combine --expectSignal 1 -t -1 --redefineSignalPOI r --cminDefaultMinimizerStrategy 0 -M AsymptoticLimits -m 125 -d Datacard_ttHHggXX.root -n _AsymptoticLimit_r --freezeParameters MH --run=blind > combine_results_${tag}.txt
		combine --expectSignal 1 -t -1 --redefineSignalPOI r --cminDefaultMinimizerStrategy 0 -M AsymptoticLimits -m 125 -d Datacard_ttHHggXX.root -n _AsymptoticLimit_r --freezeParameters allConstrainedNuisances --run=blind > stat_only_${tag}.txt

                # Likelyhood scan parts
		#combine --expectSignal 1 -t -1 --redefineSignalPOI r --cminDefaultMinimizerStrategy 0 -M MultiDimFit --algo grid --points 100 -m 125 -d Datacard_ggtt_resBkg_syst.root -n _Scan_r --freezeParameters MH --rMin 0 --rMax 5
		#python plotLScan.py higgsCombine_Scan_r.MultiDimFit.mH125.root
		#cp NLL_scan* /home/users/fsetti/public_html/HH2ggtautau/flashggFinalFit/$tag/

		tail combine_results_${tag}.txt
	popd	
}

syst_plots(){
	pushd Combine
		text2workspace.py Datacard.txt -m 125
		combineTool.py  --expectSignal 1 -t -1 -M Impacts -d Datacard.root --redefineSignalPOI r --autoMaxPOIs "r" --rMin -2 --squareDistPoiStep --cminDefaultMinimizerStrategy 0 -m 125 --freezeParameters MH --doInitialFit --robustFit 1 --robustHesse 1
		combineTool.py  --expectSignal 1 -t -1 -M Impacts -d Datacard.root --redefineSignalPOI r --autoMaxPOIs "r" --rMin -2 --squareDistPoiStep --cminDefaultMinimizerStrategy 0 -m 125 --freezeParameters MH --robustFit 1 --robustHesse 1 --doFits --parallel 10

		#combineTool.py  -t -1 --setParameters r=100.0 -M Impacts -d Datacard.root --redefineSignalPOI r --squareDistPoiStep --cminDefaultMinimizerStrategy 0 -m 125 --freezeParameters MH --doInitialFit --robustFit 1
		#combineTool.py  -t -1 --setParameters r=100.0 -M Impacts -d Datacard.root --redefineSignalPOI r --squareDistPoiStep --cminDefaultMinimizerStrategy 0 -m 125 --freezeParameters MH --robustFit 1   --doFits --parallel 10

		combineTool.py -M Impacts -d Datacard.root --redefineSignalPOI r --autoMaxPOIs "r" --rMin -2 --squareDistPoiStep --cminDefaultMinimizerStrategy 0 -m 125 --freezeParameters MH -o impacts.json 

		plotImpacts.py -i impacts.json -o impacts
		mkdir -p /home/users/iareed/public_html/ttHH/flashggFinalFit/$tag/
		cp impacts.pdf /home/users/iareed/public_html/ttHH/flashggFinalFit/$tag/impacts.pdf
	popd	
}

copy_plot(){
	mkdir -p /home/users/iareed/public_html/ttHH/flashggFinalFit/$tag
	mkdir -p /home/users/iareed/public_html/ttHH/flashggFinalFit/$tag/Data
	mkdir -p /home/users/iareed/public_html/ttHH/flashggFinalFit/$tag/Signal

	cp /home/users/iareed/public_html/ttHH/index.php /home/users/iareed/public_html/ttHH/flashggFinalFit/$tag/Data
	cp Background/outdir_$tag/bkgfTest-Data/* /home/users/iareed/public_html/ttHH/flashggFinalFit/$tag/Data
	cp Signal/outdir_packaged/Plots/* /home/users/iareed/public_html/ttHH/flashggFinalFit/$tag/Signal
	cp /home/users/iareed/public_html/ttHH/index.php /home/users/iareed/public_html/ttHH/flashggFinalFit/$tag/Signal
}

#model_bkg
#model_sig
#make_datacard
#run_combine
syst_plots
#copy_plot
