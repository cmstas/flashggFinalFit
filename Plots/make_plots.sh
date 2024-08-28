#!/usr/bin/env bash


tag=Tprime_M550_pre_app
#tag=SM_pre_app_20240523
trees=/home/users/iareed/CMSSW_10_2_13/src/flashggFinalFit/files_systs/$tag/

nToys=50
make_toys(){
    pushd Plots 
        rm -rf SplusBModels$tag
        python makeToysHH.py --inputWSFile /home/users/iareed/CMSSW_10_2_13/src/flashggFinalFit/Combine/Datacard_Tprime_M500_full.root --ext $tag --dryRun --nToys $nToys #--dropResonantBkg
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
        python makeSplusBModelPlot.py --inputWSFile /home/users/iareed/CMSSW_10_2_13/src/flashggFinalFit/Combine/Datacard_Tprime_M${mass}.root --inputSpecialFile /home/users/iareed/CMSSW_10_2_13/src/flashggFinalFit/Combine/Datacardspecial_Tprime_M${mass}.root --cat "SR1" --doBands --ext $tag # --parameterMap "singleH:1,doubleH:1"
        #python makeSplusBModelPlot.py --inputWSFile /home/users/iareed/CMSSW_10_2_13/src/flashggFinalFit/Combine/Datacard_ttHHggXX.root --cat "SR1" --doBands --ext $tag # --parameterMap "singleH:1,doubleH:1"
        mv SplusBModels${tag}/SR1_CMS_hgg_mass.pdf SplusBModels${tag}/SR1_CMS_hgg_mass_blind.pdf
        mv SplusBModels${tag}/SR1_CMS_hgg_mass.png SplusBModels${tag}/SR1_CMS_hgg_mass_blind.png
        mv SplusBModels${tag}/SR2_CMS_hgg_mass.pdf SplusBModels${tag}/SR2_CMS_hgg_mass_blind.pdf
        mv SplusBModels${tag}/SR2_CMS_hgg_mass.png SplusBModels${tag}/SR2_CMS_hgg_mass_blind.png

        #python makeSplusBModelPlot.py --inputWSFile /home/users/iareed/CMSSW_10_2_13/src/flashggFinalFit/Combine/Datacard_ttHHggXX.root --cat "SR1" --doBands --ext $tag --unblind # --parameterMap "singleH:1,doubleH:1"
        #python makeSplusBModelPlot.py --inputWSFile /home/users/iareed/CMSSW_10_2_13/src/flashggFinalFit/Combine/Datacard_Tprime_M500.root --cat "SR1" --doBands --ext $tag --unblind # --parameterMap "singleH:1,doubleH:1"
        mv SplusBModels${tag}/SR1_CMS_hgg_mass.pdf SplusBModels${tag}/SR1_CMS_hgg_mass_unblind.pdf
        mv SplusBModels${tag}/SR1_CMS_hgg_mass.png SplusBModels${tag}/SR1_CMS_hgg_mass_unblind.png
        mv SplusBModels${tag}/SR2_CMS_hgg_mass.pdf SplusBModels${tag}/SR2_CMS_hgg_mass_unblind.pdf
        mv SplusBModels${tag}/SR2_CMS_hgg_mass.png SplusBModels${tag}/SR2_CMS_hgg_mass_unblind.png
        cp SplusBModels${tag}/* /home/users/iareed/public_html/ttHH/flashggFinalFit/${tag}/Bands/
    popd
}

#make_toys
make_SpB
