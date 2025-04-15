To perform limit plot in the paper, 
python plot_limits.py --inputFile Combine/summary_combine_results_ggbbres_best_version.txt --outputFile Interpolation_extra_masses_no_trim_obs_v8 --doObserved

To make SpB fit plot
cd Plots
 . make_plots_mx280my90.sh 

To test combine fit for a certain mass points:
combine --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 --redefineSignalPOI r -M AsymptoticLimits -m 450 -d Datacard_ggbbres_mx650my450_ggbbres.root -n _AsymptoticLimit_r_ggbbres_mx650my450mh450 --freezeParameters MH,MX,MY --setParameters MX=650,MY=450,MH=450 > combine_results_ggbbres_mx650my450mh450_check0.txt
