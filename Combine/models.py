models = {
  "mu_inclusive":"",

	"ggtt_resBkg":"-P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
  --PO \"map=.*/HH2ggtautau.*:r[1,0,2]\"",

	#"ggtt_resBkg_syst":"-P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
	#--PO \"map=.*/HHggTauTau.*:r[1,0,2]\"",

# "ggtt_resBkg_syst":"-P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
#  --pO \"map=.*/2HDM_ggbb_M250.*:r[1,0,2]\" \
#  --pO \"map=.*/2HDM_ggWW_M250.*:r[1,0,2]\" \
#  --PO \"map=.*/2HDM_ggTauTau_M250.*:r[1,0,2]\"",


# "ggtt_resBkg_syst":"-P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
#  --PO \"map=.*/HHgg*.*:r[1,0,2]\"",

 "ttHHggXX":"-P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
  --PO \"map=.*/ttHH_ggbb.*:r[1,0,200]\" \
  --PO \"map=.*/ttHH_ggWW.*:r[1,0,200]\" \
  --PO \"map=.*/ttHH_ggTauTau.*:r[1,0,200]\"",

 "2HDM_M250":"-P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
  --PO \"map=.*/2HDM_ggbb_M250.*:r[1,0,200]\" \
  --PO \"map=.*/2HDM_ggWW_M250.*:r[1,0,200]\" \
  --PO \"map=.*/2HDM_ggTauTau_M250.*:r[1,0,200]\"",

"2HDM_M275":"-P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
  --PO \"map=.*/2HDM_ggbb_M275.*:r[1,0,200]\" \
  --PO \"map=.*/2HDM_ggWW_M275.*:r[1,0,200]\" \
  --PO \"map=.*/2HDM_ggTauTau_M275.*:r[1,0,200]\"",

 "2HDM_M300":"-P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
  --PO \"map=.*/2HDM_ggbb_M300.*:r[1,0,200]\" \
  --PO \"map=.*/2HDM_ggWW_M300.*:r[1,0,200]\" \
  --PO \"map=.*/2HDM_ggTauTau_M300.*:r[1,0,200]\"",

"2HDM_M325":"-P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
  --PO \"map=.*/2HDM_ggbb_M325.*:r[1,0,200]\" \
  --PO \"map=.*/2HDM_ggWW_M325.*:r[1,0,200]\" \
  --PO \"map=.*/2HDM_ggTauTau_M325.*:r[1,0,200]\"",

 "2HDM_M350":"-P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
  --PO \"map=.*/2HDM_ggbb_M350.*:r[1,0,200]\" \
  --PO \"map=.*/2HDM_ggWW_M350.*:r[1,0,200]\" \
  --PO \"map=.*/2HDM_ggTauTau_M350.*:r[1,0,200]\"",

 "Tprime_M500":"-P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
  --PO \"map=.*/Tprime_ggbb_M500.*:r[1,0,200]\" \
  --PO \"map=.*/Tprime_ggWW_M500.*:r[1,0,200]\" \
  --PO \"map=.*/Tprime_ggTauTau_M500.*:r[1,0,200]\"",

 "Tprime_M550":"-P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
  --PO \"map=.*/Tprime_ggbb_M550.*:r[1,0,200]\" \
  --PO \"map=.*/Tprime_ggWW_M550.*:r[1,0,200]\" \
  --PO \"map=.*/Tprime_ggTauTau_M550.*:r[1,0,200]\"",

 "Tprime_M600":"-P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
  --PO \"map=.*/Tprime_ggbb_M600.*:r[1,0,200]\" \
  --PO \"map=.*/Tprime_ggWW_M600.*:r[1,0,200]\" \
  --PO \"map=.*/Tprime_ggTauTau_M600.*:r[1,0,200]\"",

 "Tprime_M650":"-P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
  --PO \"map=.*/Tprime_ggbb_M650.*:r[1,0,200]\" \
  --PO \"map=.*/Tprime_ggWW_M650.*:r[1,0,200]\" \
  --PO \"map=.*/Tprime_ggTauTau_M650.*:r[1,0,200]\"",

 "Tprime_M700":"-P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
  --PO \"map=.*/Tprime_ggbb_M700.*:r[1,0,200]\" \
  --PO \"map=.*/Tprime_ggWW_M700.*:r[1,0,200]\" \
  --PO \"map=.*/Tprime_ggTauTau_M700.*:r[1,0,200]\"",

 "Tprime_M750":"-P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
  --PO \"map=.*/Tprime_ggbb_M750.*:r[1,0,200]\" \
  --PO \"map=.*/Tprime_ggWW_M750.*:r[1,0,200]\" \
  --PO \"map=.*/Tprime_ggTauTau_M750.*:r[1,0,200]\"",

 "Tprime_M800":"-P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
  --PO \"map=.*/Tprime_ggbb_M800.*:r[1,0,200]\" \
  --PO \"map=.*/Tprime_ggWW_M800.*:r[1,0,200]\" \
  --PO \"map=.*/Tprime_ggTauTau_M800.*:r[1,0,200]\"",

 "Tprime_M850":"-P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
  --PO \"map=.*/Tprime_ggbb_M850.*:r[1,0,200]\" \
  --PO \"map=.*/Tprime_ggWW_M850.*:r[1,0,200]\" \
  --PO \"map=.*/Tprime_ggTauTau_M850.*:r[1,0,200]\"",

 "Tprime_M900":"-P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
  --PO \"map=.*/Tprime_ggbb_M900.*:r[1,0,200]\" \
  --PO \"map=.*/Tprime_ggWW_M900.*:r[1,0,200]\" \
  --PO \"map=.*/Tprime_ggTauTau_M900.*:r[1,0,200]\"",

 "Tprime_M950":"-P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
  --PO \"map=.*/Tprime_ggbb_M950.*:r[1,0,200]\" \
  --PO \"map=.*/Tprime_ggWW_M950.*:r[1,0,200]\" \
  --PO \"map=.*/Tprime_ggTauTau_M950.*:r[1,0,200]\"",

 "Tprime_M1000":"-P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
  --PO \"map=.*/Tprime_ggbb_M1000.*:r[1,0,200]\" \
  --PO \"map=.*/Tprime_ggWW_M1000.*:r[1,0,200]\" \
  --PO \"map=.*/Tprime_ggTauTau_M1000.*:r[1,0,200]\"",

 "Tprime_M1100":"-P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
  --PO \"map=.*/Tprime_ggbb_M1100.*:r[1,0,200]\" \
  --PO \"map=.*/Tprime_ggWW_M1100.*:r[1,0,200]\" \
  --PO \"map=.*/Tprime_ggTauTau_M1100.*:r[1,0,200]\"",

 "Tprime_M1200":"-P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
  --PO \"map=.*/Tprime_ggbb_M1200.*:r[1,0,200]\" \
  --PO \"map=.*/Tprime_ggWW_M1200.*:r[1,0,200]\" \
  --PO \"map=.*/Tprime_ggTauTau_M1200.*:r[1,0,200]\"",

 "Tprime_M1300":"-P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
  --PO \"map=.*/Tprime_ggbb_M1300.*:r[1,0,200]\" \
  --PO \"map=.*/Tprime_ggWW_M1300.*:r[1,0,200]\" \
  --PO \"map=.*/Tprime_ggTauTau_M1300.*:r[1,0,200]\"",

 "Tprime_M1400":"-P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
  --PO \"map=.*/Tprime_ggbb_M1400.*:r[1,0,200]\" \
  --PO \"map=.*/Tprime_ggWW_M1400.*:r[1,0,200]\" \
  --PO \"map=.*/Tprime_ggTauTau_M1400.*:r[1,0,200]\"",

 "Tprime_M1500":"-P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
  --PO \"map=.*/Tprime_ggbb_M1500.*:r[1,0,200]\" \
  --PO \"map=.*/Tprime_ggWW_M1500.*:r[1,0,200]\" \
  --PO \"map=.*/Tprime_ggTauTau_M1500.*:r[1,0,200]\"",

  "mu":"-P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
--PO \"map=.*/ggH.*:r_ggH[1,0,2]\" \
--PO \"map=.*/bbH.*:r_ggH[1,0,2]\" \
--PO \"map=.*/qqH.*:r_VBF[1,0,3]\" \
--PO \"map=.*/WH_had.*:r_VH[1,0,3]\" \
--PO \"map=.*/ZH_had.*:r_VH[1,0,3]\" \
--PO \"map=.*/ggZH_had.*:r_VH[1,0,3]\" \
--PO \"map=.*/WH_lep.*:r_VH[1,0,3]\" \
--PO \"map=.*/ZH_lep.*:r_VH[1,0,3]\" \
--PO \"map=.*/ggZH_ll.*:r_VH[1,0,3]\" \
--PO \"map=.*/ggZH_nunu.*:r_VH[1,0,3]\" \
--PO \"map=.*/ttH.*:r_top[1,0,3]\" \
--PO \"map=.*/tHq.*:r_top[1,0,3]\" \
--PO \"map=.*/tHW.*:r_top[1,0,3]\"",

  "stage0":"-P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
--PO \"map=.*/ggH.*:r_ggH[1,0,2]\" \
--PO \"map=.*/bbH.*:r_ggH[1,0,2]\" \
--PO \"map=.*/qqH.*:r_qqH[1,0,3]\" \
--PO \"map=.*/WH_had.*:r_qqH[1,0,3]\" \
--PO \"map=.*/ZH_had.*:r_qqH[1,0,3]\" \
--PO \"map=.*/ggZH_had.*:r_ggH[1,0,2]\" \
--PO \"map=.*/WH_lep.*:r_WH_lep[1,0,5]\" \
--PO \"map=.*/ZH_lep.*:r_ZH_lep[1,0,5]\" \
--PO \"map=.*/ggZH_ll.*:r_ZH_lep[1,0,5]\" \
--PO \"map=.*/ggZH_nunu.*:r_ZH_lep[1,0,5]\" \
--PO \"map=.*/ttH.*:r_ttH[1,0,3]\" \
--PO \"map=.*/tHq.*:r_tH[1,0,15]\" \
--PO \"map=.*/tHW.*:r_tH[1,0,15]\"",

  "stage1p2_maximal":"-P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
--PO \"map=.*/ggH_0J_PTH_0_10.*:r_ggH_0J_low[1,0,4]\" \
--PO \"map=.*/ggZH_had_0J_PTH_0_10.*:r_ggH_0J_low[1,0,4]\" \
--PO \"map=RECO_0J_PTH_0_10_Tag.*/bbH.*:r_ggH_0J_low[1,0,4]\" \
--PO \"map=.*/ggH_0J_PTH_GT10.*:r_ggH_0J_high[1,0,2]\" \
--PO \"map=.*/ggZH_had_0J_PTH_GT10.*:r_ggH_0J_high[1,0,2]\" \
--PO \"map=RECO_0J_PTH_GT10_Tag.*/bbH.*:r_ggH_0J_high[1,0,2]\" \
--PO \"map=.*/ggH_1J_PTH_0_60.*:r_ggH_1J_low[1,0,4]\" \
--PO \"map=.*/ggZH_had_1J_PTH_0_60.*:r_ggH_1J_low[1,0,4]\" \
--PO \"map=RECO_1J_PTH_0_60_Tag.*/bbH.*:r_ggH_1J_low[1,0,4]\" \
--PO \"map=.*/ggH_1J_PTH_60_120.*:r_ggH_1J_med[1,0,4]\" \
--PO \"map=.*/ggZH_had_1J_PTH_60_120.*:r_ggH_1J_med[1,0,4]\" \
--PO \"map=RECO_1J_PTH_60_120_Tag.*/bbH.*:r_ggH_1J_med[1,0,4]\" \
--PO \"map=.*/ggH_1J_PTH_120_200.*:r_ggH_1J_high[1,0,4]\" \
--PO \"map=.*/ggZH_had_1J_PTH_120_200.*:r_ggH_1J_high[1,0,4]\" \
--PO \"map=RECO_1J_PTH_120_200_Tag.*/bbH.*:r_ggH_1J_high[1,0,4]\" \
--PO \"map=.*/ggH_GE2J_MJJ_0_350_PTH_0_60.*:r_ggH_2J_low[1,0,4]\" \
--PO \"map=.*/ggZH_had_GE2J_MJJ_0_350_PTH_0_60.*:r_ggH_2J_low[1,0,4]\" \
--PO \"map=RECO_GE2J_PTH_0_60_Tag.*/bbH.*:r_ggH_2J_low[1,0,4]\" \
--PO \"map=.*/ggH_GE2J_MJJ_0_350_PTH_60_120.*:r_ggH_2J_med[1,0,4]\" \
--PO \"map=.*/ggZH_had_GE2J_MJJ_0_350_PTH_60_120.*:r_ggH_2J_med[1,0,4]\" \
--PO \"map=RECO_GE2J_PTH_60_120_Tag.*/bbH.*:r_ggH_2J_med[1,0,4]\" \
--PO \"map=.*/ggH_GE2J_MJJ_0_350_PTH_120_200.*:r_ggH_2J_high[1,0,4]\" \
--PO \"map=.*/ggZH_had_GE2J_MJJ_0_350_PTH_120_200.*:r_ggH_2J_high[1,0,4]\" \
--PO \"map=RECO_GE2J_PTH_120_200_Tag.*/bbH.*:r_ggH_2J_high[1,0,4]\" \
--PO \"map=.*/ggH_PTH_.*:r_ggH_BSM[1,0,4]\" \
--PO \"map=.*/ggZH_had_PTH_.*:r_ggH_BSM[1,0,4]\" \
--PO \"map=RECO_PTH.*/bbH.*:r_ggH_BSM[1,0,4]\" \
--PO \"map=.*/ggH_GE2J_MJJ_350_700_.*.*:r_ggH_VBFlike[1,0,6]\" \
--PO \"map=.*/ggZH_had_GE2J_MJJ_350_700_.*.*:r_ggH_VBFlike[1,0,6]\" \
--PO \"map=.*/ggH_GE2J_MJJ_GT700_.*.*:r_ggH_VBFlike[1,0,6]\" \
--PO \"map=.*/ggZH_had_GE2J_MJJ_GT700_.*.*:r_ggH_VBFlike[1,0,6]\" \
--PO \"map=.*/qqH_GE2J_MJJ_350_700_PTH_0_200_.*:r_qqH_VBFlike[1,0,3]\" \
--PO \"map=.*/qqH_GE2J_MJJ_GT700_PTH_0_200_.*:r_qqH_VBFlike[1,0,3]\" \
--PO \"map=.*/WH_had_GE2J_MJJ_350_700_PTH_0_200_.*:r_qqH_VBFlike[1,0,3]\" \
--PO \"map=.*/WH_had_GE2J_MJJ_GT700_PTH_0_200_.*:r_qqH_VBFlike[1,0,3]\" \
--PO \"map=.*/ZH_had_GE2J_MJJ_350_700_PTH_0_200_.*:r_qqH_VBFlike[1,0,3]\" \
--PO \"map=.*/ZH_had_GE2J_MJJ_GT700_PTH_0_200_.*:r_qqH_VBFlike[1,0,3]\" \
--PO \"map=.*/qqH_GE2J_.*_PTH_GT200.*:r_qqH_BSM[1,0,4]\" \
--PO \"map=.*/WH_had_GE2J_.*_PTH_GT200.*:r_qqH_BSM[1,0,4]\" \
--PO \"map=.*/ZH_had_GE2J_.*_PTH_GT200.*:r_qqH_BSM[1,0,4]\" \
--PO \"map=.*/qqH_GE2J_MJJ_60_120.*:r_qqH_VHhad[1,0,6]\" \
--PO \"map=.*/WH_had_GE2J_MJJ_60_120.*:r_qqH_VHhad[1,0,6]\" \
--PO \"map=.*/ZH_had_GE2J_MJJ_60_120.*:r_qqH_VHhad[1,0,6]\" \
--PO \"map=.*/WH_lep.*hgg:r_WH_lep[1,0,6]\" \
--PO \"map=.*/ZH_lep.*hgg:r_ZH_lep[1,0,6]\" \
--PO \"map=.*/ggZH_ll.*hgg:r_ZH_lep[1,0,6]\" \
--PO \"map=.*/ggZH_nunu.*hgg:r_ZH_lep[1,0,6]\" \
--PO \"map=.*/ttH.*hgg:r_ttH[1,0,3]\" \
--PO \"map=.*/tHq.*hgg:r_tH[1,0,15]\" \
--PO \"map=.*/tHW.*hgg:r_tH[1,0,15]\"",

  "stage1p2_minimal":"-P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
--PO \"map=.*/ggH_0J_PTH_0_10.*:r_ggH_0J_low[1,0,4]\" \
--PO \"map=.*/ggZH_had_0J_PTH_0_10.*:r_ggH_0J_low[1,0,4]\" \
--PO \"map=RECO_0J_PTH_0_10_Tag.*/bbH.*:r_ggH_0J_low[1,0,4]\" \
--PO \"map=.*/ggH_0J_PTH_GT10.*:r_ggH_0J_high[1,0,2]\" \
--PO \"map=.*/ggZH_had_0J_PTH_GT10.*:r_ggH_0J_high[1,0,2]\" \
--PO \"map=RECO_0J_PTH_GT10_Tag.*/bbH.*:r_ggH_0J_high[1,0,2]\" \
--PO \"map=.*/ggH_1J_PTH_0_60.*:r_ggH_1J_low[1,0,4]\" \
--PO \"map=.*/ggZH_had_1J_PTH_0_60.*:r_ggH_1J_low[1,0,4]\" \
--PO \"map=RECO_1J_PTH_0_60_Tag.*/bbH.*:r_ggH_1J_low[1,0,4]\" \
--PO \"map=.*/ggH_1J_PTH_60_120.*:r_ggH_1J_med[1,0,4]\" \
--PO \"map=.*/ggZH_had_1J_PTH_60_120.*:r_ggH_1J_med[1,0,4]\" \
--PO \"map=RECO_1J_PTH_60_120_Tag.*/bbH.*:r_ggH_1J_med[1,0,4]\" \
--PO \"map=.*/ggH_1J_PTH_120_200.*:r_ggH_1J_high[1,0,4]\" \
--PO \"map=.*/ggZH_had_1J_PTH_120_200.*:r_ggH_1J_high[1,0,4]\" \
--PO \"map=RECO_1J_PTH_120_200_Tag.*/bbH.*:r_ggH_1J_high[1,0,4]\" \
--PO \"map=.*/ggH_GE2J_MJJ_0_350_PTH_0_60.*:r_ggH_2J_low[1,0,4]\" \
--PO \"map=.*/ggZH_had_GE2J_MJJ_0_350_PTH_0_60.*:r_ggH_2J_low[1,0,4]\" \
--PO \"map=RECO_GE2J_PTH_0_60_Tag.*/bbH.*:r_ggH_2J_low[1,0,4]\" \
--PO \"map=.*/ggH_GE2J_MJJ_0_350_PTH_60_120.*:r_ggH_2J_med[1,0,4]\" \
--PO \"map=.*/ggZH_had_GE2J_MJJ_0_350_PTH_60_120.*:r_ggH_2J_med[1,0,4]\" \
--PO \"map=RECO_GE2J_PTH_60_120_Tag.*/bbH.*:r_ggH_2J_med[1,0,4]\" \
--PO \"map=.*/ggH_GE2J_MJJ_0_350_PTH_120_200.*:r_ggH_2J_high[1,0,4]\" \
--PO \"map=.*/ggZH_had_GE2J_MJJ_0_350_PTH_120_200.*:r_ggH_2J_high[1,0,4]\" \
--PO \"map=RECO_GE2J_PTH_120_200_Tag.*/bbH.*:r_ggH_2J_high[1,0,4]\" \
--PO \"map=.*/ggH_PTH_200_300.*:r_ggH_BSM_low[1,0,4]\" \
--PO \"map=.*/ggZH_had_PTH_200_300.*:r_ggH_BSM_low[1,0,4]\" \
--PO \"map=RECO_PTH_200_300_Tag.*/bbH.*:r_ggH_BSM_low[1,0,4]\" \
--PO \"map=.*/ggH_PTH_300_450.*:r_ggH_BSM_high[1,0,4]\" \
--PO \"map=.*/ggZH_had_PTH_300_450.*:r_ggH_BSM_high[1,0,4]\" \
--PO \"map=RECO_PTH_300_450_Tag.*/bbH.*:r_ggH_BSM_high[1,0,4]\" \
--PO \"map=.*/ggH_PTH_450_650.*:r_ggH_BSM_high[1,0,4]\" \
--PO \"map=.*/ggZH_had_PTH_450_650.*:r_ggH_BSM_high[1,0,4]\" \
--PO \"map=RECO_PTH_450_650_Tag.*/bbH.*:r_ggH_BSM_high[1,0,4]\" \
--PO \"map=.*/ggH_PTH_GT650.*:r_ggH_BSM_high[1,0,4]\" \
--PO \"map=.*/ggZH_had_PTH_GT650.*:r_ggH_BSM_high[1,0,4]\" \
--PO \"map=RECO_PTH_GT650_Tag.*/bbH.*:r_ggH_BSM_high[1,0,4]\" \
--PO \"map=.*/ggH_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25.*:r_qqH_low_mjj_low_pthjj[1,0,6]\" \
--PO \"map=.*/ggZH_had_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25.*:r_qqH_low_mjj_low_pthjj[1,0,6]\" \
--PO \"map=.*/ggH_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25.*:r_qqH_low_mjj_high_pthjj[1,0,7]\" \
--PO \"map=.*/ggZH_had_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25.*:r_qqH_low_mjj_high_pthjj[1,0,7]\" \
--PO \"map=.*/ggH_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25.*:r_qqH_high_mjj_low_pthjj[1,0,6]\" \
--PO \"map=.*/ggZH_had_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25.*:r_qqH_high_mjj_low_pthjj[1,0,6]\" \
--PO \"map=.*/ggH_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25.*:r_qqH_high_mjj_high_pthjj[1,0,5]\" \
--PO \"map=.*/ggZH_had_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25.*:r_qqH_high_mjj_high_pthjj[1,0,5]\" \
--PO \"map=.*/qqH_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25.*:r_qqH_low_mjj_low_pthjj[1,0,6]\" \
--PO \"map=.*/qqH_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25.*:r_qqH_low_mjj_high_pthjj[1,0,7]\" \
--PO \"map=.*/qqH_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25.*:r_qqH_high_mjj_low_pthjj[1,0,6]\" \
--PO \"map=.*/qqH_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25.*:r_qqH_high_mjj_high_pthjj[1,0,5]\" \
--PO \"map=.*/WH_had_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25.*:r_qqH_low_mjj_low_pthjj[1,0,6]\" \
--PO \"map=.*/WH_had_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25.*:r_qqH_low_mjj_high_pthjj[1,0,7]\" \
--PO \"map=.*/WH_had_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25.*:r_qqH_high_mjj_low_pthjj[1,0,6]\" \
--PO \"map=.*/WH_had_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25.*:r_qqH_high_mjj_high_pthjj[1,0,5]\" \
--PO \"map=.*/ZH_had_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25.*:r_qqH_low_mjj_low_pthjj[1,0,6]\" \
--PO \"map=.*/ZH_had_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25.*:r_qqH_low_mjj_high_pthjj[1,0,7]\" \
--PO \"map=.*/ZH_had_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25.*:r_qqH_high_mjj_low_pthjj[1,0,6]\" \
--PO \"map=.*/ZH_had_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25.*:r_qqH_high_mjj_high_pthjj[1,0,5]\" \
--PO \"map=.*/qqH_GE2J_.*_PTH_GT200.*:r_qqH_BSM[1,0,4]\" \
--PO \"map=.*/WH_had_GE2J_.*_PTH_GT200.*:r_qqH_BSM[1,0,4]\" \
--PO \"map=.*/ZH_had_GE2J_.*_PTH_GT200.*:r_qqH_BSM[1,0,4]\" \
--PO \"map=.*/qqH_GE2J_MJJ_60_120.*:r_qqH_VHhad[1,0,6]\" \
--PO \"map=.*/WH_had_GE2J_MJJ_60_120.*:r_qqH_VHhad[1,0,6]\" \
--PO \"map=.*/ZH_had_GE2J_MJJ_60_120.*:r_qqH_VHhad[1,0,6]\" \
--PO \"map=.*/WH_lep_PTV_0_75.*hgg:r_WH_lep_low[1,0,6]\" \
--PO \"map=.*/WH_lep_PTV_75_150.*hgg:r_WH_lep_high[1,0,6]\" \
--PO \"map=.*/WH_lep_PTV_150_250.*hgg:r_WH_lep_high[1,0,6]\" \
--PO \"map=.*/WH_lep_PTV_GT250.*hgg:r_WH_lep_high[1,0,6]\" \
--PO \"map=.*/ZH_lep.*hgg:r_ZH_lep[1,0,6]\" \
--PO \"map=.*/ggZH_ll.*hgg:r_ZH_lep[1,0,6]\" \
--PO \"map=.*/ggZH_nunu.*hgg:r_ZH_lep[1,0,6]\" \
--PO \"map=.*/ttH_PTH_0_60.*hgg:r_ttH_low[1,0,5]\" \
--PO \"map=.*/ttH_PTH_60_120.*hgg:r_ttH_medlow[1,0,3]\" \
--PO \"map=.*/ttH_PTH_120_200.*hgg:r_ttH_medhigh[1,0,4]\" \
--PO \"map=.*/ttH_PTH_200_300.*hgg:r_ttH_high[1,0,5]\" \
--PO \"map=.*/ttH_PTH_GT300.*hgg:r_ttH_high[1,0,5]\" \
--PO \"map=.*/tHq.*hgg:r_tH[1,0,15]\" \
--PO \"map=.*/tHW.*hgg:r_tH[1,0,15]\"",

  "stage1p2_extended":"-P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
--PO \"map=.*/ggH_0J_PTH_0_10.*:r_ggH_0J_low[1,0,4]\" \
--PO \"map=.*/ggZH_had_0J_PTH_0_10.*:r_ggH_0J_low[1,0,4]\" \
--PO \"map=RECO_0J_PTH_0_10_Tag.*/bbH.*:r_ggH_0J_low[1,0,4]\" \
--PO \"map=.*/ggH_0J_PTH_GT10.*:r_ggH_0J_high[1,0,2]\" \
--PO \"map=.*/ggZH_had_0J_PTH_GT10.*:r_ggH_0J_high[1,0,2]\" \
--PO \"map=RECO_0J_PTH_GT10_Tag.*/bbH.*:r_ggH_0J_high[1,0,2]\" \
--PO \"map=.*/ggH_1J_PTH_0_60.*:r_ggH_1J_low[1,0,4]\" \
--PO \"map=.*/ggZH_had_1J_PTH_0_60.*:r_ggH_1J_low[1,0,4]\" \
--PO \"map=RECO_1J_PTH_0_60_Tag.*/bbH.*:r_ggH_1J_low[1,0,4]\" \
--PO \"map=.*/ggH_1J_PTH_60_120.*:r_ggH_1J_med[1,0,4]\" \
--PO \"map=.*/ggZH_had_1J_PTH_60_120.*:r_ggH_1J_med[1,0,4]\" \
--PO \"map=RECO_1J_PTH_60_120_Tag.*/bbH.*:r_ggH_1J_med[1,0,4]\" \
--PO \"map=.*/ggH_1J_PTH_120_200.*:r_ggH_1J_high[1,0,4]\" \
--PO \"map=.*/ggZH_had_1J_PTH_120_200.*:r_ggH_1J_high[1,0,4]\" \
--PO \"map=RECO_1J_PTH_120_200_Tag.*/bbH.*:r_ggH_1J_high[1,0,4]\" \
--PO \"map=.*/ggH_GE2J_MJJ_0_350_PTH_0_60.*:r_ggH_2J_low[1,0,4]\" \
--PO \"map=.*/ggZH_had_GE2J_MJJ_0_350_PTH_0_60.*:r_ggH_2J_low[1,0,4]\" \
--PO \"map=RECO_GE2J_PTH_0_60_Tag.*/bbH.*:r_ggH_2J_low[1,0,4]\" \
--PO \"map=.*/ggH_GE2J_MJJ_0_350_PTH_60_120.*:r_ggH_2J_med[1,0,4]\" \
--PO \"map=.*/ggZH_had_GE2J_MJJ_0_350_PTH_60_120.*:r_ggH_2J_med[1,0,4]\" \
--PO \"map=RECO_GE2J_PTH_60_120_Tag.*/bbH.*:r_ggH_2J_med[1,0,4]\" \
--PO \"map=.*/ggH_GE2J_MJJ_0_350_PTH_120_200.*:r_ggH_2J_high[1,0,4]\" \
--PO \"map=.*/ggZH_had_GE2J_MJJ_0_350_PTH_120_200.*:r_ggH_2J_high[1,0,4]\" \
--PO \"map=RECO_GE2J_PTH_120_200_Tag.*/bbH.*:r_ggH_2J_high[1,0,4]\" \
--PO \"map=.*/ggH_PTH_200_300.*:r_ggH_BSM_low[1,0,4]\" \
--PO \"map=.*/ggZH_had_PTH_200_300.*:r_ggH_BSM_low[1,0,4]\" \
--PO \"map=RECO_PTH_200_300_Tag.*/bbH.*:r_ggH_BSM_low[1,0,4]\" \
--PO \"map=.*/ggH_PTH_300_450.*:r_ggH_BSM_med[1,0,4]\" \
--PO \"map=.*/ggZH_had_PTH_300_450.*:r_ggH_BSM_med[1,0,4]\" \
--PO \"map=RECO_PTH_300_450_Tag.*/bbH.*:r_ggH_BSM_med[1,0,4]\" \
--PO \"map=.*/ggH_PTH_450_650.*:r_ggH_BSM_high[1,0,6]\" \
--PO \"map=.*/ggZH_had_PTH_450_650.*:r_ggH_BSM_high[1,0,6]\" \
--PO \"map=RECO_PTH_450_650_Tag.*/bbH.*:r_ggH_BSM_high[1,0,6]\" \
--PO \"map=.*/ggH_PTH_GT650.*:r_ggH_BSM_high[1,0,6]\" \
--PO \"map=.*/ggZH_had_PTH_GT650.*:r_ggH_BSM_high[1,0,6]\" \
--PO \"map=RECO_PTH_GT650_Tag.*/bbH.*:r_ggH_BSM_high[1,0,6]\" \
--PO \"map=.*/ggH_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25.*:r_qqH_low_mjj_low_pthjj[1,0,6]\" \
--PO \"map=.*/ggZH_had_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25.*:r_qqH_low_mjj_low_pthjj[1,0,6]\" \
--PO \"map=.*/ggH_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25.*:r_qqH_low_mjj_high_pthjj[1,0,7]\" \
--PO \"map=.*/ggZH_had_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25.*:r_qqH_low_mjj_high_pthjj[1,0,7]\" \
--PO \"map=.*/ggH_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25.*:r_qqH_high_mjj_low_pthjj[1,0,6]\" \
--PO \"map=.*/ggZH_had_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25.*:r_qqH_high_mjj_low_pthjj[1,0,6]\" \
--PO \"map=.*/ggH_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25.*:r_qqH_high_mjj_high_pthjj[1,0,5]\" \
--PO \"map=.*/ggZH_had_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25.*:r_qqH_high_mjj_high_pthjj[1,0,5]\" \
--PO \"map=.*/qqH_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25.*:r_qqH_low_mjj_low_pthjj[1,0,6]\" \
--PO \"map=.*/qqH_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25.*:r_qqH_low_mjj_high_pthjj[1,0,7]\" \
--PO \"map=.*/qqH_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25.*:r_qqH_high_mjj_low_pthjj[1,0,6]\" \
--PO \"map=.*/qqH_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25.*:r_qqH_high_mjj_high_pthjj[1,0,5]\" \
--PO \"map=.*/WH_had_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25.*:r_qqH_low_mjj_low_pthjj[1,0,6]\" \
--PO \"map=.*/WH_had_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25.*:r_qqH_low_mjj_high_pthjj[1,0,7]\" \
--PO \"map=.*/WH_had_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25.*:r_qqH_high_mjj_low_pthjj[1,0,6]\" \
--PO \"map=.*/WH_had_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25.*:r_qqH_high_mjj_high_pthjj[1,0,5]\" \
--PO \"map=.*/ZH_had_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25.*:r_qqH_low_mjj_low_pthjj[1,0,6]\" \
--PO \"map=.*/ZH_had_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25.*:r_qqH_low_mjj_high_pthjj[1,0,7]\" \
--PO \"map=.*/ZH_had_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25.*:r_qqH_high_mjj_low_pthjj[1,0,6]\" \
--PO \"map=.*/ZH_had_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25.*:r_qqH_high_mjj_high_pthjj[1,0,5]\" \
--PO \"map=.*/qqH_GE2J_.*_PTH_GT200.*:r_qqH_BSM[1,0,4]\" \
--PO \"map=.*/WH_had_GE2J_.*_PTH_GT200.*:r_qqH_BSM[1,0,4]\" \
--PO \"map=.*/ZH_had_GE2J_.*_PTH_GT200.*:r_qqH_BSM[1,0,4]\" \
--PO \"map=.*/qqH_GE2J_MJJ_60_120.*:r_qqH_VHhad[1,0,6]\" \
--PO \"map=.*/WH_had_GE2J_MJJ_60_120.*:r_qqH_VHhad[1,0,6]\" \
--PO \"map=.*/ZH_had_GE2J_MJJ_60_120.*:r_qqH_VHhad[1,0,6]\" \
--PO \"map=.*/WH_lep_PTV_0_75.*hgg:r_WH_lep_low[1,0,6]\" \
--PO \"map=.*/WH_lep_PTV_75_150.*hgg:r_WH_lep_high[1,0,6]\" \
--PO \"map=.*/WH_lep_PTV_150_250.*hgg:r_WH_lep_high[1,0,6]\" \
--PO \"map=.*/WH_lep_PTV_GT250.*hgg:r_WH_lep_high[1,0,6]\" \
--PO \"map=.*/ZH_lep.*hgg:r_ZH_lep[1,0,6]\" \
--PO \"map=.*/ggZH_ll.*hgg:r_ZH_lep[1,0,6]\" \
--PO \"map=.*/ggZH_nunu.*hgg:r_ZH_lep[1,0,6]\" \
--PO \"map=.*/ttH_PTH_0_60.*hgg:r_ttH_low[1,0,5]\" \
--PO \"map=.*/ttH_PTH_60_120.*hgg:r_ttH_medlow[1,0,3]\" \
--PO \"map=.*/ttH_PTH_120_200.*hgg:r_ttH_medhigh[1,0,4]\" \
--PO \"map=.*/ttH_PTH_200_300.*hgg:r_ttH_high[1,0,5]\" \
--PO \"map=.*/ttH_PTH_GT300.*hgg:r_ttH_high[1,0,5]\" \
--PO \"map=.*/tHq.*hgg:r_tH[1,0,15]\" \
--PO \"map=.*/tHW.*hgg:r_tH[1,0,15]\"",


  "kappas_resolved":"-P HiggsAnalysis.CombinedLimit.LHCHCGModels:K1 --PO BRU=0",

  "kappas":"-P HiggsAnalysis.CombinedLimit.LHCHCGModels:K2 --PO BRU=0",

  "kVkF":"-P HiggsAnalysis.CombinedLimit.LHCHCGModels:K3 --PO BRU=0"
}
