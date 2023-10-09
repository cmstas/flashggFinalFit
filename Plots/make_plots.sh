#!/usr/bin/env bash

set -x

#source /cvmfs/cms.cern.ch/cmsset_default.sh
#source /vols/grid/cms/setup.sh

tag=SM_22Sep23_fixed_dijet_dummies
trees=/home/users/iareed/CMSSW_10_2_13/src/flashggFinalFit/files_systs/$tag/

#cmsenv
#source setup.sh

nToys=10

make_toys(){
    pushd Plots 
        rm -rf SplusBModels$tag
        python makeToysHH.py --inputWSFile /home/users/iareed/CMSSW_10_2_13/src/flashggFinalFit/Combine/Datacard_ttHHggXX.root --ext $tag --dryRun --nToys $nToys --dropResonantBkg
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
        python makeSplusBModelPlot.py --inputWSFile /home/users/iareed/CMSSW_10_2_13/src/flashggFinalFit/Combine/Datacard_ttHHggXX.root --cat "SR1" --doBands --ext $tag #--parameterMap r:0 #--parameterMap ".*/ttHHggbb.*:r[1,0,2]"
#        python makeSplusBModelPlot.py --inputWSFile /home/users/iareed/CMSSW_10_2_13/src/flashggFinalFit/Combine/Datacard_ttHHggXX.root --cat "SR2" --doBands --ext $tag #--parameterMap r:0 #--parameterMap ".*/ttHHggbb.*:r[1,0,2]"

        cp SplusBModels$tag/*.png /home/users/iareed/public_html/ttHH/flashggFinalFit/$tag/Bands/
    popd        

}

make_toys
make_SpB
