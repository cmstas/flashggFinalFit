#!/usr/bin/env bash

set -x

source /cvmfs/cms.cern.ch/cmsset_default.sh
source /vols/grid/cms/setup.sh

tag=15Aug2022_bbgg_res
trees=/home/users/fsetti/ambulance_bbgg_flashggFinalFit/CMSSW_10_2_13/src/flashggFinalFit/files/$tag/

cmsenv
source setup.sh

model_bkg(){
	for my in 90
	do
	 sed -i "s/mass_value/${my}/g" tools/mgg_window.py
	 sed -i "s/-999/${my}/g" tools/mgg_window.h
		pushd Trees2WS
		 python trees2ws_data.py --inputConfig syst_config_res_bbgg.py --inputTreeFile $trees/Data/allData.root
		popd
		
		pushd Background
		 	rm -rf outdir_$tag
			make clean
			make
			sed -i "s/dummy/${tag}/g" config_res_bbgg.py 

		  python RunBackgroundScripts.py --inputConfig config_res_bbgg.py --mode fTestParallel

			sed -i "s/${tag}/dummy/g" config_res_bbgg.py
		popd
	 	sed -i "s/${my}/mass_value/g" tools/mgg_window.py
	 sed -i "s/${my}/-999/g" tools/mgg_window.h
	done
}

#Construct Signal Models (one per year)
model_sig(){
	#for my in 90 95 100
	for my in 90
	do
	 sed -i "s/mass_value/${my}/g" tools/mgg_window.py
		#for mx in 600 650 700
		for mx in 600
		do
			procs=("NMSSMYggHbbMX${mx}MY${my}" )

			for year in 2016 2017 2018
			#for year in 2016
			do
				rm -rf $trees/ws_signal_$year
				mkdir -p $trees/ws_signal_$year
				for proc in "${procs[@]}"
				do

					rm -rf $trees/$year/ws_$proc

					pushd Trees2WS
						python trees2ws.py --inputConfig syst_config_res_bbgg.py --inputTreeFile $trees/$year/${proc}_${my}_13TeV.root --inputMass $my --productionMode $proc --year $year --doSystematics
					popd

					mv $trees/$year/ws_$proc/${proc}_${my}_13TeV_$proc.root $trees/ws_signal_$year/output_${proc}_M${my}_13TeV_pythia8_${proc}.root 

				done

				pushd Signal	
				 rm -rf outdir_${tag}_$year
				 sed -i "s/dummy/${tag}/g" syst_config_res_bbgg_$year.py
				 sed -i "s/mass_value/${my}/g" syst_config_res_bbgg_$year.py

  		   python RunSignalScripts.py --inputConfig syst_config_res_bbgg_$year.py --mode fTest --modeOpts "--doPlots"
				 python RunSignalScripts.py --inputConfig syst_config_res_bbgg_$year.py --mode calcPhotonSyst
				 #python RunSignalScripts.py --inputConfig syst_config_res_bbgg_$year.py --mode signalFit --groupSignalFitJobsByCat --modeOpts "--skipVertexScenarioSplit --replacementThreshold 100 --useDCB "
				 python RunSignalScripts.py --inputConfig syst_config_res_bbgg_$year.py --mode signalFit --groupSignalFitJobsByCat --modeOpts "--skipVertexScenarioSplit --replacementThreshold 100 "

				 sed -i "s/${tag}/dummy/g" syst_config_res_bbgg_$year.py
				 sed -i "s/${my}/mass_value/g" syst_config_res_bbgg_$year.py
				popd
			done
		done
	 sed -i "s/${my}/mass_value/g" tools/mgg_window.py


		pushd Signal	
			rm -rf outdir_packaged
			python RunPackager.py --cats SR1 --exts ${tag}_2016,${tag}_2017,${tag}_2018 --batch local --massPoints $my --mergeYears
			python RunPackager.py --cats SR2 --exts ${tag}_2016,${tag}_2017,${tag}_2018 --batch local --massPoints $my --mergeYears
		#	python RunPlotter.py --procs HHggTauTau --cats SR1 --years 2016,2017,2018 --ext packaged
		#	python RunPlotter.py --procs HHggTauTau --cats SR2 --years 2016,2017,2018 --ext packaged
		popd

	done
}

make_datacard(){
	#for my in 90 95 100
	for my in 90
	do
		#for mx in 600 650 700
		for mx in 600
		do
			pushd Datacard
			 rm -rf yields_$tag
		
			 python RunYields.py --inputWSDirMap 2016=${trees}/ws_signal_2016,2017=${trees}/ws_signal_2017,2018=${trees}/ws_signal_2018 --cats auto --procs auto --batch local --mergeYears --ext $tag --doSystematics --skipZeroes --mass $my
			 python makeDatacard.py --years 2016,2017,2018 --ext $tag --prune --pruneThreshold 0.000001 --doSystematics
		
			popd
		done
	done
}

run_combine(){
	#for my in 90 95 100
	for my in 90
	do
		#for mx in 600 650 700
		for mx in 600
		do

			pushd Combine
				rm -rf Models
				mkdir -p Models
				mkdir -p Models/signal
				mkdir -p Models/background
				cp ../Signal/outdir_packaged/CMS-HGG*.root ./Models/signal/
				cp ../Background/outdir_$tag/CMS-HGG*.root ./Models/background/
				cp ../Datacard/Datacard.txt Datacard.txt
			
				python RunText2Workspace.py --mode  res_bbgg --dryRun
				./t2w_jobs/t2w_res_bbgg.sh

				combine --expectSignal 1 -t -1 --redefineSignalPOI r --cminDefaultMinimizerStrategy 0 -M AsymptoticLimits -m 90 -d Datacard_res_bbgg.root -n _AsymptoticLimit_r --freezeParameters MH --run=blind > combine_results.txt

				tail combine_results.txt
			popd	

		done
	done
}

model_bkg
model_sig
make_datacard
run_combine
