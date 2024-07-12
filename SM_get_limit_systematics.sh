#!/usr/bin/env bash

#set -x

source /cvmfs/cms.cern.ch/cmsset_default.sh
#source /vols/grid/cms/setup.sh

tag=SM_pre_app_20240523
interpretation=ttHHggXX
trees=/home/users/iareed/CMSSW_10_2_13/src/flashggFinalFit/files_systs/$tag/

cmsenv
source setup.sh

model_bkg(){
    #syst_config_ttHH_ggXX.py will only need to be changed once per analysis
    pushd Trees2WS
        python trees2ws_data.py --inputConfig syst_config_ttHH_ggXX.py --inputTreeFile $trees/Data/allData.root
    popd

    #config_ttHH_ggxx.py should not need to be changed, though a better name might make sense
    pushd Background
        rm -rf outdir_$tag
        sed -i "s/dummy/${tag}/g" config_ttHH_ggXX.py
        python RunBackgroundScripts.py --inputConfig config_ttHH_ggXX.py --mode fTestParallel
        sed -i "s/${tag}/dummy/g" config_ttHH_ggXX.py
    popd
}

#Construct Signal Models (one per year)
model_sig(){
    #procs=("ttHH_ggbb" "ttHH_ggWW" "ttHH_ggTauTau")
    procs=("ttHH_ggbb" "ttHH_ggWW" "ttHH_ggTauTau" "ggH" "ttH" "tHq" "tHW" "VH" "ggHH_ggbb" "ggHH_ggWWsemileptonic" "ggHH_ggWWdileptonic" "ggHH_ggTauTau")
    #procs=("ttHH_ggbb" "ttHH_ggWW" "ttHH_ggTauTau" "ggH" "ttH" "VBFH" "tHq" "tHW" "VH" "ggHH_ggbb" "ggHH_ggWWsemileptonic" "ggHH_ggWWdileptonic" "ggHH_ggTauTau")
    for year in 2016 2017 2018; do
	rm -rf $trees/ws_signal_$year
	mkdir -p $trees/ws_signal_$year
	for proc in "${procs[@]}"; do
	    rm -rf $trees/$year/ws_$proc

            # You should use the same config here as in the background modeling section
	    pushd Trees2WS
		python trees2ws.py --inputConfig syst_config_ttHH_ggXX.py --inputTreeFile $trees/$year/${proc}_125.38_13TeV.root --inputMass 125.38 --productionMode $proc --year $year --doSystematics
	    popd
	    mv $trees/$year/ws_$proc/${proc}_125.38_13TeV_$proc.root $trees/ws_signal_$year/output_${proc}_M125.38_13TeV_pythia8_${proc}.root
	done

        # Configs here are on a per mapping basis
        #TODO: Have mapping updated on the fly too, not just the tag and year
        # Mappings defined here Signal/tools/replacementMap.py and Signal/tools/XSBRMap.py
	pushd Signal
	    rm -rf outdir_${tag}_$year
	    sed -i "s/dummy_tag/${tag}/g" syst_config_ttHH_ggXX.py
	    sed -i "s/dummy_year/$year/g" syst_config_ttHH_ggXX.py
	    sed -i "s/dummy_interpretation/$interpretation/g" syst_config_ttHH_ggXX.py

            python RunSignalScripts.py --inputConfig syst_config_ttHH_ggXX.py --mode fTest --modeOpts "--doPlots"
	    python RunSignalScripts.py --inputConfig syst_config_ttHH_ggXX.py --mode calcPhotonSyst
	    python RunSignalScripts.py --inputConfig syst_config_ttHH_ggXX.py --mode signalFit --groupSignalFitJobsByCat --modeOpts "--skipVertexScenarioSplit"

	    sed -i "s/${tag}/dummy_tag/g" syst_config_ttHH_ggXX.py
	    sed -i "s/$year/dummy_year/g" syst_config_ttHH_ggXX.py
	    sed -i "s/$interpretation/dummy_interpretation/g" syst_config_ttHH_ggXX.py
	popd
    done

    pushd Signal
	rm -rf outdir_packaged
        rm -rf outdir_${tag}_packaged

	python RunPackager.py --cats SR1 --exts ${tag}_2016,${tag}_2017,${tag}_2018 --batch local --massPoints 125.38 --mergeYears
	python RunPlotter.py --procs all --cats SR1 --years 2016,2017,2018 --ext packaged
	python RunPackager.py --cats SR2 --exts ${tag}_2016,${tag}_2017,${tag}_2018 --batch local --massPoints 125.38 --mergeYears
	python RunPlotter.py --procs all --cats SR2 --years 2016,2017,2018 --ext packaged

        #python RunPlotter.py --procs ttHH_ggbb --cats SR1 --years 2016,2017,2018 --ext packaged
        #python RunPlotter.py --procs ttHH_ggbb --cats SR2 --years 2016,2017,2018 --ext packaged
        #python RunPlotter.py --procs ttHH_ggWW --cats SR1 --years 2016,2017,2018 --ext packaged
        #python RunPlotter.py --procs ttHH_ggWW --cats SR2 --years 2016,2017,2018 --ext packaged
        #python RunPlotter.py --procs ttHH_ggTauTau --cats SR1 --years 2016,2017,2018 --ext packaged
        #python RunPlotter.py --procs ttHH_ggTauTau --cats SR2 --years 2016,2017,2018 --ext packaged
        #
        #python RunPlotter.py --procs VH --cats SR1 --years 2016,2017,2018 --ext packaged
        #python RunPlotter.py --procs VH --cats SR2 --years 2016,2017,2018 --ext packaged
        #python RunPlotter.py --procs ttH --cats SR1 --years 2016,2017,2018 --ext packaged
        #python RunPlotter.py --procs ttH --cats SR2 --years 2016,2017,2018 --ext packaged
        #python RunPlotter.py --procs tHq --cats SR1 --years 2016,2017,2018 --ext packaged
        #python RunPlotter.py --procs tHq --cats SR2 --years 2016,2017,2018 --ext packaged
        #python RunPlotter.py --procs tHW --cats SR1 --years 2016,2017,2018 --ext packaged
        #python RunPlotter.py --procs tHW --cats SR2 --years 2016,2017,2018 --ext packaged
        #python RunPlotter.py --procs ggH --cats SR1 --years 2016,2017,2018 --ext packaged
        #python RunPlotter.py --procs ggH --cats SR2 --years 2016,2017,2018 --ext packaged
        #python RunPlotter.py --procs VBFH --cats SR1 --years 2016,2017,2018 --ext packaged
        #python RunPlotter.py --procs VBFH --cats SR2 --years 2016,2017,2018 --ext packaged

        #python RunPlotter.py --procs ggHH_ggbb --cats SR1 --years 2016,2017,2018 --ext packaged
        #python RunPlotter.py --procs ggHH_ggbb --cats SR2 --years 2016,2017,2018 --ext packaged
        #python RunPlotter.py --procs ggHH_ggWWsemileptonic --cats SR1 --years 2016,2017,2018 --ext packaged
        #python RunPlotter.py --procs ggHH_ggWWsemileptonic --cats SR2 --years 2016,2017,2018 --ext packaged
        #python RunPlotter.py --procs ggHH_ggWWdileptonic --cats SR1 --years 2016,2017,2018 --ext packaged
        #python RunPlotter.py --procs ggHH_ggWWdileptonic --cats SR2 --years 2016,2017,2018 --ext packaged
        #python RunPlotter.py --procs ggHH_ggTauTau --cats SR1 --years 2016,2017,2018 --ext packaged
        #python RunPlotter.py --procs ggHH_ggTauTau --cats SR2 --years 2016,2017,2018 --ext packaged

        cp -a outdir_packaged outdir_${tag}_packaged
    popd
}

make_datacard(){
    #Make sure desired systematics are specified here Datacard/systematics.py
    #TODO: Check theory_uncertainties are updated for 2HDM and Tprime
    pushd Datacard
        rm -rf yields_$tag
        rm Datacard.txt

        python RunYields.py --mass "125.38" --inputWSDirMap 2016=${trees}/ws_signal_2016,2017=${trees}/ws_signal_2017,2018=${trees}/ws_signal_2018 --cats auto --procs auto --batch local --mergeYears --skipZeroes --ext $tag --doSystematics
        #python RunYields.py --mass "125.38" --inputWSDirMap 2016=${trees}/ws_signal_2016,2017=${trees}/ws_signal_2017,2018=${trees}/ws_signal_2018 --cats auto --procs "ttHH_ggbb,ttHH_ggWW,ttHH_ggTauTau" --batch local --mergeYears --skipZeroes --ext $tag --doSystematics

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
	cp ../Signal/outdir_${tag}_packaged/CMS-HGG*.root ./Models/signal/
	cp ../Background/outdir_$tag/CMS-HGG*.root ./Models/background/
	cp ../Datacard/Datacard_${tag}.txt Datacard.txt
        tail Datacard.txt

	python RunText2Workspace.py --mode $interpretation --dryRun
	./t2w_jobs/t2w_${interpretation}.sh
	rm combine_results_${tag}.txt
        common_runes=" --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2"
        #Blind
        eval "combine --redefineSignalPOI r -M AsymptoticLimits -m 125.38 -d Datacard_${interpretation}.root -n _AsymptoticLimit_r --run=blind --freezeParameters MH $common_runes > combine_results_${tag}.txt"
	eval "combine --redefineSignalPOI r -M AsymptoticLimits -m 125.38 -d Datacard_${interpretation}.root -n _AsymptoticLimit_r --run=blind --freezeParameters allConstrainedNuisances $common_runes > stat_only_${tag}.txt"
        ##Unblind
        #eval "combine --redefineSignalPOI r -M AsymptoticLimits -m 125.38 -d Datacard_${interpretation}.root -n _AsymptoticLimit_r --freezeParameters MH $common_runes > combine_results_${tag}_unblind.txt"
	#eval "combine --redefineSignalPOI r -M AsymptoticLimits -m 125.38 -d Datacard_${interpretation}.root -n _AsymptoticLimit_r --freezeParameters allConstrainedNuisances $common_runes > stat_only_${tag}_unblind.txt"

        # Likelyhood scan parts
	#combine --expectSignal 1 -t -1 --redefineSignalPOI r --cminDefaultMinimizerStrategy 0 -M MultiDimFit --algo grid --points 100 -m 125.38 -d Datacard_ggtt_resBkg_syst.root -n _Scan_r --freezeParameters MH --rMin 0 --rMax 5
	#python plotLScan.py higgsCombine_Scan_r.MultiDimFit.mH125.root
	#cp NLL_scan* /home/users/fsetti/public_html/HH2ggtautau/flashggFinalFit/$tag/

        echo "Blind"
	tail combine_results_${tag}.txt
        #echo "Unblind"
	#tail combine_results_${tag}_unblind.txt
    popd
}

syst_plots(){
    pushd Combine
        #Start by extracting the central limit (always on line 10) from the associated run tag
        line=10
        central_limit=$(sed -n "${line}p" "combine_results_${tag}.txt" | awk '{print $NF}')

	cp ../Datacard/Datacard_${tag}.txt Datacard.txt
        text2workspace.py Datacard.txt -m 125.38
	mkdir -p /home/users/iareed/public_html/ttHH/flashggFinalFit/$tag/
        common_runes=" --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2"

        eval "combineTool.py -M Impacts -d Datacard.root -m 125.38 -t -1 --setParameters r=$central_limit --redefineSignalPOI r --autoMaxPOIs 'r' --rMin -10 --rMax 200 --squareDistPoiStep --freezeParameters MH --doInitialFit $common_runes"
        eval "combineTool.py -M Impacts -d Datacard.root -m 125.38 -t -1 --setParameters r=$central_limit --redefineSignalPOI r --autoMaxPOIs 'r' --rMin -10 --rMax 200 --squareDistPoiStep --freezeParameters MH --doFits --parallel 10 $common_runes"
        rm impacts.json
        eval "combineTool.py -M Impacts -d Datacard.root -m 125.38 -t -1 --setParameters r=$central_limit --redefineSignalPOI r --autoMaxPOIs 'r' --rMin -10 --rMax 200 --squareDistPoiStep --freezeParameters MH -o impacts.json $common_runes"
        rm impacts.pdf
	plotImpacts.py -i impacts.json -o impacts
	cp impacts.pdf /home/users/iareed/public_html/ttHH/flashggFinalFit/$tag/impacts.pdf

        # For unblinding
        # GOF
        #combine -m GoodnessOfFit Datacard.txt -m 125.38 --algo=saturated -n _ttHH_SM_data --freezeParameters MH
        #combine -m GoodnessOfFit Datacard.txt -m 125.38 --algo=saturated -n _ttHH_SM_toys --freezeParameters MH --toysFreq -t 1000
        #combineTool.py -M CollectGoodnessOfFit --input higgsCombine_ttHH_SM_data.GoodnessOfFit.mH125.38.root higgsCombine_ttHH_SM_toys.GoodnessOfFit.mH125.38.123456.root -m 125.38 -o gof_SM.json
        #plotGof.py gof_SM.json --statistic saturated --mass 125.379997253 -o gof_SM_plot --title-right="SM"

        # Impacts
        eval "combineTool.py -M Impacts -d Datacard.root -m 125.38 --redefineSignalPOI r --autoMaxPOIs 'r' --rMin -10 --rMax 200 --squareDistPoiStep --freezeParameters MH --doInitialFit --robustHesse 1 --robustFit 1 $common_runes"
        eval "combineTool.py -M Impacts -d Datacard.root -m 125.38 --redefineSignalPOI r --autoMaxPOIs 'r' --rMin -10 --rMax 200 --squareDistPoiStep --freezeParameters MH --doFits --robustHesse 1 --robustFit 1 --parallel 10 $common_runes"
        rm impacts_unblind.json
        eval "combineTool.py -M Impacts -d Datacard.root -m 125.38 --redefineSignalPOI r --autoMaxPOIs 'r' --rMin -10 --rMax 200 --squareDistPoiStep --freezeParameters MH -o impacts_unblind.json $common_runes"
        rm impacts_unblind.pdf
        rm impacts_partial_unblind.pdf
	plotImpacts.py -i impacts_partial_unblind.json -o impacts_unblind
	plotImpacts.py -i impacts_partial_unblind.json -o impacts_partial_unblind --blind
	cp impacts_unblind.pdf /home/users/iareed/public_html/ttHH/flashggFinalFit/$tag/impacts_unblind.pdf
	cp impacts_partial_unblind.pdf /home/users/iareed/public_html/ttHH/flashggFinalFit/$tag/impacts_partial_unblind.pdf
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
run_combine
#syst_plots
#copy_plot
