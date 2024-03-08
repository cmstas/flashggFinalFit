# Python script to hold replacement model mapping for different analyses
from collections import OrderedDict as od

# Add analyses to globalReplacementMap. See "STXS" as an example
globalReplacementMap = od()

# Example analysis which with cats Untagged_Tag0,VBF_Tag0
globalReplacementMap['example'] = od()
# For WRONG VERTEX SCENARIO:
#  * single proc x cat for wrong vertex since for dZ > 1cm shape independent of proc x cat
#  * use proc x cat with highest number of WV events
globalReplacementMap['example']['procWV'] = "GG2H"
globalReplacementMap['example']['catWV'] = "Untagged_Tag0"
# For RIGHT VERTEX SCENARIO:
#  * default you should add is diagonal process from given category 
#  * if few events in diagonal process then may need to change the category aswell (see catRVMap)
#  * map must contain entry for all cats being processed (for replacement proc and cat)
globalReplacementMap['example']['procRVMap'] = od()
globalReplacementMap["example"]["procRVMap"]["Untagged_Tag0"] = "GG2H"
globalReplacementMap["example"]["procRVMap"]["VBF_Tag0"] = "VBF"
# Replacement category for RV fit
globalReplacementMap["example"]["catRVMap"] = od()
globalReplacementMap["example"]["catRVMap"]["Untagged_Tag0"] = "Untagged_Tag0"
globalReplacementMap["example"]["catRVMap"]["VBF_Tag0"] = "VBF_Tag0"


# Example analysis which with cats Untagged_Tag0,VBF_Tag0
globalReplacementMap['ggtt_nonRes'] = od()
globalReplacementMap['ggtt_nonRes']['procWV'] = "HH2ggtautau"
globalReplacementMap['ggtt_nonRes']['catWV'] = "HH2ggtautau_SR1"
globalReplacementMap['ggtt_nonRes']['catWV'] = "HH2ggtautau_SR2"

globalReplacementMap['ggtt_nonRes']['procWV'] = "ttHHggbb"
globalReplacementMap['ggtt_nonRes']['catWV'] = "ttHHggbb_SR1"
globalReplacementMap['ggtt_nonRes']['catWV'] = "ttHHggbb_SR2"
# For RIGHT VERTEX SCENARIO:
#  * default you should add is diagonal process from given category 
#  * if few events in diagonal process then may need to change the category aswell (see catRVMap)
#  * map must contain entry for all cats being processed (for replacement proc and cat)
globalReplacementMap['ggtt_nonRes']['procRVMap'] = od()
#globalReplacementMap['ggtt_nonRes']["procRVMap"]["SR1"] = "HH2ggtautau"
#globalReplacementMap['ggtt_nonRes']["procRVMap"]["SR2"] = "HH2ggtautau"

globalReplacementMap['ggtt_nonRes']["procRVMap"]["SR1"] = "ttHHggbb"
globalReplacementMap['ggtt_nonRes']["procRVMap"]["SR2"] = "ttHHggbb"

# Replacement category for RV fit
globalReplacementMap['ggtt_nonRes']["catRVMap"] = od()
globalReplacementMap['ggtt_nonRes']["catRVMap"]["SR1"] = "SR1"
globalReplacementMap['ggtt_nonRes']["catRVMap"]["SR2"] = "SR2"


#ttHHggXX SM
globalReplacementMap['ttHHggXX'] = od()
globalReplacementMap['ttHHggXX']['procWV'] = "ttHH_ggbb"
globalReplacementMap['ttHHggXX']['catWV'] = "ttHH_ggbb_SR1"
globalReplacementMap['ttHHggXX']['catWV'] = "ttHH_ggbb_SR2"
globalReplacementMap['ttHHggXX']['procRVMap'] = od()
globalReplacementMap['ttHHggXX']["procRVMap"]["SR1"] = "ttHH_ggbb"
globalReplacementMap['ttHHggXX']["procRVMap"]["SR2"] = "ttHH_ggbb"
globalReplacementMap['ttHHggXX']["catRVMap"] = od()
globalReplacementMap['ttHHggXX']["catRVMap"]["SR1"] = "SR1"
globalReplacementMap['ttHHggXX']["catRVMap"]["SR2"] = "SR2"

#ttHHggXX 2HDM M250
globalReplacementMap['2HDM_M250'] = od()
globalReplacementMap['2HDM_M250']['procWV'] = "2HDMbbM250"
globalReplacementMap['2HDM_M250']['catWV'] = "2HDMbbM250_SR1"
globalReplacementMap['2HDM_M250']['catWV'] = "2HDMbbM250_SR2"
globalReplacementMap['2HDM_M250']['procRVMap'] = od()
globalReplacementMap['2HDM_M250']["procRVMap"]["SR1"] = "2HDMbbM250"
globalReplacementMap['2HDM_M250']["procRVMap"]["SR2"] = "2HDMbbM250"
globalReplacementMap['2HDM_M250']["catRVMap"] = od()
globalReplacementMap['2HDM_M250']["catRVMap"]["SR1"] = "SR1"
globalReplacementMap['2HDM_M250']["catRVMap"]["SR2"] = "SR2"

#ttHHggXX 2HDM M300
globalReplacementMap['2HDM_M300'] = od()
globalReplacementMap['2HDM_M300']['procWV'] = "2HDMbbM300"
globalReplacementMap['2HDM_M300']['catWV'] = "2HDMbbM300_SR1"
globalReplacementMap['2HDM_M300']['catWV'] = "2HDMbbM300_SR2"
globalReplacementMap['2HDM_M300']['procRVMap'] = od()
globalReplacementMap['2HDM_M300']["procRVMap"]["SR1"] = "2HDMbbM300"
globalReplacementMap['2HDM_M300']["procRVMap"]["SR2"] = "2HDMbbM300"
globalReplacementMap['2HDM_M300']["catRVMap"] = od()
globalReplacementMap['2HDM_M300']["catRVMap"]["SR1"] = "SR1"
globalReplacementMap['2HDM_M300']["catRVMap"]["SR2"] = "SR2"

#ttHHggXX 2HDM M350
globalReplacementMap['2HDM_M350'] = od()
globalReplacementMap['2HDM_M350']['procWV'] = "2HDMbbM350"
globalReplacementMap['2HDM_M350']['catWV'] = "2HDMbbM350_SR1"
globalReplacementMap['2HDM_M350']['catWV'] = "2HDMbbM350_SR2"
globalReplacementMap['2HDM_M350']['procRVMap'] = od()
globalReplacementMap['2HDM_M350']["procRVMap"]["SR1"] = "2HDMbbM350"
globalReplacementMap['2HDM_M350']["procRVMap"]["SR2"] = "2HDMbbM350"
globalReplacementMap['2HDM_M350']["catRVMap"] = od()
globalReplacementMap['2HDM_M350']["catRVMap"]["SR1"] = "SR1"
globalReplacementMap['2HDM_M350']["catRVMap"]["SR2"] = "SR2"

#ttHHggXX Tprime M500 
globalReplacementMap['Tprime_M500'] = od()
globalReplacementMap['Tprime_M500']['procWV'] = "TprimeBBM500"
globalReplacementMap['Tprime_M500']['catWV'] = "TprimeBBM500_SR1"
globalReplacementMap['Tprime_M500']['catWV'] = "TprimeBBM500_SR2"
globalReplacementMap['Tprime_M500']['procRVMap'] = od()
globalReplacementMap['Tprime_M500']["procRVMap"]["SR1"] = "TprimeBBM500"
globalReplacementMap['Tprime_M500']["procRVMap"]["SR2"] = "TprimeBBM500"
globalReplacementMap['Tprime_M500']["catRVMap"] = od()
globalReplacementMap['Tprime_M500']["catRVMap"]["SR1"] = "SR1"
globalReplacementMap['Tprime_M500']["catRVMap"]["SR2"] = "SR2"

#ttHHggXX Tprime M550 
globalReplacementMap['Tprime_M550'] = od()
globalReplacementMap['Tprime_M550']['procWV'] = "TprimeBBM550"
globalReplacementMap['Tprime_M550']['catWV'] = "TprimeBBM550_SR1"
globalReplacementMap['Tprime_M550']['catWV'] = "TprimeBBM550_SR2"
globalReplacementMap['Tprime_M550']['procRVMap'] = od()
globalReplacementMap['Tprime_M550']["procRVMap"]["SR1"] = "TprimeBBM550"
globalReplacementMap['Tprime_M550']["procRVMap"]["SR2"] = "TprimeBBM550"
globalReplacementMap['Tprime_M550']["catRVMap"] = od()
globalReplacementMap['Tprime_M550']["catRVMap"]["SR1"] = "SR1"
globalReplacementMap['Tprime_M550']["catRVMap"]["SR2"] = "SR2"

#ttHHggXX Tprime M600 
globalReplacementMap['Tprime_M600'] = od()
globalReplacementMap['Tprime_M600']['procWV'] = "TprimeBBM600"
globalReplacementMap['Tprime_M600']['catWV'] = "TprimeBBM600_SR1"
globalReplacementMap['Tprime_M600']['catWV'] = "TprimeBBM600_SR2"
globalReplacementMap['Tprime_M600']['procRVMap'] = od()
globalReplacementMap['Tprime_M600']["procRVMap"]["SR1"] = "TprimeBBM600"
globalReplacementMap['Tprime_M600']["procRVMap"]["SR2"] = "TprimeBBM600"
globalReplacementMap['Tprime_M600']["catRVMap"] = od()
globalReplacementMap['Tprime_M600']["catRVMap"]["SR1"] = "SR1"
globalReplacementMap['Tprime_M600']["catRVMap"]["SR2"] = "SR2"

#ttHHggXX Tprime M650 
globalReplacementMap['Tprime_M650'] = od()
globalReplacementMap['Tprime_M650']['procWV'] = "TprimeBBM650"
globalReplacementMap['Tprime_M650']['catWV'] = "TprimeBBM650_SR1"
globalReplacementMap['Tprime_M650']['catWV'] = "TprimeBBM650_SR2"
globalReplacementMap['Tprime_M650']['procRVMap'] = od()
globalReplacementMap['Tprime_M650']["procRVMap"]["SR1"] = "TprimeBBM650"
globalReplacementMap['Tprime_M650']["procRVMap"]["SR2"] = "TprimeBBM650"
globalReplacementMap['Tprime_M650']["catRVMap"] = od()
globalReplacementMap['Tprime_M650']["catRVMap"]["SR1"] = "SR1"
globalReplacementMap['Tprime_M650']["catRVMap"]["SR2"] = "SR2"

#ttHHggXX Tprime M700 
globalReplacementMap['Tprime_M700'] = od()
globalReplacementMap['Tprime_M700']['procWV'] = "TprimeBBM700"
globalReplacementMap['Tprime_M700']['catWV'] = "TprimeBBM700_SR1"
globalReplacementMap['Tprime_M700']['catWV'] = "TprimeBBM700_SR2"
globalReplacementMap['Tprime_M700']['procRVMap'] = od()
globalReplacementMap['Tprime_M700']["procRVMap"]["SR1"] = "TprimeBBM700"
globalReplacementMap['Tprime_M700']["procRVMap"]["SR2"] = "TprimeBBM700"
globalReplacementMap['Tprime_M700']["catRVMap"] = od()
globalReplacementMap['Tprime_M700']["catRVMap"]["SR1"] = "SR1"
globalReplacementMap['Tprime_M700']["catRVMap"]["SR2"] = "SR2"

#ttHHggXX Tprime M750 
globalReplacementMap['Tprime_M750'] = od()
globalReplacementMap['Tprime_M750']['procWV'] = "TprimeBBM750"
globalReplacementMap['Tprime_M750']['catWV'] = "TprimeBBM750_SR1"
globalReplacementMap['Tprime_M750']['catWV'] = "TprimeBBM750_SR2"
globalReplacementMap['Tprime_M750']['procRVMap'] = od()
globalReplacementMap['Tprime_M750']["procRVMap"]["SR1"] = "TprimeBBM750"
globalReplacementMap['Tprime_M750']["procRVMap"]["SR2"] = "TprimeBBM750"
globalReplacementMap['Tprime_M750']["catRVMap"] = od()
globalReplacementMap['Tprime_M750']["catRVMap"]["SR1"] = "SR1"
globalReplacementMap['Tprime_M750']["catRVMap"]["SR2"] = "SR2"

#ttHHggXX Tprime M800 
globalReplacementMap['Tprime_M800'] = od()
globalReplacementMap['Tprime_M800']['procWV'] = "TprimeBBM800"
globalReplacementMap['Tprime_M800']['catWV'] = "TprimeBBM800_SR1"
globalReplacementMap['Tprime_M800']['catWV'] = "TprimeBBM800_SR2"
globalReplacementMap['Tprime_M800']['procRVMap'] = od()
globalReplacementMap['Tprime_M800']["procRVMap"]["SR1"] = "TprimeBBM800"
globalReplacementMap['Tprime_M800']["procRVMap"]["SR2"] = "TprimeBBM800"
globalReplacementMap['Tprime_M800']["catRVMap"] = od()
globalReplacementMap['Tprime_M800']["catRVMap"]["SR1"] = "SR1"
globalReplacementMap['Tprime_M800']["catRVMap"]["SR2"] = "SR2"

#ttHHggXX Tprime M850 
globalReplacementMap['Tprime_M850'] = od()
globalReplacementMap['Tprime_M850']['procWV'] = "TprimeBBM850"
globalReplacementMap['Tprime_M850']['catWV'] = "TprimeBBM850_SR1"
globalReplacementMap['Tprime_M850']['catWV'] = "TprimeBBM850_SR2"
globalReplacementMap['Tprime_M850']['procRVMap'] = od()
globalReplacementMap['Tprime_M850']["procRVMap"]["SR1"] = "TprimeBBM850"
globalReplacementMap['Tprime_M850']["procRVMap"]["SR2"] = "TprimeBBM850"
globalReplacementMap['Tprime_M850']["catRVMap"] = od()
globalReplacementMap['Tprime_M850']["catRVMap"]["SR1"] = "SR1"
globalReplacementMap['Tprime_M850']["catRVMap"]["SR2"] = "SR2"

#ttHHggXX Tprime M900 
globalReplacementMap['Tprime_M900'] = od()
globalReplacementMap['Tprime_M900']['procWV'] = "TprimeBBM900"
globalReplacementMap['Tprime_M900']['catWV'] = "TprimeBBM900_SR1"
globalReplacementMap['Tprime_M900']['catWV'] = "TprimeBBM900_SR2"
globalReplacementMap['Tprime_M900']['procRVMap'] = od()
globalReplacementMap['Tprime_M900']["procRVMap"]["SR1"] = "TprimeBBM900"
globalReplacementMap['Tprime_M900']["procRVMap"]["SR2"] = "TprimeBBM900"
globalReplacementMap['Tprime_M900']["catRVMap"] = od()
globalReplacementMap['Tprime_M900']["catRVMap"]["SR1"] = "SR1"
globalReplacementMap['Tprime_M900']["catRVMap"]["SR2"] = "SR2"

#ttHHggXX Tprime M950 
globalReplacementMap['Tprime_M950'] = od()
globalReplacementMap['Tprime_M950']['procWV'] = "TprimeBBM950"
globalReplacementMap['Tprime_M950']['catWV'] = "TprimeBBM950_SR1"
globalReplacementMap['Tprime_M950']['catWV'] = "TprimeBBM950_SR2"
globalReplacementMap['Tprime_M950']['procRVMap'] = od()
globalReplacementMap['Tprime_M950']["procRVMap"]["SR1"] = "TprimeBBM950"
globalReplacementMap['Tprime_M950']["procRVMap"]["SR2"] = "TprimeBBM950"
globalReplacementMap['Tprime_M950']["catRVMap"] = od()
globalReplacementMap['Tprime_M950']["catRVMap"]["SR1"] = "SR1"
globalReplacementMap['Tprime_M950']["catRVMap"]["SR2"] = "SR2"

#ttHHggXX Tprime M1000 
globalReplacementMap['Tprime_M1000'] = od()
globalReplacementMap['Tprime_M1000']['procWV'] = "TprimeBBM1000"
globalReplacementMap['Tprime_M1000']['catWV'] = "TprimeBBM1000_SR1"
globalReplacementMap['Tprime_M1000']['catWV'] = "TprimeBBM1000_SR2"
globalReplacementMap['Tprime_M1000']['procRVMap'] = od()
globalReplacementMap['Tprime_M1000']["procRVMap"]["SR1"] = "TprimeBBM1000"
globalReplacementMap['Tprime_M1000']["procRVMap"]["SR2"] = "TprimeBBM1000"
globalReplacementMap['Tprime_M1000']["catRVMap"] = od()
globalReplacementMap['Tprime_M1000']["catRVMap"]["SR1"] = "SR1"
globalReplacementMap['Tprime_M1000']["catRVMap"]["SR2"] = "SR2"

#ttHHggXX Tprime M1100 
globalReplacementMap['Tprime_M1100'] = od()
globalReplacementMap['Tprime_M1100']['procWV'] = "TprimeBBM1100"
globalReplacementMap['Tprime_M1100']['catWV'] = "TprimeBBM1100_SR1"
globalReplacementMap['Tprime_M1100']['catWV'] = "TprimeBBM1100_SR2"
globalReplacementMap['Tprime_M1100']['procRVMap'] = od()
globalReplacementMap['Tprime_M1100']["procRVMap"]["SR1"] = "TprimeBBM1100"
globalReplacementMap['Tprime_M1100']["procRVMap"]["SR2"] = "TprimeBBM1100"
globalReplacementMap['Tprime_M1100']["catRVMap"] = od()
globalReplacementMap['Tprime_M1100']["catRVMap"]["SR1"] = "SR1"
globalReplacementMap['Tprime_M1100']["catRVMap"]["SR2"] = "SR2"

#ttHHggXX Tprime M1200 
globalReplacementMap['Tprime_M1200'] = od()
globalReplacementMap['Tprime_M1200']['procWV'] = "TprimeBBM1200"
globalReplacementMap['Tprime_M1200']['catWV'] = "TprimeBBM1200_SR1"
globalReplacementMap['Tprime_M1200']['catWV'] = "TprimeBBM1200_SR2"
globalReplacementMap['Tprime_M1200']['procRVMap'] = od()
globalReplacementMap['Tprime_M1200']["procRVMap"]["SR1"] = "TprimeBBM1200"
globalReplacementMap['Tprime_M1200']["procRVMap"]["SR2"] = "TprimeBBM1200"
globalReplacementMap['Tprime_M1200']["catRVMap"] = od()
globalReplacementMap['Tprime_M1200']["catRVMap"]["SR1"] = "SR1"
globalReplacementMap['Tprime_M1200']["catRVMap"]["SR2"] = "SR1"

#ttHHggXX Tprime M1300 
globalReplacementMap['Tprime_M1300'] = od()
globalReplacementMap['Tprime_M1300']['procWV'] = "TprimeBBM1300"
globalReplacementMap['Tprime_M1300']['catWV'] = "TprimeBBM1300_SR1"
globalReplacementMap['Tprime_M1300']['catWV'] = "TprimeBBM1300_SR2"
globalReplacementMap['Tprime_M1300']['procRVMap'] = od()
globalReplacementMap['Tprime_M1300']["procRVMap"]["SR1"] = "TprimeBBM1300"
globalReplacementMap['Tprime_M1300']["procRVMap"]["SR2"] = "TprimeBBM1300"
globalReplacementMap['Tprime_M1300']["catRVMap"] = od()
globalReplacementMap['Tprime_M1300']["catRVMap"]["SR1"] = "SR1"
globalReplacementMap['Tprime_M1300']["catRVMap"]["SR2"] = "SR1"

#ttHHggXX Tprime M1400 
globalReplacementMap['Tprime_M1400'] = od()
globalReplacementMap['Tprime_M1400']['procWV'] = "TprimeBBM1400"
globalReplacementMap['Tprime_M1400']['catWV'] = "TprimeBBM1400_SR1"
globalReplacementMap['Tprime_M1400']['catWV'] = "TprimeBBM1400_SR2"
globalReplacementMap['Tprime_M1400']['procRVMap'] = od()
globalReplacementMap['Tprime_M1400']["procRVMap"]["SR1"] = "TprimeBBM1400"
globalReplacementMap['Tprime_M1400']["procRVMap"]["SR2"] = "TprimeBBM1400"
globalReplacementMap['Tprime_M1400']["catRVMap"] = od()
globalReplacementMap['Tprime_M1400']["catRVMap"]["SR1"] = "SR1"
globalReplacementMap['Tprime_M1400']["catRVMap"]["SR2"] = "SR1"

#ttHHggXX Tprime M1500 
globalReplacementMap['Tprime_M1500'] = od()
globalReplacementMap['Tprime_M1500']['procWV'] = "TprimeBBM1500"
globalReplacementMap['Tprime_M1500']['catWV'] = "TprimeBBM1500_SR1"
globalReplacementMap['Tprime_M1500']['catWV'] = "TprimeBBM1500_SR2"
globalReplacementMap['Tprime_M1500']['procRVMap'] = od()
globalReplacementMap['Tprime_M1500']["procRVMap"]["SR1"] = "TprimeBBM1500"
globalReplacementMap['Tprime_M1500']["procRVMap"]["SR2"] = "TprimeBBM1500"
globalReplacementMap['Tprime_M1500']["catRVMap"] = od()
globalReplacementMap['Tprime_M1500']["catRVMap"]["SR1"] = "SR1"
globalReplacementMap['Tprime_M1500']["catRVMap"]["SR2"] = "SR1"


# STXS analysis
globalReplacementMap['STXS'] = od()
# For WRONG VERTEX SCENARIO:
#  * single proc x cat for wrong vertex since for dZ > 1cm shape independent of proc x cat
#  * use proc x cat with highest number of WV events
globalReplacementMap['STXS']['procWV'] = "GG2H_0J_PTH_GT10"
globalReplacementMap['STXS']['catWV'] = "RECO_0J_PTH_GT10_Tag1"
# For RIGHT VERTEX SCENARIO:
#  * default mapping is to use diagonal process from given category 
#  * if few events in diagonal process then may need to change the category aswell (see catRVMap)
#  * map must contain entry for all cats being processed (for replacement proc and cat)
globalReplacementMap['STXS']['procRVMap'] = od()
globalReplacementMap["STXS"]["procRVMap"]["RECO_0J_PTH_0_10_Tag0"] = "GG2H_0J_PTH_0_10"
globalReplacementMap["STXS"]["procRVMap"]["RECO_0J_PTH_0_10_Tag1"] = "GG2H_0J_PTH_0_10"
globalReplacementMap["STXS"]["procRVMap"]["RECO_0J_PTH_0_10_Tag2"] = "GG2H_0J_PTH_0_10"
globalReplacementMap["STXS"]["procRVMap"]["RECO_0J_PTH_GT10_Tag0"] = "GG2H_0J_PTH_GT10"
globalReplacementMap["STXS"]["procRVMap"]["RECO_0J_PTH_GT10_Tag1"] = "GG2H_0J_PTH_GT10"
globalReplacementMap["STXS"]["procRVMap"]["RECO_0J_PTH_GT10_Tag2"] = "GG2H_0J_PTH_GT10"
globalReplacementMap["STXS"]["procRVMap"]["RECO_1J_PTH_0_60_Tag0"] = "GG2H_1J_PTH_0_60"
globalReplacementMap["STXS"]["procRVMap"]["RECO_1J_PTH_0_60_Tag1"] = "GG2H_1J_PTH_0_60"
globalReplacementMap["STXS"]["procRVMap"]["RECO_1J_PTH_0_60_Tag2"] = "GG2H_1J_PTH_0_60"
globalReplacementMap["STXS"]["procRVMap"]["RECO_1J_PTH_120_200_Tag0"] = "GG2H_1J_PTH_120_200"
globalReplacementMap["STXS"]["procRVMap"]["RECO_1J_PTH_120_200_Tag1"] = "GG2H_1J_PTH_120_200"
globalReplacementMap["STXS"]["procRVMap"]["RECO_1J_PTH_120_200_Tag2"] = "GG2H_1J_PTH_120_200"
globalReplacementMap["STXS"]["procRVMap"]["RECO_1J_PTH_60_120_Tag0"] = "GG2H_1J_PTH_60_120"
globalReplacementMap["STXS"]["procRVMap"]["RECO_1J_PTH_60_120_Tag1"] = "GG2H_1J_PTH_60_120"
globalReplacementMap["STXS"]["procRVMap"]["RECO_1J_PTH_60_120_Tag2"] = "GG2H_1J_PTH_60_120"
globalReplacementMap["STXS"]["procRVMap"]["RECO_GE2J_PTH_0_60_Tag0"] = "GG2H_GE2J_MJJ_0_350_PTH_0_60"
globalReplacementMap["STXS"]["procRVMap"]["RECO_GE2J_PTH_0_60_Tag1"] = "GG2H_GE2J_MJJ_0_350_PTH_0_60"
globalReplacementMap["STXS"]["procRVMap"]["RECO_GE2J_PTH_0_60_Tag2"] = "GG2H_GE2J_MJJ_0_350_PTH_0_60"
globalReplacementMap["STXS"]["procRVMap"]["RECO_GE2J_PTH_120_200_Tag0"] = "GG2H_GE2J_MJJ_0_350_PTH_120_200"
globalReplacementMap["STXS"]["procRVMap"]["RECO_GE2J_PTH_120_200_Tag1"] = "GG2H_GE2J_MJJ_0_350_PTH_120_200"
globalReplacementMap["STXS"]["procRVMap"]["RECO_GE2J_PTH_120_200_Tag2"] = "GG2H_GE2J_MJJ_0_350_PTH_120_200"
globalReplacementMap["STXS"]["procRVMap"]["RECO_GE2J_PTH_60_120_Tag0"] = "GG2H_GE2J_MJJ_0_350_PTH_60_120"
globalReplacementMap["STXS"]["procRVMap"]["RECO_GE2J_PTH_60_120_Tag1"] = "GG2H_GE2J_MJJ_0_350_PTH_60_120"
globalReplacementMap["STXS"]["procRVMap"]["RECO_GE2J_PTH_60_120_Tag2"] = "GG2H_GE2J_MJJ_0_350_PTH_60_120"
globalReplacementMap["STXS"]["procRVMap"]["RECO_PTH_200_300_Tag0"] = "GG2H_PTH_200_300"
globalReplacementMap["STXS"]["procRVMap"]["RECO_PTH_200_300_Tag1"] = "GG2H_PTH_200_300"
globalReplacementMap["STXS"]["procRVMap"]["RECO_PTH_300_450_Tag0"] = "GG2H_PTH_300_450"
globalReplacementMap["STXS"]["procRVMap"]["RECO_PTH_300_450_Tag1"] = "GG2H_PTH_300_450"
globalReplacementMap["STXS"]["procRVMap"]["RECO_PTH_450_650_Tag0"] = "GG2H_PTH_450_650"
globalReplacementMap["STXS"]["procRVMap"]["RECO_PTH_GT650_Tag0"] = "GG2H_PTH_GT650"
globalReplacementMap["STXS"]["procRVMap"]["RECO_THQ_LEP"] = "THQ"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_0_60_Tag0"] = "TTH_PTH_0_60"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_0_60_Tag1"] = "TTH_PTH_0_60"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_0_60_Tag2"] = "TTH_PTH_0_60"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_0_60_Tag3"] = "TTH_PTH_0_60"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_120_200_Tag0"] = "TTH_PTH_120_200"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_120_200_Tag1"] = "TTH_PTH_120_200"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_120_200_Tag2"] = "TTH_PTH_120_200"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_120_200_Tag3"] = "TTH_PTH_120_200"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_200_300_Tag0"] = "TTH_PTH_200_300"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_200_300_Tag1"] = "TTH_PTH_200_300"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_200_300_Tag2"] = "TTH_PTH_200_300"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_60_120_Tag0"] = "TTH_PTH_60_120"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_60_120_Tag1"] = "TTH_PTH_60_120"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_60_120_Tag2"] = "TTH_PTH_60_120"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_60_120_Tag3"] = "TTH_PTH_60_120"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_GT300_Tag0"] = "TTH_PTH_GT300"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_GT300_Tag1"] = "TTH_PTH_GT300"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_GT300_Tag2"] = "TTH_PTH_GT300"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_LEP_PTH_0_60_Tag0"] = "TTH_PTH_0_60"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_LEP_PTH_0_60_Tag1"] = "TTH_PTH_0_60"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_LEP_PTH_0_60_Tag2"] = "TTH_PTH_0_60"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_LEP_PTH_120_200_Tag0"] = "TTH_PTH_120_200"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_LEP_PTH_120_200_Tag1"] = "TTH_PTH_120_200"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_LEP_PTH_200_300_Tag0"] = "TTH_PTH_200_300"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_LEP_PTH_200_300_Tag1"] = "TTH_PTH_200_300"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_LEP_PTH_60_120_Tag0"] = "TTH_PTH_60_120"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_LEP_PTH_60_120_Tag1"] = "TTH_PTH_60_120"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_LEP_PTH_60_120_Tag2"] = "TTH_PTH_60_120"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_LEP_PTH_GT300_Tag0"] = "TTH_PTH_GT300"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VBFLIKEGGH_Tag0"] = "GG2H_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VBFLIKEGGH_Tag1"] = "GG2H_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VBFTOPO_BSM_Tag0"] = "VBF_GE2J_MJJ_GT350_PTH_GT200"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VBFTOPO_BSM_Tag1"] = "VBF_GE2J_MJJ_GT350_PTH_GT200"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VBFTOPO_JET3VETO_HIGHMJJ_Tag0"] = "VBF_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VBFTOPO_JET3VETO_HIGHMJJ_Tag1"] = "VBF_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VBFTOPO_JET3VETO_LOWMJJ_Tag0"] = "VBF_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VBFTOPO_JET3VETO_LOWMJJ_Tag1"] = "VBF_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VBFTOPO_JET3_HIGHMJJ_Tag0"] = "VBF_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VBFTOPO_JET3_HIGHMJJ_Tag1"] = "VBF_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VBFTOPO_JET3_LOWMJJ_Tag0"] = "GG2H_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VBFTOPO_JET3_LOWMJJ_Tag1"] = "GG2H_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VBFTOPO_VHHAD_Tag0"] = "WH2HQQ_GE2J_MJJ_60_120"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VBFTOPO_VHHAD_Tag1"] = "GG2H_GE2J_MJJ_0_350_PTH_120_200"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VH_MET_Tag0"] = "QQ2HLL_PTV_150_250_0J"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VH_MET_Tag1"] = "QQ2HLL_PTV_75_150"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VH_MET_Tag2"] = "QQ2HLL_PTV_75_150"
globalReplacementMap["STXS"]["procRVMap"]["RECO_WH_LEP_PTV_0_75_Tag0"] = "QQ2HLNU_PTV_0_75"
globalReplacementMap["STXS"]["procRVMap"]["RECO_WH_LEP_PTV_0_75_Tag1"] = "QQ2HLNU_PTV_0_75"
globalReplacementMap["STXS"]["procRVMap"]["RECO_WH_LEP_PTV_75_150_Tag0"] = "QQ2HLNU_PTV_75_150"
globalReplacementMap["STXS"]["procRVMap"]["RECO_WH_LEP_PTV_75_150_Tag1"] = "QQ2HLNU_PTV_75_150"
globalReplacementMap["STXS"]["procRVMap"]["RECO_WH_LEP_PTV_GT150_Tag0"] = "QQ2HLNU_PTV_150_250_0J"
globalReplacementMap["STXS"]["procRVMap"]["RECO_ZH_LEP_Tag0"] = "QQ2HLL_PTV_0_75"
globalReplacementMap["STXS"]["procRVMap"]["RECO_ZH_LEP_Tag1"] = "QQ2HLL_PTV_0_75"
# Replacement category for RV fit
globalReplacementMap["STXS"]["catRVMap"] = od()
globalReplacementMap["STXS"]["catRVMap"]["RECO_0J_PTH_0_10_Tag0"] = "RECO_0J_PTH_0_10_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_0J_PTH_0_10_Tag1"] = "RECO_0J_PTH_0_10_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_0J_PTH_0_10_Tag2"] = "RECO_0J_PTH_0_10_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_0J_PTH_GT10_Tag0"] = "RECO_0J_PTH_GT10_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_0J_PTH_GT10_Tag1"] = "RECO_0J_PTH_GT10_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_0J_PTH_GT10_Tag2"] = "RECO_0J_PTH_GT10_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_1J_PTH_0_60_Tag0"] = "RECO_1J_PTH_0_60_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_1J_PTH_0_60_Tag1"] = "RECO_1J_PTH_0_60_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_1J_PTH_0_60_Tag2"] = "RECO_1J_PTH_0_60_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_1J_PTH_120_200_Tag0"] = "RECO_1J_PTH_120_200_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_1J_PTH_120_200_Tag1"] = "RECO_1J_PTH_120_200_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_1J_PTH_120_200_Tag2"] = "RECO_1J_PTH_120_200_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_1J_PTH_60_120_Tag0"] = "RECO_1J_PTH_60_120_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_1J_PTH_60_120_Tag1"] = "RECO_1J_PTH_60_120_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_1J_PTH_60_120_Tag2"] = "RECO_1J_PTH_60_120_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_GE2J_PTH_0_60_Tag0"] = "RECO_GE2J_PTH_0_60_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_GE2J_PTH_0_60_Tag1"] = "RECO_GE2J_PTH_0_60_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_GE2J_PTH_0_60_Tag2"] = "RECO_GE2J_PTH_0_60_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_GE2J_PTH_120_200_Tag0"] = "RECO_GE2J_PTH_120_200_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_GE2J_PTH_120_200_Tag1"] = "RECO_GE2J_PTH_120_200_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_GE2J_PTH_120_200_Tag2"] = "RECO_GE2J_PTH_120_200_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_GE2J_PTH_60_120_Tag0"] = "RECO_GE2J_PTH_60_120_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_GE2J_PTH_60_120_Tag1"] = "RECO_GE2J_PTH_60_120_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_GE2J_PTH_60_120_Tag2"] = "RECO_GE2J_PTH_60_120_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_PTH_200_300_Tag0"] = "RECO_PTH_200_300_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_PTH_200_300_Tag1"] = "RECO_PTH_200_300_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_PTH_300_450_Tag0"] = "RECO_PTH_300_450_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_PTH_300_450_Tag1"] = "RECO_PTH_300_450_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_PTH_450_650_Tag0"] = "RECO_PTH_450_650_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_PTH_GT650_Tag0"] = "RECO_PTH_GT650_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_THQ_LEP"] = "RECO_THQ_LEP"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_0_60_Tag0"] = "RECO_TTH_HAD_PTH_0_60_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_0_60_Tag1"] = "RECO_TTH_HAD_PTH_0_60_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_0_60_Tag2"] = "RECO_TTH_HAD_PTH_0_60_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_0_60_Tag3"] = "RECO_TTH_HAD_PTH_0_60_Tag3"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_120_200_Tag0"] = "RECO_TTH_HAD_PTH_120_200_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_120_200_Tag1"] = "RECO_TTH_HAD_PTH_120_200_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_120_200_Tag2"] = "RECO_TTH_HAD_PTH_120_200_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_120_200_Tag3"] = "RECO_TTH_HAD_PTH_120_200_Tag3"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_200_300_Tag0"] = "RECO_TTH_HAD_PTH_200_300_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_200_300_Tag1"] = "RECO_TTH_HAD_PTH_200_300_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_200_300_Tag2"] = "RECO_TTH_HAD_PTH_200_300_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_60_120_Tag0"] = "RECO_TTH_HAD_PTH_60_120_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_60_120_Tag1"] = "RECO_TTH_HAD_PTH_60_120_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_60_120_Tag2"] = "RECO_TTH_HAD_PTH_60_120_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_60_120_Tag3"] = "RECO_TTH_HAD_PTH_60_120_Tag3"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_GT300_Tag0"] = "RECO_TTH_HAD_PTH_GT300_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_GT300_Tag1"] = "RECO_TTH_HAD_PTH_GT300_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_GT300_Tag2"] = "RECO_TTH_HAD_PTH_GT300_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_LEP_PTH_0_60_Tag0"] = "RECO_TTH_LEP_PTH_0_60_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_LEP_PTH_0_60_Tag1"] = "RECO_TTH_LEP_PTH_0_60_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_LEP_PTH_0_60_Tag2"] = "RECO_TTH_LEP_PTH_0_60_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_LEP_PTH_120_200_Tag0"] = "RECO_TTH_LEP_PTH_120_200_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_LEP_PTH_120_200_Tag1"] = "RECO_TTH_LEP_PTH_120_200_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_LEP_PTH_200_300_Tag0"] = "RECO_TTH_LEP_PTH_200_300_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_LEP_PTH_200_300_Tag1"] = "RECO_TTH_LEP_PTH_200_300_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_LEP_PTH_60_120_Tag0"] = "RECO_TTH_LEP_PTH_60_120_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_LEP_PTH_60_120_Tag1"] = "RECO_TTH_LEP_PTH_60_120_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_LEP_PTH_60_120_Tag2"] = "RECO_TTH_LEP_PTH_60_120_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_LEP_PTH_GT300_Tag0"] = "RECO_TTH_LEP_PTH_GT300_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VBFLIKEGGH_Tag0"] = "RECO_VBFLIKEGGH_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VBFLIKEGGH_Tag1"] = "RECO_VBFLIKEGGH_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VBFTOPO_BSM_Tag0"] = "RECO_VBFTOPO_BSM_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VBFTOPO_BSM_Tag1"] = "RECO_VBFTOPO_BSM_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VBFTOPO_JET3VETO_HIGHMJJ_Tag0"] = "RECO_VBFTOPO_JET3VETO_HIGHMJJ_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VBFTOPO_JET3VETO_HIGHMJJ_Tag1"] = "RECO_VBFTOPO_JET3VETO_HIGHMJJ_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VBFTOPO_JET3VETO_LOWMJJ_Tag0"] = "RECO_VBFTOPO_JET3VETO_LOWMJJ_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VBFTOPO_JET3VETO_LOWMJJ_Tag1"] = "RECO_VBFTOPO_JET3VETO_LOWMJJ_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VBFTOPO_JET3_HIGHMJJ_Tag0"] = "RECO_VBFTOPO_JET3_HIGHMJJ_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VBFTOPO_JET3_HIGHMJJ_Tag1"] = "RECO_VBFTOPO_JET3_HIGHMJJ_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VBFTOPO_JET3_LOWMJJ_Tag0"] = "RECO_VBFTOPO_JET3_LOWMJJ_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VBFTOPO_JET3_LOWMJJ_Tag1"] = "RECO_VBFTOPO_JET3_LOWMJJ_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VBFTOPO_VHHAD_Tag0"] = "RECO_VBFTOPO_VHHAD_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VBFTOPO_VHHAD_Tag1"] = "RECO_VBFTOPO_VHHAD_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VH_MET_Tag0"] = "RECO_VH_MET_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VH_MET_Tag1"] = "RECO_VH_MET_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VH_MET_Tag2"] = "RECO_VH_MET_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_WH_LEP_PTV_0_75_Tag0"] = "RECO_WH_LEP_PTV_0_75_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_WH_LEP_PTV_0_75_Tag1"] = "RECO_WH_LEP_PTV_0_75_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_WH_LEP_PTV_75_150_Tag0"] = "RECO_WH_LEP_PTV_75_150_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_WH_LEP_PTV_75_150_Tag1"] = "RECO_WH_LEP_PTV_75_150_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_WH_LEP_PTV_GT150_Tag0"] = "RECO_WH_LEP_PTV_GT150_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_ZH_LEP_Tag0"] = "RECO_ZH_LEP_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_ZH_LEP_Tag1"] = "RECO_ZH_LEP_Tag1"
