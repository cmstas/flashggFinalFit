#!/usr/bin/env bash

nToys=500
make_toys(){
    pushd Plots 
        rm -rf SplusBModels$tag
        python makeToysHH.py --inputWSFile /home/users/iareed/CMSSW_10_2_13/src/flashggFinalFit/Combine/Datacard_${interpretation}.root --ext $tag --dryRun --nToys $nToys #--dropResonantBkg
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
        python makeSplusBModelPlot.py --inputWSFile "${path}Datacard_${interpretation}.root" --inputSpecialFile "${path}Datacardspecial_${interpretation}.root" --cat "SR1" --doBands --ext $tag 
        mv SplusBModels${tag}/SR1_CMS_hgg_mass.pdf SplusBModels${tag}/SR1_CMS_hgg_mass_blind.pdf
        mv SplusBModels${tag}/SR1_CMS_hgg_mass.png SplusBModels${tag}/SR1_CMS_hgg_mass_blind.png

        python makeSplusBModelPlot.py --inputWSFile "${path}Datacard_${interpretation}.root" --inputSpecialFile "${path}Datacardspecial_${interpretation}.root" --cat "SR1" --doBands --ext $tag --unblind
        mv SplusBModels${tag}/SR1_CMS_hgg_mass.pdf SplusBModels${tag}/SR1_CMS_hgg_mass_unblind.pdf
        mv SplusBModels${tag}/SR1_CMS_hgg_mass.png SplusBModels${tag}/SR1_CMS_hgg_mass_unblind.png
 

        if (($mass < ${SR1_only})); then
            python makeSplusBModelPlot.py --inputWSFile "${path}Datacard_${interpretation}.root" --inputSpecialFile "${path}Datacardspecial_${interpretation}.root" --cat "SR2" --doBands --ext $tag 
            mv SplusBModels${tag}/SR2_CMS_hgg_mass.pdf SplusBModels${tag}/SR2_CMS_hgg_mass_blind.pdf
            mv SplusBModels${tag}/SR2_CMS_hgg_mass.png SplusBModels${tag}/SR2_CMS_hgg_mass_blind.png

            python makeSplusBModelPlot.py --inputWSFile "${path}Datacard_${interpretation}.root" --inputSpecialFile "${path}Datacardspecial_${interpretation}.root" --cat "SR2" --doBands --ext $tag --unblind
            mv SplusBModels${tag}/SR2_CMS_hgg_mass.pdf SplusBModels${tag}/SR2_CMS_hgg_mass_unblind.pdf
            mv SplusBModels${tag}/SR2_CMS_hgg_mass.png SplusBModels${tag}/SR2_CMS_hgg_mass_unblind.png
        fi

        mkdir -p /home/users/iareed/public_html/ttHH/flashggFinalFit/${tag}/Bands/
        cp SplusBModels${tag}/* /home/users/iareed/public_html/ttHH/flashggFinalFit/${tag}/Bands/
    popd
}

for mass in 550; do
#for mass in 500 550 600 650 700 750 800 850 900 950 1000 1100 1200 1300 1400 1500; do
    path=/home/users/iareed/CMSSW_10_2_13/src/flashggFinalFit/Combine/
    mass_point=M${mass}
    tag=Tprime_M${mass}_pre_app
    SR1_only=1000
    interpretation=Tprime_${mass_point}
    make_toys
    make_SpB
done
