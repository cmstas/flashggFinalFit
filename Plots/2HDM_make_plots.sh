#!/usr/bin/env bash

nToys=100
make_toys(){
    pushd Plots 
        rm -rf SplusBModels$tag
        python makeToysHH.py --inputWSFile /home/users/iareed/CMSSW_10_2_13/src/flashggFinalFit/Combine/Datacard_${interpretation}.root --ext $tag --dryRun --nToys $nToys #--dropResonantBkg
        #python makeToysHH.py --inputWSFile /home/users/iareed/CMSSW_10_2_13/src/flashggFinalFit/Combine/higgsCombinestandard.MultiDimFit.mH125.38.root --ext $tag --dryRun --nToys $nToys --loadSnapshot MultiDimFit #--dropResonantBkg
        #python makeToysHH.py --inputWSFile /home/users/iareed/CMSSW_10_2_13/src/flashggFinalFit/Combine/Datacard_ttHHggXX.root --ext $tag --dryRun --nToys $nToys #--dropResonantBkg
        iter=0
        while [ $iter -lt $nToys ]
        do 
            ./SplusBModels${tag}/toys/jobs/sub_toy_$(($iter)).sh &
            ./SplusBModels${tag}/toys/jobs/sub_toy_$(($iter+1)).sh &
            ./SplusBModels${tag}/toys/jobs/sub_toy_$(($iter+2)).sh &
            ./SplusBModels${tag}/toys/jobs/sub_toy_$(($iter+3)).sh &
            ./SplusBModels${tag}/toys/jobs/sub_toy_$(($iter+4)).sh &
            ./SplusBModels${tag}/toys/jobs/sub_toy_$(($iter+5)).sh &
            ./SplusBModels${tag}/toys/jobs/sub_toy_$(($iter+6)).sh &
            ./SplusBModels${tag}/toys/jobs/sub_toy_$(($iter+7)).sh &
            ./SplusBModels${tag}/toys/jobs/sub_toy_$(($iter+8)).sh &
            ./SplusBModels${tag}/toys/jobs/sub_toy_$(($iter+9)).sh &
            ./SplusBModels${tag}/toys/jobs/sub_toy_$(($iter+10)).sh &
            ./SplusBModels${tag}/toys/jobs/sub_toy_$(($iter+11)).sh &
            ./SplusBModels${tag}/toys/jobs/sub_toy_$(($iter+12)).sh &
            ./SplusBModels${tag}/toys/jobs/sub_toy_$(($iter+13)).sh &
            ./SplusBModels${tag}/toys/jobs/sub_toy_$(($iter+14)).sh &
            ./SplusBModels${tag}/toys/jobs/sub_toy_$(($iter+15)).sh &
            ./SplusBModels${tag}/toys/jobs/sub_toy_$(($iter+16)).sh &
            ./SplusBModels${tag}/toys/jobs/sub_toy_$(($iter+17)).sh &
            ./SplusBModels${tag}/toys/jobs/sub_toy_$(($iter+18)).sh &
            ./SplusBModels${tag}/toys/jobs/sub_toy_$(($iter+19)).sh &
            ./SplusBModels${tag}/toys/jobs/sub_toy_$(($iter+20)).sh &
            ./SplusBModels${tag}/toys/jobs/sub_toy_$(($iter+21)).sh &
            ./SplusBModels${tag}/toys/jobs/sub_toy_$(($iter+22)).sh &
            ./SplusBModels${tag}/toys/jobs/sub_toy_$(($iter+23)).sh &
            ./SplusBModels${tag}/toys/jobs/sub_toy_$(($iter+24)).sh &
            ./SplusBModels${tag}/toys/jobs/sub_toy_$(($iter+25)).sh &
            ./SplusBModels${tag}/toys/jobs/sub_toy_$(($iter+26)).sh &
            ./SplusBModels${tag}/toys/jobs/sub_toy_$(($iter+27)).sh &
            ./SplusBModels${tag}/toys/jobs/sub_toy_$(($iter+28)).sh &
            ./SplusBModels${tag}/toys/jobs/sub_toy_$(($iter+29)).sh &
            ./SplusBModels${tag}/toys/jobs/sub_toy_$(($iter+30)).sh &
            ./SplusBModels${tag}/toys/jobs/sub_toy_$(($iter+31)).sh &
            ./SplusBModels${tag}/toys/jobs/sub_toy_$(($iter+32)).sh &
            ./SplusBModels${tag}/toys/jobs/sub_toy_$(($iter+33)).sh &
            ./SplusBModels${tag}/toys/jobs/sub_toy_$(($iter+34)).sh &
            ./SplusBModels${tag}/toys/jobs/sub_toy_$(($iter+35)).sh &
            ./SplusBModels${tag}/toys/jobs/sub_toy_$(($iter+36)).sh &
            ./SplusBModels${tag}/toys/jobs/sub_toy_$(($iter+37)).sh &
            ./SplusBModels${tag}/toys/jobs/sub_toy_$(($iter+38)).sh &
            ./SplusBModels${tag}/toys/jobs/sub_toy_$(($iter+39)).sh &
            ./SplusBModels${tag}/toys/jobs/sub_toy_$(($iter+40)).sh &
            ./SplusBModels${tag}/toys/jobs/sub_toy_$(($iter+41)).sh &
            ./SplusBModels${tag}/toys/jobs/sub_toy_$(($iter+42)).sh &
            ./SplusBModels${tag}/toys/jobs/sub_toy_$(($iter+43)).sh &
            ./SplusBModels${tag}/toys/jobs/sub_toy_$(($iter+44)).sh &
            ./SplusBModels${tag}/toys/jobs/sub_toy_$(($iter+45)).sh &
            ./SplusBModels${tag}/toys/jobs/sub_toy_$(($iter+46)).sh &
            ./SplusBModels${tag}/toys/jobs/sub_toy_$(($iter+47)).sh &
            ./SplusBModels${tag}/toys/jobs/sub_toy_$(($iter+48)).sh &
            ./SplusBModels${tag}/toys/jobs/sub_toy_$(($iter+49)).sh &
            iter=$(($iter+50))
            wait
        done
    popd
}

make_SpB(){
    pushd Plots 
        #python makeSplusBModelPlot.py --inputWSFile "${path}Datacard_${interpretation}.root" --inputSpecialFile "${path}Datacardspecial_${interpretation}.root" --cat "SR1" --doBands --ext $tag 
        #mv SplusBModels${tag}/SR1_CMS_hgg_mass.pdf SplusBModels${tag}/SR1_CMS_hgg_mass_blind.pdf
        #mv SplusBModels${tag}/SR1_CMS_hgg_mass.png SplusBModels${tag}/SR1_CMS_hgg_mass_blind.png

        #python makeSplusBModelPlot.py --inputWSFile "/home/users/iareed/CMSSW_10_2_13/src/flashggFinalFit/Combine/higgsCombinestandard.MultiDimFit.mH125.38.root" --inputSpecialFile "/home/users/iareed/CMSSW_10_2_13/src/flashggFinalFit/Combine/higgsCombinespecial.MultiDimFit.mH125.38.root" --cat "SR1" --doBands --ext $tag --unblind --loadSnapshot MultiDimFit
        python makeSplusBModelPlot.py --inputWSFile "${path}Datacard_${interpretation}.root" --inputSpecialFile "${path}Datacard_${interpretation}.root" --cat "SR1" --doBands --ext $tag --unblind
        #python makeSplusBModelPlot.py --inputWSFile "${path}Datacard_${interpretation}.root" --inputSpecialFile "${path}Datacardspecial_${interpretation}.root" --cat "SR1" --doBands --ext $tag --unblind
        mv SplusBModels${tag}/SR1_CMS_hgg_mass.pdf SplusBModels${tag}/SR1_CMS_hgg_mass_unblind.pdf
        mv SplusBModels${tag}/SR1_CMS_hgg_mass.png SplusBModels${tag}/SR1_CMS_hgg_mass_unblind.png

        #python makeSplusBModelPlot.py --inputWSFile "${path}Datacard_${interpretation}.root" --inputSpecialFile "${path}Datacardspecial_${interpretation}.root" --cat "SR2" --doBands --ext $tag 
        #mv SplusBModels${tag}/SR2_CMS_hgg_mass.pdf SplusBModels${tag}/SR2_CMS_hgg_mass_blind.pdf
        #mv SplusBModels${tag}/SR2_CMS_hgg_mass.png SplusBModels${tag}/SR2_CMS_hgg_mass_blind.png

        python makeSplusBModelPlot.py --inputWSFile "${path}Datacard_${interpretation}.root" --inputSpecialFile "${path}Datacardspecial_${interpretation}.root" --cat "SR2" --doBands --ext $tag --unblind
        mv SplusBModels${tag}/SR2_CMS_hgg_mass.pdf SplusBModels${tag}/SR2_CMS_hgg_mass_unblind.pdf
        mv SplusBModels${tag}/SR2_CMS_hgg_mass.png SplusBModels${tag}/SR2_CMS_hgg_mass_unblind.png

        mkdir -p /home/users/iareed/public_html/ttHH/flashggFinalFit/${tag}/Bands/
        cp SplusBModels${tag}/* /home/users/iareed/public_html/ttHH/flashggFinalFit/${tag}/Bands/
    popd
}

for mass in 250; do # 275 300 325 350; do
    path=/home/users/iareed/CMSSW_10_2_13/src/flashggFinalFit/Combine/
    mass_point=M${mass}
    tag=2HDM_M${mass}_pre_app_1108_unblind
    interpretation=2HDM_${mass_point}
    #make_toys
    make_SpB
done
