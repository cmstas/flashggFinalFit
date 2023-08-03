#!/usr/bin/env bash

set -x

source /cvmfs/cms.cern.ch/cmsset_default.sh
source /vols/grid/cms/setup.sh

cmsenv
source setup.sh

MY=95
MX=-1

tag=21Sep2022_MY${MY}
trees=/home/users/fsetti/flashggFinalFit_resonant/CMSSW_10_2_13/src/flashggFinalFit/files/$tag/

model_bkg(){
 sed -i "s/mass_value/${MY}/g" tools/mgg_window.py
 sed -i "s/-999/${MY}/g" tools/mgg_window.h
	pushd Trees2WS
	 python trees2ws_data.py --inputConfig syst_config_res_bbgg.py --inputTreeFile $trees/Data/allData.root
	popd
	
	pushd Background
	 	rm -rf outdir_${tag}_MX*_MY${MY}
		make clean
		make
		sed -i "s/dummy/${tag}/g" config_res_bbgg.py 
		sed -i "s/my_mass/${MY}/g" config_res_bbgg.py 
		sed -i "s/mx_mass/600/g" config_res_bbgg.py 

	  python RunBackgroundScripts.py --inputConfig config_res_bbgg.py --mode fTestParallel

		sed -i "s/${tag}/dummy/g" config_res_bbgg.py
		sed -i "s/${MY}/my_mass/g" config_res_bbgg.py 
		sed -i "s/600/mx_mass/g" config_res_bbgg.py 
		cp -r outdir_${tag}_MX600_MY${MY} outdir_${tag}_MX650_MY${MY}
		cp -r outdir_${tag}_MX600_MY${MY} outdir_${tag}_MX700_MY${MY}
	popd
 	sed -i "s/${MY}/mass_value/g" tools/mgg_window.py
 sed -i "s/${MY}/-999/g" tools/mgg_window.h
}


#Construct Signal Models (one per year)
model_sig(){
	sed -i "s/mass_value/${MY}/g" tools/mgg_window.py

	#Manully add all MX processes
	procs=("NMSSMYggHbbMX600MY${MY}" "NMSSMYggHbbMX650MY${MY}" "NMSSMYggHbbMX700MY${MY}" )
	#procs=("NMSSMYggHbbMX600MY${MY}" )

	for year in 2016 2017 2018
	#for year in 2016
	do
		rm -rf $trees/ws_signal_$year
		mkdir -p $trees/ws_signal_$year
		for proc in "${procs[@]}"
		do
			rm -rf $trees/$year/ws_$proc
			pushd Trees2WS
				python trees2ws.py --inputConfig syst_config_res_bbgg.py --inputTreeFile $trees/$year/${proc}_${MY}_13TeV.root --inputMass $MY --productionMode $proc --year $year --doSystematics
			popd
			mv $trees/$year/ws_$proc/${proc}_${MY}_13TeV_$proc.root $trees/ws_signal_$year/output_${proc}_M${MY}_13TeV_pythia8_${proc}.root 
		done

		pushd Signal	
		 rm -rf outdir_${tag}_$year
		 sed -i "s/dummy/${tag}/g" syst_config_res_bbgg_$year.py
		 sed -i "s/mass_value/${MY}/g" syst_config_res_bbgg_$year.py

	   python RunSignalScripts.py --inputConfig syst_config_res_bbgg_$year.py --mode fTest --modeOpts "--doPlots --mass ${MY}"
		 python RunSignalScripts.py --inputConfig syst_config_res_bbgg_$year.py --mode calcPhotonSyst
		 python RunSignalScripts.py --inputConfig syst_config_res_bbgg_$year.py --mode signalFit --groupSignalFitJobsByCat --modeOpts "--skipVertexScenarioSplit --replacementThreshold 100 --useDCB --doPlots"

		 #copy plots
	   plot_dir=/home/users/fsetti/public_html/HH2bbgg/flashggFinalFit/$tag/signalFit_$year
	   rm -rf $plot_dir
	   mkdir -p $plot_dir
     cp outdir_${tag}_$year/signalFit/Plots/*.png $plot_dir
	   cp ~/public_html/niceplots/index.php $plot_dir

	   plot_dir=/home/users/fsetti/public_html/HH2bbgg/flashggFinalFit/$tag/fTest_$year
	   rm -rf $plot_dir
	   mkdir -p $plot_dir
     cp outdir_${tag}_$year/fTest/Plots/*.png $plot_dir
	   cp ~/public_html/niceplots/index.php $plot_dir
			
		 sed -i "s/${tag}/dummy/g" syst_config_res_bbgg_$year.py
		popd

  sed -i "s/${MY}/mass_value/g" syst_config_res_bbgg_$year.py
	done

	pushd Signal	
		rm -rf outdir_packaged
		python RunPackager.py --cats SR1 --exts ${tag}_2016,${tag}_2017,${tag}_2018 --batch local --massPoints $MY --mergeYears
		python RunPackager.py --cats SR2 --exts ${tag}_2016,${tag}_2017,${tag}_2018 --batch local --massPoints $MY --mergeYears
		python RunPlotter.py --procs NMSSMYggHbbMX600MY${MY} --cats SR1 --ext packaged --MH $MY --mass $MY
		python RunPlotter.py --procs NMSSMYggHbbMX600MY${MY} --cats SR2 --ext packaged --MH $MY --mass $MY
		python RunPlotter.py --procs NMSSMYggHbbMX650MY${MY} --cats SR1 --ext packaged --MH $MY --mass $MY
		python RunPlotter.py --procs NMSSMYggHbbMX650MY${MY} --cats SR2 --ext packaged --MH $MY --mass $MY
		python RunPlotter.py --procs NMSSMYggHbbMX700MY${MY} --cats SR1 --ext packaged --MH $MY --mass $MY
		python RunPlotter.py --procs NMSSMYggHbbMX700MY${MY} --cats SR2 --ext packaged --MH $MY --mass $MY
	popd

	sed -i "s/${MY}/mass_value/g" tools/mgg_window.py
}

make_datacard(){
	procs=("NMSSMYggHbbMX600MY${MY}" "NMSSMYggHbbMX650MY${MY}" "NMSSMYggHbbMX700MY${MY}" )
	for proc in "${procs[@]}"
	do
		pushd Datacard
			rm -rf yields_$tag	
			python RunYields.py --inputWSDirMap 2016=${trees}/ws_signal_2016,2017=${trees}/ws_signal_2017,2018=${trees}/ws_signal_2018 --cats auto --procs "${proc}" --batch local --mergeYears --ext $tag --doSystematics --skipZeroes --mass $MY
			python makeDatacard.py --years 2016,2017,2018 --ext $tag --prune --pruneThreshold 0.000001 --doSystematics
			#echo "signal_scaler rateParam * NMSSM* 1" >> Datacard.txt
			#echo "nuisance edit freeze signal_scaler" >> Datacard.txt
			mv Datacard.txt ../Combine/Datacard_${proc}.txt	
		popd
	done
}

run_combine(){
	pushd Combine
		rm -rf Models
		mkdir -p Models
		mkdir -p Models/signal
		mkdir -p Models/background
		cp ../Signal/outdir_packaged/CMS-HGG*.root ./Models/signal/
		cp ../Background/outdir_${tag}_MX600_MY${MY}/CMS-HGG*.root ./Models/background/
		procs=("NMSSMYggHbbMX600MY${MY}" "NMSSMYggHbbMX650MY${MY}" "NMSSMYggHbbMX700MY${MY}" )
		for proc in "${procs[@]}"
		do

			python RunText2Workspace.py --mode  res_bbgg --dryRun --ext "_"${proc} --common_opts "-m ${MY} higgsMassRange=$((${MY}-3)),$((${MY}+3))" 
			./t2w_jobs/t2w_res_bbgg_${proc}.sh

			combine --expectSignal 1 -t -1 --redefineSignalPOI r --cminDefaultMinimizerStrategy 0 -M AsymptoticLimits -m ${MY} -d Datacard_${proc}_res_bbgg.root -n _AsymptoticLimit_r --freezeParameters MH --run=blind > combine_results_${proc}.txt

			tail combine_results_${proc}.txt
		done
	popd	
}

copy_plots(){

	plot_dir=/home/users/fsetti/public_html/HH2bbgg/flashggFinalFit/$tag
	mkdir -p $plot_dir
	mkdir -p $plot_dir/sig
	mkdir -p $plot_dir/bkg

	cp Signal/outdir_packaged/Plots/*.png $plot_dir/sig
	cp ~/public_html/niceplots/index.php $plot_dir/sig
	
	cp Background/outdir_${tag}_MX600_MY${MY}/bkgfTest-Data/*.png $plot_dir/bkg
	cp ~/public_html/niceplots/index.php $plot_dir/bkg
}

MY=90
tag=21Sep2022_MY${MY}
trees=/home/users/fsetti/flashggFinalFit_resonant/CMSSW_10_2_13/src/flashggFinalFit/files/$tag/
#
model_bkg
model_sig
copy_plots
make_datacard
run_combine
#

####################################################################

MY=95
tag=21Sep2022_MY${MY}
trees=/home/users/fsetti/flashggFinalFit_resonant/CMSSW_10_2_13/src/flashggFinalFit/files/$tag/

model_bkg
model_sig
copy_plots
make_datacard
run_combine
#
#
#####################################################################
#
MY=100
tag=21Sep2022_MY${MY}
trees=/home/users/fsetti/flashggFinalFit_resonant/CMSSW_10_2_13/src/flashggFinalFit/files/$tag/

model_bkg
model_sig
copy_plots
make_datacard
run_combine
