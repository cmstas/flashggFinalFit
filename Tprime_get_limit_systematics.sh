#!/usr/bin/env bash

set -x

source /cvmfs/cms.cern.ch/cmsset_default.sh
#source /vols/grid/cms/setup.sh
cmsenv
source setup.sh

#Location of input files, also used for naming of output
#TODO: Get output naming split from tag to allow multiple runs from the same input files
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
        #procs=("TprimeBB${mass_point}" "ggH" )
        #procs=("TprimeBB${mass_point}" "ttHHggbb" "ggH")
        procs=("TprimeBB${mass_point}" "TprimeWW${mass_point}" "TprimeTAUTAU${mass_point}" "ttHHggbb" "ttHHggWW" "ttHHggTauTau" "ggH" "ttH" "VBFH" "VH" "HHGGbb" "HHGGWWsemileptonic" "HHGGWWdileptonic" "HHGGTauTau")
	for year in 2016 2017 2018
	do
		rm -rf $trees/ws_signal_$year
		mkdir -p $trees/ws_signal_$year
		for proc in "${procs[@]}"
		do
			rm -rf $trees/$year/ws_$proc

                        # You should use the same config here as in the background modeling section
			pushd Trees2WS
				python trees2ws.py --inputConfig syst_config_ttHH_ggXX.py --inputTreeFile $trees/$year/${proc}_125_13TeV.root --inputMass 125 --productionMode $proc --year $year --doSystematics
			popd

			mv $trees/$year/ws_$proc/${proc}_125_13TeV_$proc.root $trees/ws_signal_$year/output_${proc}_M125_13TeV_pythia8_${proc}.root 
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
		    python RunSignalScripts.py --inputConfig syst_config_ttHH_ggXX.py --mode signalFit --groupSignalFitJobsByCat --modeOpts "--skipVertexScenarioSplit "

	            sed -i "s/${tag}/dummy_tag/g" syst_config_ttHH_ggXX.py
	            sed -i "s/$year/dummy_year/g" syst_config_ttHH_ggXX.py
	            sed -i "s/$interpretation/dummy_interpretation/g" syst_config_ttHH_ggXX.py
	    	popd
	done

	pushd Signal	
		rm -rf outdir_packaged
                rm -rf outdir_${tag}_packaged

		python RunPackager.py --cats SR1 --exts ${tag}_2016,${tag}_2017,${tag}_2018 --batch local --massPoints 125 --mergeYears
		python RunPlotter.py --procs all --cats SR1 --years 2016,2017,2018 --ext packaged
		python RunPackager.py --cats SR2 --exts ${tag}_2016,${tag}_2017,${tag}_2018 --batch local --massPoints 125 --mergeYears
		python RunPlotter.py --procs all --cats SR2 --years 2016,2017,2018 --ext packaged

                python RunPlotter.py --procs TprimeBB${mass_point} --cats SR1 --years 2016,2017,2018 --ext packaged
                python RunPlotter.py --procs TprimeBB${mass_point} --cats SR2 --years 2016,2017,2018 --ext packaged
                python RunPlotter.py --procs TprimeWW${mass_point} --cats SR1 --years 2016,2017,2018 --ext packaged
                python RunPlotter.py --procs TprimeWW${mass_point} --cats SR2 --years 2016,2017,2018 --ext packaged
                python RunPlotter.py --procs TprimeTAUTAU${mass_point} --cats SR1 --years 2016,2017,2018 --ext packaged
                python RunPlotter.py --procs TprimeTAUTAU${mass_point} --cats SR2 --years 2016,2017,2018 --ext packaged

                python RunPlotter.py --procs ttHHggbb --cats SR1 --years 2016,2017,2018 --ext packaged
                python RunPlotter.py --procs ttHHggbb --cats SR2 --years 2016,2017,2018 --ext packaged
                python RunPlotter.py --procs ttHHggWW --cats SR1 --years 2016,2017,2018 --ext packaged
                python RunPlotter.py --procs ttHHggWW --cats SR2 --years 2016,2017,2018 --ext packaged
                python RunPlotter.py --procs ttHHggTauTau --cats SR1 --years 2016,2017,2018 --ext packaged
                python RunPlotter.py --procs ttHHggTauTau --cats SR2 --years 2016,2017,2018 --ext packaged
                    
                python RunPlotter.py --procs VH --cats SR1 --years 2016,2017,2018 --ext packaged
                python RunPlotter.py --procs VH --cats SR2 --years 2016,2017,2018 --ext packaged
                python RunPlotter.py --procs ttH --cats SR1 --years 2016,2017,2018 --ext packaged
                python RunPlotter.py --procs ttH --cats SR2 --years 2016,2017,2018 --ext packaged
                python RunPlotter.py --procs ggH --cats SR1 --years 2016,2017,2018 --ext packaged
                python RunPlotter.py --procs ggH --cats SR2 --years 2016,2017,2018 --ext packaged
                python RunPlotter.py --procs VBFH --cats SR1 --years 2016,2017,2018 --ext packaged
                python RunPlotter.py --procs VBFH --cats SR2 --years 2016,2017,2018 --ext packaged

                python RunPlotter.py --procs HHGGbb --cats SR1 --years 2016,2017,2018 --ext packaged
                python RunPlotter.py --procs HHGGbb --cats SR2 --years 2016,2017,2018 --ext packaged
                python RunPlotter.py --procs HHGGWWsemileptonic --cats SR1 --years 2016,2017,2018 --ext packaged
                python RunPlotter.py --procs HHGGWWsemileptonic --cats SR2 --years 2016,2017,2018 --ext packaged
                python RunPlotter.py --procs HHGGWWdileptonic --cats SR1 --years 2016,2017,2018 --ext packaged
                python RunPlotter.py --procs HHGGWWdileptonic --cats SR2 --years 2016,2017,2018 --ext packaged
                python RunPlotter.py --procs HHGGTauTau --cats SR1 --years 2016,2017,2018 --ext packaged
                python RunPlotter.py --procs HHGGTauTau --cats SR2 --years 2016,2017,2018 --ext packaged

                cp -a outdir_packaged outdir_${tag}_packaged
	popd
}

make_datacard(){
        #Make usre desired systematics are specified here Datacard/systematics.py
        #TODO: Check theory_uncertainties are updated for 2HDM and Tprime
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
		cp ../Signal/outdir_${tag}_packaged/CMS-HGG*.root ./Models/signal/
		cp ../Background/outdir_$tag/CMS-HGG*.root ./Models/background/
		cp ../Datacard/Datacard_${tag}.txt Datacard.txt
		
                python RunText2Workspace.py --mode $interpretation --dryRun
		./t2w_jobs/t2w_${interpretation}.sh

#		combine --expectSignal 1 -t -1 --redefineSignalPOI r --cminDefaultMinimizerStrategy 0 -M AsymptoticLimits -m 125 -d Datacard_ttHHggXX.root -n _AsymptoticLimit_r --freezeParameters MH --run=blind > combine_results_${tag}.txt
#		combine --expectSignal 1 -t -1 --redefineSignalPOI r --cminDefaultMinimizerStrategy 0 -M AsymptoticLimits -m 125 -d Datacard_ttHHggXX.root -n _AsymptoticLimit_r --freezeParameters allConstrainedNuisances --run=blind > stat_only_${tag}.txt
		combine --redefineSignalPOI r  -M AsymptoticLimits -m 125 -d Datacard_${interpretation}.root -n _AsymptoticLimit_r --freezeParameters MH --run=blind > combine_results_${tag}.txt --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2
		combine --redefineSignalPOI r  -M AsymptoticLimits -m 125 -d Datacard_${interpretation}.root -n _AsymptoticLimit_r --freezeParameters allConstrainedNuisances --run=blind > stat_only_${tag}.txt --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2


                # Likelyhood scan parts
		#combine --expectSignal 1 -t -1 --redefineSignalPOI r --cminDefaultMinimizerStrategy 0 -M MultiDimFit --algo grid --points 100 -m 125 -d Datacard_ggtt_resBkg_syst.root -n _Scan_r --freezeParameters MH --rMin 0 --rMax 5
		#python plotLScan.py higgsCombine_Scan_r.MultiDimFit.mH125.root
		#cp NLL_scan* /home/users/fsetti/public_html/HH2ggtautau/flashggFinalFit/$tag/

		tail combine_results_${tag}.txt
	popd	
}

syst_plots(){
	pushd Combine
                #Start by extracting the central limit (always on line 10) from the associated run tag
                line=10
                central_limit=$(sed -n "${line}p" "combine_results_${tag}.txt" | awk '{print $NF}')


		text2workspace.py Datacard.txt -m 125
		combineTool.py  --setParameters r=$central_limit -t -1 -M Impacts -d Datacard.root --redefineSignalPOI r --autoMaxPOIs "r" --rMin -10 --rMax 200 --squareDistPoiStep -m 125 --freezeParameters MH --doInitialFit --robustFit 1 --robustHesse 1 --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2
		combineTool.py  --setParameters r=$central_limit -t -1 -M Impacts -d Datacard.root --redefineSignalPOI r --autoMaxPOIs "r" --rMin -10 --rMax 200 --squareDistPoiStep -m 125 --freezeParameters MH --robustFit 1 --robustHesse 1 --doFits --parallel 10 --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2
		#combineTool.py  --setParameters r=1.0 -t -1 -M Impacts -d Datacard.root --redefineSignalPOI r --autoMaxPOIs "r" --rMin -10 --rMax 300 --squareDistPoiStep --cminDefaultMinimizerStrategy 0 -m 125 --freezeParameters MH --doInitialFit --robustFit 1 --robustHesse 1
		#combineTool.py  --setParameters r=1.0 -t -1 -M Impacts -d Datacard.root --redefineSignalPOI r --autoMaxPOIs "r" --rMin -10 --rMax 300 --squareDistPoiStep --cminDefaultMinimizerStrategy 0 -m 125 --freezeParameters MH --robustFit 1 --robustHesse 1 --doFits --parallel 10


		#combineTool.py  -t -1 --setParameters r=100.0 -M Impacts -d Datacard.root --redefineSignalPOI r --squareDistPoiStep --cminDefaultMinimizerStrategy 0 -m 125 --freezeParameters MH --doInitialFit --robustFit 1
		#combineTool.py  -t -1 --setParameters r=100.0 -M Impacts -d Datacard.root --redefineSignalPOI r --squareDistPoiStep --cminDefaultMinimizerStrategy 0 -m 125 --freezeParameters MH --robustFit 1   --doFits --parallel 10
                rm impacts.json
		combineTool.py -M Impacts -d Datacard.root --redefineSignalPOI r --autoMaxPOIs "r" --setParameters r=$central_limit -t -1 --rMin -10 --rMax 200 --squareDistPoiStep -m 125 --freezeParameters MH -o impacts.json --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2
		#combineTool.py -M Impacts -d Datacard.root --redefineSignalPOI r --autoMaxPOIs "r" --setParameters r=260.0 -t -1 --rMin -10 --rMax 300 --squareDistPoiStep --cminDefaultMinimizerStrategy 0 -m 125 --freezeParameters MH -o impacts.json 

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
	cp Signal/outdir_${tag}_packaged/Plots/* /home/users/iareed/public_html/ttHH/flashggFinalFit/$tag/Signal
	cp /home/users/iareed/public_html/ttHH/index.php /home/users/iareed/public_html/ttHH/flashggFinalFit/$tag/Signal
}

for mass in 500 550 600 650 700 750 800 850 900 950 1000 1100
do
    mass_point=M${mass}
    tag=Tprime_${mass_point}_22Sep23_fixed_dijet_dummies

    #Identify which interpretation is being done in the analysis, needed a different name for clarity
    interpretation=Tprime_${mass_point}

    #Path to all input locations
    trees=/home/users/iareed/CMSSW_10_2_13/src/flashggFinalFit/files_systs/$tag/

    #model_bkg
    model_sig
    #make_datacard
    #run_combine
    #syst_plots
    copy_plot
done

