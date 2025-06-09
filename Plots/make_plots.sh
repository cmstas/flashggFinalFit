#!/usr/bin/env bash


tag=mx1000my125

nToys=5000
make_toys(){
    pushd Plots 
        rm -rf SplusBModels$tag
	#python makeToysHH.py --inputWSFile /home/users/yagu/XYH/XtoYH_sys/plots_2023-12-19_CategorizationAndPreselSFCorrected/CMSSW_10_2_13/src/flashggFinalFit/higgsCombine_MultiDimFit_r_ggbbres_mx1000my125mh125.MultiDimFit.mH125.root --ext $tag --dryRun --nToys $nToys
        python makeToysHH.py --inputWSFile /home/users/yagu/XYH/XtoYH_sys/plots_2023-12-19_CategorizationAndPreselSFCorrected/CMSSW_10_2_13/src/flashggFinalFit/higgsCombine_MultiDimFit_r_ggbbres_mx1000my125mh125.MultiDimFit.mH125.root --ext $tag --dryRun --nToys $nToys #--loadSnapshot MultiDimFit #--dropResonantBkg
        #python makeToysHH.py --inputWSFile /home/users/iareed/CMSSW_10_2_13/src/flashggFinalFit/Combine/Datacard_ttHHggXX.root --ext $tag --dryRun --nToys $nToys #--dropResonantBkg
        iter=0
        while [ $iter -lt $nToys ]
        do 
            ./SplusBModels${tag}/toys/jobs/sub_toy_$(($iter+1)).sh &
            ./SplusBModels${tag}/toys/jobs/sub_toy_$(($iter+2)).sh &
            ./SplusBModels${tag}/toys/jobs/sub_toy_$(($iter+3)).sh &
            ./SplusBModels${tag}/toys/jobs/sub_toy_$(($iter+4)).sh &
            ./SplusBModels${tag}/toys/jobs/sub_toy_$(($iter+5)).sh &
            ./SplusBModels${tag}/toys/jobs/sub_toy_$(($iter+6)).sh &
            ./SplusBModels${tag}/toys/jobs/sub_toy_$(($iter+7)).sh &
            ./SplusBModels${tag}/toys/jobs/sub_toy_$(($iter+8)).sh &
            ./SplusBModels${tag}/toys/jobs/sub_toy_$(($iter+9)).sh &
            ./SplusBModels${tag}/toys/jobs/sub_toy_$iter.sh
            iter=$(($iter+10))
        done
    popd
}

make_SpB(){
    pushd Plots
        #python makeSplusBModelPlot.py --inputWSFile /home/users/yagu/XYH/XtoYH_sys/plots_2023-12-19_CategorizationAndPreselSFCorrected/CMSSW_10_2_13/src/flashggFinalFit/higgsCombine_MultiDimFit_r_ggbbres_mx1000my125mh125.MultiDimFit.mH125.root --inputSpecialFile /home/users/yagu/XYH/XtoYH_sys/plots_2023-12-19_CategorizationAndPreselSFCorrected/CMSSW_10_2_13/src/flashggFinalFit/higgsCombine_MultiDimFit_r_ggbbres_mx1000my125mh125.MultiDimFit.mH125.root --cat "cat0" --doBands --ext $tag --unblind # --parameterMap "singleH:1,doubleH:1"
        python makeSplusBModelPlot.py --inputWSFile /home/users/yagu/XYH/XtoYH_sys/plots_2023-12-19_CategorizationAndPreselSFCorrected/CMSSW_10_2_13/src/flashggFinalFit/higgsCombine_MultiDimFit_r_ggbbres_mx1000my125mh125.MultiDimFit.mH125.root --inputSpecialFile /home/users/yagu/XYH/XtoYH_sys/plots_2023-12-19_CategorizationAndPreselSFCorrected/CMSSW_10_2_13/src/flashggFinalFit/higgsCombine_MultiDimFit_r_ggbbres_mx1000my125mh125.MultiDimFit.mH125.root --cat "cat0" --doBands --ext $tag --unblind #--loadSnapshot MultiDimFit # --parameterMap "singleH:1,doubleH:1"
        ##python makeSplusBModelPlot.py --inputWSFile /home/users/iareed/CMSSW_10_2_13/src/flashggFinalFit/Combine/Datacard_ttHHggXX.root --cat "SR1" --doBands --ext $tag # --parameterMap "singleH:1,doubleH:1"
        #mv SplusBModels${tag}/SR1_CMS_hgg_mass.pdf SplusBModels${tag}/SR1_CMS_hgg_mass_blind.pdf
        #mv SplusBModels${tag}/SR1_CMS_hgg_mass.png SplusBModels${tag}/SR1_CMS_hgg_mass_blind.png
        #mv SplusBModels${tag}/SR2_CMS_hgg_mass.pdf SplusBModels${tag}/SR2_CMS_hgg_mass_blind.pdf
        #mv SplusBModels${tag}/SR2_CMS_hgg_mass.png SplusBModels${tag}/SR2_CMS_hgg_mass_blind.png

        ##python makeSplusBModelPlot.py --inputWSFile /home/users/iareed/CMSSW_10_2_13/src/flashggFinalFit/Combine/Datacard_ttHHggXX.root --cat "SR1" --doBands --ext $tag --unblind # --parameterMap "singleH:1,doubleH:1"
        ##python makeSplusBModelPlot.py --inputWSFile /home/users/iareed/CMSSW_10_2_13/src/flashggFinalFit/Combine/Datacard_Tprime_M500.root --cat "SR1" --doBands --ext $tag --unblind # --parameterMap "singleH:1,doubleH:1"
        #mv SplusBModels${tag}/SR1_CMS_hgg_mass.pdf SplusBModels${tag}/SR1_CMS_hgg_mass_unblind.pdf
        #mv SplusBModels${tag}/SR1_CMS_hgg_mass.png SplusBModels${tag}/SR1_CMS_hgg_mass_unblind.png
        #mv SplusBModels${tag}/SR2_CMS_hgg_mass.pdf SplusBModels${tag}/SR2_CMS_hgg_mass_unblind.pdf
        #mv SplusBModels${tag}/SR2_CMS_hgg_mass.png SplusBModels${tag}/SR2_CMS_hgg_mass_unblind.png
        #cp SplusBModels${tag}/* /home/users/iareed/public_html/ttHH/flashggFinalFit/${tag}/Bands/
    popd
}

make_toys
make_SpB
