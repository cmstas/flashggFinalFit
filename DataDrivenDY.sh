#!/usr/bin/env bash

source /cvmfs/cms.cern.ch/cmsset_default.sh
#source /vols/grid/cms/setup.sh
source setup.sh

#Path to dir with inverted selection dataset
trees=/home/users/iareed/XToYggHbb_looper/cpp/Data_04Oct23/tag_for_fggff_mx280/outputTrees

#Path to dir with nominal signal models
sig_model=/home/hep/mdk16/PhD/ggtt/ResonantGGTT/Outputs/Y_gg_Low_Mass/Interpolation

#Path to dir with nominal resonant background models
res_bkg_model=/home/hep/mdk16/PhD/ggtt/ResonantGGTT/Outputs/Y_gg_Low_Mass/ResonantBkg

#Path to dir with nominal non resonant background models
non_res_bkg_model=/dummy/path/for/now

#dy_bkg_model=/home/hep/mdk16/PhD/ggtt/ResonantGGTT/RelicDYEstimation
sig_years="2016 2017 2018"
bkg_years="combined"

proc_template="ggttres"

# Function to wait for jobs to finish, not used for local running
#wait_batch() {
#  while [[ -n $(qstat -xml | grep "${1}") ]]; do
#    echo $(qstat -xml | grep "${1}" | wc -l) "batch jobs remaining..."
#    echo $(qstat -xml -s r | grep "${1}" | wc -l) "batch jobs running..."
#    sleep 10
#  done
#}

get_mx() {
  echo $1 | cut -d'x' -f2 | cut -d'm' -f1
}
get_my() {
  echo $1 | cut -d'y' -f2
}


# Collection of envirionment variables depending on physics model
#graviton, radion, Y->tautau settings
# mggl=100
# mggh=180
# plot_blinding_region="115,135"
# get_mh() {
#   echo 125
# }
# lumiMap="lumiMap = {'2016':36.31, '2017':41.48, '2018':59.83, 'combined':137.65, 'merged':137.65}"

#low mass Y->gg settings
mggl=55
mggh=1000
plot_blinding_region="68,135"
get_mh () {
  echo $(get_my $1)
}
do_scan=1
step_sf=1
lumiMap="lumiMap = {'2016':36.31, '2017':41.48, '2018':54.67, 'combined':132.46, 'merged':132.46}"
do_dy_bkg=1

#high mass Y->gg settings
# mggl=100
# mggh=1000
# plot_blinding_region="115,900"
# get_mh () {
#   echo $(get_my $1)
# }
# do_scan=1
# step_sf=1
# lumiMap="lumiMap = {'2016':36.31, '2017':41.48, '2018':59.83, 'combined':137.65, 'merged':137.65}"

sed -i "/lumiMap/s/.*/${lumiMap}/" tools/commonObjects.py
# Find all mass points to run the DDDY for
echo "Finding mass points in: " ${trees}/${bkg_years}
for year in $bkg_years ; do
  #masses=$(python detect_mass_points.py ${trees}/${year}/)
  masses="mx280my90" #hard coded for now while debugging
done
echo "Detected mass points:" $masses


# Non essential tool, handy for a cross check
count_cats_and_crs(){
    for year in $bkg_years ; do
      pushd ${trees}/${year}
        for m in $masses ; do
          let nCats=$(echo Data*${m}* | wc -w)
          let nCR=$(echo Data*${m}*cr_* | wc -w)
          echo "Detected $nCR control regions"
          let nCats=${nCats}-${nCR} 
          echo "Detected ${nCats} categories"
          popd
        done
    done
}

# Convert input root files into workspaces
make_workspaces(){
    for year in $bkg_years ; do
        for m in $masses ; do
          echo ${PWD}
          ./get_limit_hadd_tree2ws.sh $trees $proc_template $year $m $mggl $mggh
          #qsub -q hep.q -l h_rt=300 get_limit_hadd_tree2ws.sh $trees $proc_template $year $m $mggl $mggh
        done
    done
    #wait_batch get_limit_hadd_tree2ws
}

# Model the background
model_background(){
    pushd Background
      #TODO: Stop plots from appearing on screen
      for year in $bkg_years ; do
        for m in $masses ; do
          #TODO Double check these replacements still make sense
          proc=${proc_template}${m}
          cp config_ggtt_batch.py config_ggtt_batch_${year}_${m}.py
          sed -i "s;<trees/year/m/ws/signal_year>;${trees}/${year}/${m}/ws/data_${year};g" config_ggtt_batch_${year}_${m}.py
          sed -i "s;<m>;${m};g" config_ggtt_batch_${year}_${m}.py
          #sed -i "s;<signal_year>_<m>;${year}_${m};g" config_ggtt_batch_${year}_${m}.py
          #sed -i "s;<signal_year>;${year};g" config_ggtt_batch_${year}_${m}.py
          
          mh=$(get_mh $m)
          if (( $mh < 83 )); then
            low_bound=68 #low mass exception
          else
            low_bound=$(expr ${mh} - $((1250/${mh})) )
          fi      
          high_bound=$(expr ${mh} + $((1250/${mh})) )
          python RunBackgroundScripts_lite.py --inputConfig config_ggtt_batch_${year}_${m}.py --mode fTest --modeOpts "--blindingRegion ${low_bound},${high_bound} --plotBlindingRegion ${plot_blinding_region} --gofCriteria 0.01" > /dev/null &
          sleep 0.5
        done
      done

      wait $! #waits for last background submission
      wait_batch sub_fTest

      failed_jobs=">> Failed job list \n"

      #check jobs successful
      for ((i = 0 ; i < ${nCats} ; i++)); do
        for year in $bkg_years ; do
          for m in $masses ; do
            
            proc=${proc_template}${m}
            if ! test -f outdir_ggtt_resonant_${year}_${m}/fTest/output/CMS-HGG_multipdf_${proc}cat${i}.root; then
              failed_jobs=${failed_jobs}"${year} ${m} cat${i} 0.01 -> 0.005 \n"
              echo ${year} ${m} cat${i}
              pushd outdir_ggtt_resonant_${year}_${m}/fTest/jobs
                sed -i 's/--gofCriteria 0.01/--gofCriteria 0.005/g' sub_fTest_ggtt_resonant_combined_${m}_${proc}cat${i}.sh
                #set +e
                ./sub_fTest_ggtt_resonant_combined_${m}_${proc}cat${i}.sh >> rerunning_background.log #2>&1
                #set -e
              popd
            fi

            if ! test -f outdir_ggtt_resonant_${year}_${m}/fTest/output/CMS-HGG_multipdf_${proc}cat${i}.root; then
              failed_jobs=${failed_jobs}"${year} ${m} cat${i} 0.005 -> 0.001 \n"
              pushd outdir_ggtt_resonant_${year}_${m}/fTest/jobs
                sed -i 's/--gofCriteria 0.005/--gofCriteria 0.001/g' sub_fTest_ggtt_resonant_combined_${m}_${proc}cat${i}.sh
                #set +e
                ./sub_fTest_ggtt_resonant_combined_${m}_${proc}cat${i}.sh >> rerunning_background.log 2>&1
                #set -e
              popd
            fi

            if ! test -f outdir_ggtt_resonant_${year}_${m}/fTest/output/CMS-HGG_multipdf_${proc}cat${i}.root; then
              failed_jobs=${failed_jobs}"${year} ${m} cat${i} 0.001 -> 0.0 \n"
              pushd outdir_ggtt_resonant_${year}_${m}/fTest/jobs
                sed -i 's/--gofCriteria 0.001/--gofCriteria 0.0/g' sub_fTest_ggtt_resonant_combined_${m}_${proc}cat${i}.sh
                ./sub_fTest_ggtt_resonant_combined_${m}_${proc}cat${i}.sh >> rerunning_background.log 2>&1
              popd
            fi

            #mv outdir_ggtt_resonant_${year}_${m}/fTest/output/CMS-HGG_multipdf_${proc}cat${i}.root outdir_ggtt_resonant_${year}_${m}/fTest/output/CMS-HGG_multipdf_${proc}cat${i}_${year}.root

          done
        done
      done

      for year in $bkg_years ; do
        rename .root _${year}.root outdir_ggtt_resonant_${year}_*/fTest/output/*.root
      done

      echo -e $failed_jobs
    popd
}

# Not needed for ABCD, left in for easier combination with nominal running
model_signal(){
    pushd SignalModelInterpolation
      python create_signal_ws_new_cat_2d.py -i $sig_model -o outdir --mgg-range $mggl $mggh
      python create_signal_ws_new_cat_2d_res_bkg.py -i $res_bkg_model -o res_bkg_outdir
      # if [[ -n $do_dy_bkg ]]; then 
      #   python create_signal_ws_new_cat_2d_dy_bkg.py -i $dy_bkg_model -o dy_bkg_outdir
      # fi
    popd
}

# Produce the datacard
make_datacard(){
pushd Datacard
  for m in $masses ; do
    #TODO Make this actually loop compatible
    python makeDatacardGGTT_new.py --output "Datacard_ggtt_resonant_mx280my90.txt" --MH 90.0 --MX 280.0 --MY 90.0 --doABCD --do-res-bkg
    #if [[ -n $do_dy_bkg ]]; then 
    #  ../get_limit_datacard.sh $sig_model $res_bkg_model $m $(get_mh $m) $(get_mx $m) $(get_my $m) $do_dy_bkg
    #  #qsub -q hep.q -l h_rt=1200 ../get_limit_datacard.sh $sig_model $res_bkg_model $m $(get_mh $m) $(get_mx $m) $(get_my $m) $do_dy_bkg
    #else
    #  ../get_limit_datacard.sh $sig_model $res_bkg_model $m $(get_mh $m) $(get_mx $m) $(get_my $m)
    #  #qsub -q hep.q -l h_rt=1200 ../get_limit_datacard.sh $sig_model $res_bkg_model $m $(get_mh $m) $(get_mx $m) $(get_my $m)
    #fi
  done

  #wait_batch get_limit_datacard
popd

}

# Run combine
run_combine(){
    pushd Combine
     #TODO Maybe force the removal of these dirs before creating them
     mkdir -p Models
     mkdir -p Models/signal
     mkdir -p Models/res_bkg
     #mkdir -p Models/dy_bkg
     mkdir -p Models/background

    #TODO correct pathing
    # Move signal files
     #cp /home/users/yagu/XYH/FinalFit/CMSSW_10_2_13/src/flashggFinalFit/SignalModelInterpolation/outdir/* ./Models/signal/
    #path to current signal files, produced manually from using test_first_part.sh using /home/users/yagu/XYH/XtoYH_pNN/Interpolation_forIan/model.json
     cp /home/users/iareed/CMSSW_10_2_13/src/flashggFinalFit/SignalModelInterpolation/outdir/* ./Models/signal/

    # Move resonant background files
     #cp /home/users/yagu/XYH/FinalFit/CMSSW_10_2_13/src/flashggFinalFit/SignalModelInterpolation/res_bkg_outdir/* ./Models/res_bkg/
    #path to current signal files, produced manually from using test_third_part.sh
     cp /home/users/iareed/CMSSW_10_2_13/src/flashggFinalFit/SignalModelInterpolation/res_bkg_outdir/* ./Models/res_bkg/

    #  if [[ -n $do_dy_bkg ]]; then 
    #     cp ../SignalModelInterpolation/dy_bkg_outdir/* ./Models/dy_bkg/
    #  fi
     #set +e
    # Move nominal nonresonant background
     cp /home/users/yagu/XYH/FinalFit/CMSSW_10_2_13/src/flashggFinalFit_new/Background/outdir_ggtt_resonant_mx280my90/fTest/output/* ./Models/background/

    # Move inverted nonresonant background
     cp /home/users/iareed/CMSSW_10_2_13/src/flashggFinalFit/Background/outdir_ggtt_resonant_*/fTest/output/CMS-HGG*.root ./Models/background/
     #set -e

    # Move datacard
     cp ../Datacard/Datacard_ggtt_resonant_mx280my90.txt .

     for m in $masses ; do
      ../get_limit_workspace.sh $mggl $mggh $(get_mx $m) $(get_my $m) $(get_mh $m)
      #echo "fake"
      #qsub -q hep.q -l h_rt=3600 ../get_limit_workspace.sh $mggl $mggh $(get_mx $m) $(get_my $m) $(get_mh $m)
      #qsub -q hep.q -l h_rt=7200 -pe hep.pe 16 ../get_limit_workspace.sh $mggl $mggh $(get_mx $m) $(get_my $m) $(get_mh $m)
     done

     #wait_batch get_limit_workspace

     for m in $masses ; do
      if [[ -n $do_scan ]]; then 
        #python get_mH_for_scan.py ${step_sf} ${m} ${masses}
        mh_to_scan=$(python get_mH_for_scan.py ${step_sf} ${m} ${masses})
      else
        mh_to_scan=$(get_mh $m)
      fi

      for mh_scan in $mh_to_scan ; do
        echo $mh_scan
        echo "Running combine variations"
        ../get_limit_combine.sh $mggl $mggh $(get_mx $m) $(get_my $m) $mh_scan
        #qsub -q hep.q -l h_rt=7200 ../get_limit_combine.sh $mggl $mggh $(get_mx $m) $(get_my $m) $mh_scan
        #qsub -q hep.q -l h_rt=1800 -pe hep.pe 8 ../get_limit_combine.sh $mggl $mggh $(get_mx $m) $(get_my $m) $mh_scan
      done
     done

     #wait_batch get_limit_combine

     grep 'r <' combine_results_ggtt_resonant_*.txt > combine_results_summary.txt
    popd
}

# Move plots to desired location
#TODO: Make desired location one dir/changeable
move_plots(){
    mkdir -p Outputs/CollectedPlots
    cp -r Background/plots Outputs/CollectedPlots/Background/
    mkdir -p Outputs/CollectedPlots/Combine
    mkdir -p Outputs/CollectedPlots/Combine/Datacard
    cp Combine/Datacard* Outputs/CollectedPlots/Combine/Datacard
    mkdir -p Outputs/CollectedPlots/Combine/Results
    cp Combine/combine_results* Outputs/CollectedPlots/Combine/Results
    cp -r Combine/Models Outputs/CollectedPlots/Combine/Models
    mkdir -p Outputs/CollectedPlots/Combine/Impacts
    cp Combine/impacts* Outputs/CollectedPlots/Combine/Impacts/
    mkdir -p Outputs/CollectedPlots/Combine/NLL_Scans
    cp Combine/NLL_Scan* Outputs/CollectedPlots/Combine/NLL_Scans
    mkdir -p Outputs/CollectedPlots/Background/DY
    cp Combine/ggttres*cr*.png Outputs/CollectedPlots/Background/DY
}

count_cats_and_crs
#make_workspaces
#model_background
#make_datacard
run_combine
#move_plots
