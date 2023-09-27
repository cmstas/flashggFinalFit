# Python script to hold XS * BR for normalisation of signal models
from collections import OrderedDict as od
from commonObjects import *
  
# Add analyses to globalReplacementMap. See "STXS" as an example
globalXSBRMap = od()

# For case of fixed xs/br Use 'mode':constant 'factor':X e.g.
#globalXSBRMap['example'] = od()
#globalXSBRMap['example']['decay'] = {'mode':'constant','factor':1}
#globalXSBRMap['example']['PROCNAME'] = {'mode':'constant','factor':0.001}

# ttHH SM mappings
globalXSBRMap['ttHHggXX'] = od()
globalXSBRMap['ttHHggXX']['decay'] = {'mode':'constant','factor':1}
globalXSBRMap['ttHHggXX']['ttHHggbb'] = {'mode':'constant','factor':1}
globalXSBRMap['ttHHggXX']['ttHHggWW'] = {'mode':'constant','factor':1}
globalXSBRMap['ttHHggXX']['ttHHggTauTau'] = {'mode':'constant','factor':1}
globalXSBRMap['ttHHggXX']['ggH'] = {'mode':'ggH'}
globalXSBRMap['ttHHggXX']['ttH'] = {'mode':'ttH'}
globalXSBRMap['ttHHggXX']['VBFH'] = {'mode':'qqH'}
globalXSBRMap['ttHHggXX']['VH'] = {'mode':'VH'}
globalXSBRMap['ttHHggXX']['HHGGbb'] = {'mode':'constant','factor':1}
globalXSBRMap['ttHHggXX']['HHGGWWdileptonic'] = {'mode':'constant','factor':1}
globalXSBRMap['ttHHggXX']['HHGGWWsemileptonic'] = {'mode':'constant','factor':1}
globalXSBRMap['ttHHggXX']['HHGGTauTau'] = {'mode':'constant','factor':1}

# 2HDM M250
globalXSBRMap['2HDM_M250'] = od()
globalXSBRMap['2HDM_M250']['decay'] = {'mode':'constant','factor':1}
globalXSBRMap['2HDM_M250']['2HDMbbM250'] = {'mode':'constant','factor':1}
globalXSBRMap['2HDM_M250']['2HDMWWM250'] = {'mode':'constant','factor':1}
globalXSBRMap['2HDM_M250']['2HDMTAUTAUM250'] = {'mode':'constant','factor':1}
globalXSBRMap['2HDM_M250']['ttHHggbb'] = {'mode':'constant','factor':1}
globalXSBRMap['2HDM_M250']['ttHHggWW'] = {'mode':'constant','factor':1}
globalXSBRMap['2HDM_M250']['ttHHggTauTau'] = {'mode':'constant','factor':1}
globalXSBRMap['2HDM_M250']['ggH'] = {'mode':'ggH'}
globalXSBRMap['2HDM_M250']['ttH'] = {'mode':'ttH'}
globalXSBRMap['2HDM_M250']['VBFH'] = {'mode':'qqH'}
globalXSBRMap['2HDM_M250']['VH'] = {'mode':'VH'}
globalXSBRMap['2HDM_M250']['HHGGbb'] = {'mode':'constant','factor':1}
globalXSBRMap['2HDM_M250']['HHGGWWdileptonic'] = {'mode':'constant','factor':1}
globalXSBRMap['2HDM_M250']['HHGGWWsemileptonic'] = {'mode':'constant','factor':1}
globalXSBRMap['2HDM_M250']['HHGGTauTau'] = {'mode':'constant','factor':1}

# 2HDM M300
globalXSBRMap['2HDM_M300'] = od()
globalXSBRMap['2HDM_M300']['decay'] = {'mode':'constant','factor':1}
globalXSBRMap['2HDM_M300']['2HDMbbM300'] = {'mode':'constant','factor':1}
globalXSBRMap['2HDM_M300']['2HDMWWM300'] = {'mode':'constant','factor':1}
globalXSBRMap['2HDM_M300']['2HDMTAUTAUM300'] = {'mode':'constant','factor':1}
globalXSBRMap['2HDM_M300']['ttHHggbb'] = {'mode':'constant','factor':1}
globalXSBRMap['2HDM_M300']['ttHHggWW'] = {'mode':'constant','factor':1}
globalXSBRMap['2HDM_M300']['ttHHggTauTau'] = {'mode':'constant','factor':1}
globalXSBRMap['2HDM_M300']['ggH'] = {'mode':'ggH'}
globalXSBRMap['2HDM_M300']['ttH'] = {'mode':'ttH'}
globalXSBRMap['2HDM_M300']['VBFH'] = {'mode':'qqH'}
globalXSBRMap['2HDM_M300']['VH'] = {'mode':'VH'}
globalXSBRMap['2HDM_M300']['HHGGbb'] = {'mode':'constant','factor':1}
globalXSBRMap['2HDM_M300']['HHGGWWdileptonic'] = {'mode':'constant','factor':1}
globalXSBRMap['2HDM_M300']['HHGGWWsemileptonic'] = {'mode':'constant','factor':1}
globalXSBRMap['2HDM_M300']['HHGGTauTau'] = {'mode':'constant','factor':1}

# 2HDM M350
globalXSBRMap['2HDM_M350'] = od()
globalXSBRMap['2HDM_M350']['decay'] = {'mode':'constant','factor':1}
globalXSBRMap['2HDM_M350']['2HDMbbM350'] = {'mode':'constant','factor':1}
globalXSBRMap['2HDM_M350']['2HDMWWM350'] = {'mode':'constant','factor':1}
globalXSBRMap['2HDM_M350']['2HDMTAUTAUM350'] = {'mode':'constant','factor':1}
globalXSBRMap['2HDM_M350']['ttHHggbb'] = {'mode':'constant','factor':1}
globalXSBRMap['2HDM_M350']['ttHHggWW'] = {'mode':'constant','factor':1}
globalXSBRMap['2HDM_M350']['ttHHggTauTau'] = {'mode':'constant','factor':1}
globalXSBRMap['2HDM_M350']['ggH'] = {'mode':'ggH'}
globalXSBRMap['2HDM_M350']['ttH'] = {'mode':'ttH'}
globalXSBRMap['2HDM_M350']['VBFH'] = {'mode':'qqH'}
globalXSBRMap['2HDM_M350']['VH'] = {'mode':'VH'}
globalXSBRMap['2HDM_M350']['HHGGbb'] = {'mode':'constant','factor':1}
globalXSBRMap['2HDM_M350']['HHGGWWdileptonic'] = {'mode':'constant','factor':1}
globalXSBRMap['2HDM_M350']['HHGGWWsemileptonic'] = {'mode':'constant','factor':1}
globalXSBRMap['2HDM_M350']['HHGGTauTau'] = {'mode':'constant','factor':1}

# TPrime M500
globalXSBRMap['Tprime_M500'] = od()
globalXSBRMap['Tprime_M500']['decay'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M500']['TprimeBBM500'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M500']['TprimeWWM500'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M500']['TprimeTAUTAUM500'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M500']['ttHHggbb'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M500']['ttHHggWW'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M500']['ttHHggTauTau'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M500']['ggH'] = {'mode':'ggH'}
globalXSBRMap['Tprime_M500']['ttH'] = {'mode':'ttH'}
globalXSBRMap['Tprime_M500']['VBFH'] = {'mode':'qqH'}
globalXSBRMap['Tprime_M500']['VH'] = {'mode':'VH'}
globalXSBRMap['Tprime_M500']['HHGGbb'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M500']['HHGGWWdileptonic'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M500']['HHGGWWsemileptonic'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M500']['HHGGTauTau'] = {'mode':'constant','factor':1}

# TPrime M550
globalXSBRMap['Tprime_M550'] = od()
globalXSBRMap['Tprime_M550']['decay'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M550']['TprimeBBM550'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M550']['TprimeWWM550'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M550']['TprimeTAUTAUM550'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M550']['ttHHggbb'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M550']['ttHHggWW'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M550']['ttHHggTauTau'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M550']['ggH'] = {'mode':'ggH'}
globalXSBRMap['Tprime_M550']['ttH'] = {'mode':'ttH'}
globalXSBRMap['Tprime_M550']['VBFH'] = {'mode':'qqH'}
globalXSBRMap['Tprime_M550']['VH'] = {'mode':'VH'}
globalXSBRMap['Tprime_M550']['HHGGbb'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M550']['HHGGWWdileptonic'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M550']['HHGGWWsemileptonic'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M550']['HHGGTauTau'] = {'mode':'constant','factor':1}

# TPrime M600
globalXSBRMap['Tprime_M600'] = od()
globalXSBRMap['Tprime_M600']['decay'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M600']['TprimeBBM600'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M600']['TprimeWWM600'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M600']['TprimeTAUTAUM600'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M600']['ttHHggbb'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M600']['ttHHggWW'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M600']['ttHHggTauTau'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M600']['ggH'] = {'mode':'ggH'}
globalXSBRMap['Tprime_M600']['ttH'] = {'mode':'ttH'}
globalXSBRMap['Tprime_M600']['VBFH'] = {'mode':'qqH'}
globalXSBRMap['Tprime_M600']['VH'] = {'mode':'VH'}
globalXSBRMap['Tprime_M600']['HHGGbb'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M600']['HHGGWWdileptonic'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M600']['HHGGWWsemileptonic'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M600']['HHGGTauTau'] = {'mode':'constant','factor':1}

# TPrime M650
globalXSBRMap['Tprime_M650'] = od()
globalXSBRMap['Tprime_M650']['decay'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M650']['TprimeBBM650'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M650']['TprimeWWM650'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M650']['TprimeTAUTAUM650'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M650']['ttHHggbb'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M650']['ttHHggWW'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M650']['ttHHggTauTau'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M650']['ggH'] = {'mode':'ggH'}
globalXSBRMap['Tprime_M650']['ttH'] = {'mode':'ttH'}
globalXSBRMap['Tprime_M650']['VBFH'] = {'mode':'qqH'}
globalXSBRMap['Tprime_M650']['VH'] = {'mode':'VH'}
globalXSBRMap['Tprime_M650']['HHGGbb'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M650']['HHGGWWdileptonic'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M650']['HHGGWWsemileptonic'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M650']['HHGGTauTau'] = {'mode':'constant','factor':1}

# TPrime M700
globalXSBRMap['Tprime_M700'] = od()
globalXSBRMap['Tprime_M700']['decay'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M700']['TprimeBBM700'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M700']['TprimeWWM700'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M700']['TprimeTAUTAUM700'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M700']['ttHHggbb'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M700']['ttHHggWW'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M700']['ttHHggTauTau'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M700']['ggH'] = {'mode':'ggH'}
globalXSBRMap['Tprime_M700']['ttH'] = {'mode':'ttH'}
globalXSBRMap['Tprime_M700']['VBFH'] = {'mode':'qqH'}
globalXSBRMap['Tprime_M700']['VH'] = {'mode':'VH'}
globalXSBRMap['Tprime_M700']['HHGGbb'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M700']['HHGGWWdileptonic'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M700']['HHGGWWsemileptonic'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M700']['HHGGTauTau'] = {'mode':'constant','factor':1}

# TPrime M750
globalXSBRMap['Tprime_M750'] = od()
globalXSBRMap['Tprime_M750']['decay'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M750']['TprimeBBM750'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M750']['TprimeWWM750'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M750']['TprimeTAUTAUM750'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M750']['ttHHggbb'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M750']['ttHHggWW'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M750']['ttHHggTauTau'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M750']['ggH'] = {'mode':'ggH'}
globalXSBRMap['Tprime_M750']['ttH'] = {'mode':'ttH'}
globalXSBRMap['Tprime_M750']['VBFH'] = {'mode':'qqH'}
globalXSBRMap['Tprime_M750']['VH'] = {'mode':'VH'}
globalXSBRMap['Tprime_M750']['HHGGbb'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M750']['HHGGWWdileptonic'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M750']['HHGGWWsemileptonic'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M750']['HHGGTauTau'] = {'mode':'constant','factor':1}

# TPrime M800
globalXSBRMap['Tprime_M800'] = od()
globalXSBRMap['Tprime_M800']['decay'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M800']['TprimeBBM800'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M800']['TprimeWWM800'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M800']['TprimeTAUTAUM800'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M800']['ttHHggbb'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M800']['ttHHggWW'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M800']['ttHHggTauTau'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M800']['ggH'] = {'mode':'ggH'}
globalXSBRMap['Tprime_M800']['ttH'] = {'mode':'ttH'}
globalXSBRMap['Tprime_M800']['VBFH'] = {'mode':'qqH'}
globalXSBRMap['Tprime_M800']['VH'] = {'mode':'VH'}
globalXSBRMap['Tprime_M800']['HHGGbb'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M800']['HHGGWWdileptonic'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M800']['HHGGWWsemileptonic'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M800']['HHGGTauTau'] = {'mode':'constant','factor':1}

# TPrime M850
globalXSBRMap['Tprime_M850'] = od()
globalXSBRMap['Tprime_M850']['decay'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M850']['TprimeBBM850'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M850']['TprimeWWM850'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M850']['TprimeTAUTAUM850'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M850']['ttHHggbb'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M850']['ttHHggWW'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M850']['ttHHggTauTau'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M850']['ggH'] = {'mode':'ggH'}
globalXSBRMap['Tprime_M850']['ttH'] = {'mode':'ttH'}
globalXSBRMap['Tprime_M850']['VBFH'] = {'mode':'qqH'}
globalXSBRMap['Tprime_M850']['VH'] = {'mode':'VH'}
globalXSBRMap['Tprime_M850']['HHGGbb'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M850']['HHGGWWdileptonic'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M850']['HHGGWWsemileptonic'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M850']['HHGGTauTau'] = {'mode':'constant','factor':1}

# TPrime M900
globalXSBRMap['Tprime_M900'] = od()
globalXSBRMap['Tprime_M900']['decay'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M900']['TprimeBBM900'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M900']['TprimeWWM900'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M900']['TprimeTAUTAUM900'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M900']['ttHHggbb'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M900']['ttHHggWW'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M900']['ttHHggTauTau'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M900']['ggH'] = {'mode':'ggH'}
globalXSBRMap['Tprime_M900']['ttH'] = {'mode':'ttH'}
globalXSBRMap['Tprime_M900']['VBFH'] = {'mode':'qqH'}
globalXSBRMap['Tprime_M900']['VH'] = {'mode':'VH'}
globalXSBRMap['Tprime_M900']['HHGGbb'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M900']['HHGGWWdileptonic'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M900']['HHGGWWsemileptonic'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M900']['HHGGTauTau'] = {'mode':'constant','factor':1}

# TPrime M950
globalXSBRMap['Tprime_M950'] = od()
globalXSBRMap['Tprime_M950']['decay'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M950']['TprimeBBM950'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M950']['TprimeWWM950'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M950']['TprimeTAUTAUM950'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M950']['ttHHggbb'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M950']['ttHHggWW'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M950']['ttHHggTauTau'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M950']['ggH'] = {'mode':'ggH'}
globalXSBRMap['Tprime_M950']['ttH'] = {'mode':'ttH'}
globalXSBRMap['Tprime_M950']['VBFH'] = {'mode':'qqH'}
globalXSBRMap['Tprime_M950']['VH'] = {'mode':'VH'}
globalXSBRMap['Tprime_M950']['HHGGbb'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M950']['HHGGWWdileptonic'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M950']['HHGGWWsemileptonic'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M950']['HHGGTauTau'] = {'mode':'constant','factor':1}

# TPrime M1000
globalXSBRMap['Tprime_M1000'] = od()
globalXSBRMap['Tprime_M1000']['decay'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1000']['TprimeBBM1000'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1000']['TprimeWWM1000'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1000']['TprimeTAUTAUM1000'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1000']['ttHHggbb'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1000']['ttHHggWW'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1000']['ttHHggTauTau'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1000']['ggH'] = {'mode':'ggH'}
globalXSBRMap['Tprime_M1000']['ttH'] = {'mode':'ttH'}
globalXSBRMap['Tprime_M1000']['VBFH'] = {'mode':'qqH'}
globalXSBRMap['Tprime_M1000']['VH'] = {'mode':'VH'}
globalXSBRMap['Tprime_M1000']['HHGGbb'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1000']['HHGGWWdileptonic'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1000']['HHGGWWsemileptonic'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1000']['HHGGTauTau'] = {'mode':'constant','factor':1}

# TPrime M1100
globalXSBRMap['Tprime_M1100'] = od()
globalXSBRMap['Tprime_M1100']['decay'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1100']['TprimeBBM1100'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1100']['TprimeWWM1100'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1100']['TprimeTAUTAUM1100'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1100']['ttHHggbb'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1100']['ttHHggWW'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1100']['ttHHggTauTau'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1100']['ggH'] = {'mode':'ggH'}
globalXSBRMap['Tprime_M1100']['ttH'] = {'mode':'ttH'}
globalXSBRMap['Tprime_M1100']['VBFH'] = {'mode':'qqH'}
globalXSBRMap['Tprime_M1100']['VH'] = {'mode':'VH'}
globalXSBRMap['Tprime_M1100']['HHGGbb'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1100']['HHGGWWdileptonic'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1100']['HHGGWWsemileptonic'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1100']['HHGGTauTau'] = {'mode':'constant','factor':1}

# TPrime M1200
globalXSBRMap['Tprime_M1200'] = od()
globalXSBRMap['Tprime_M1200']['decay'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1200']['TprimeBBM1200'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1200']['TprimeWWM1200'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1200']['TprimeTAUTAUM1200'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1200']['ttHHggbb'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1200']['ttHHggWW'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1200']['ttHHggTauTau'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1200']['ggH'] = {'mode':'ggH'}
globalXSBRMap['Tprime_M1200']['ttH'] = {'mode':'ttH'}
globalXSBRMap['Tprime_M1200']['VBFH'] = {'mode':'qqH'}
globalXSBRMap['Tprime_M1200']['VH'] = {'mode':'VH'}
globalXSBRMap['Tprime_M1200']['HHGGbb'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1200']['HHGGWWdileptonic'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1200']['HHGGWWsemileptonic'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1200']['HHGGTauTau'] = {'mode':'constant','factor':1}

# TPrime M1300
globalXSBRMap['Tprime_M1300'] = od()
globalXSBRMap['Tprime_M1300']['decay'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1300']['TprimeBBM1300'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1300']['TprimeWWM1300'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1300']['TprimeTAUTAUM1300'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1300']['ttHHggbb'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1300']['ttHHggWW'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1300']['ttHHggTauTau'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1300']['ggH'] = {'mode':'ggH'}
globalXSBRMap['Tprime_M1300']['ttH'] = {'mode':'ttH'}
globalXSBRMap['Tprime_M1300']['VBFH'] = {'mode':'qqH'}
globalXSBRMap['Tprime_M1300']['VH'] = {'mode':'VH'}
globalXSBRMap['Tprime_M1300']['HHGGbb'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1300']['HHGGWWdileptonic'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1300']['HHGGWWsemileptonic'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1300']['HHGGTauTau'] = {'mode':'constant','factor':1}

# TPrime M1400
globalXSBRMap['Tprime_M1400'] = od()
globalXSBRMap['Tprime_M1400']['decay'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1400']['TprimeBBM1400'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1400']['TprimeWWM1400'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1400']['TprimeTAUTAUM1400'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1400']['ttHHggbb'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1400']['ttHHggWW'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1400']['ttHHggTauTau'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1400']['ggH'] = {'mode':'ggH'}
globalXSBRMap['Tprime_M1400']['ttH'] = {'mode':'ttH'}
globalXSBRMap['Tprime_M1400']['VBFH'] = {'mode':'qqH'}
globalXSBRMap['Tprime_M1400']['VH'] = {'mode':'VH'}
globalXSBRMap['Tprime_M1400']['HHGGbb'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1400']['HHGGWWdileptonic'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1400']['HHGGWWsemileptonic'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1400']['HHGGTauTau'] = {'mode':'constant','factor':1}

# TPrime M1500
globalXSBRMap['Tprime_M1500'] = od()
globalXSBRMap['Tprime_M1500']['decay'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1500']['TprimeBBM1500'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1500']['TprimeWWM1500'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1500']['TprimeTAUTAUM1500'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1500']['ttHHggbb'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1500']['ttHHggWW'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1500']['ttHHggTauTau'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1500']['ggH'] = {'mode':'ggH'}
globalXSBRMap['Tprime_M1500']['ttH'] = {'mode':'ttH'}
globalXSBRMap['Tprime_M1500']['VBFH'] = {'mode':'qqH'}
globalXSBRMap['Tprime_M1500']['VH'] = {'mode':'VH'}
globalXSBRMap['Tprime_M1500']['HHGGbb'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1500']['HHGGWWdileptonic'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1500']['HHGGWWsemileptonic'] = {'mode':'constant','factor':1}
globalXSBRMap['Tprime_M1500']['HHGGTauTau'] = {'mode':'constant','factor':1}

















































globalXSBRMap['ggtt_nonRes'] = od()
globalXSBRMap['ggtt_nonRes']['decay'] = {'mode':'constant','factor':1}
globalXSBRMap['ggtt_nonRes']['HH2ggtautau'] = {'mode':'constant','factor':1}
globalXSBRMap['ggtt_nonRes']['HHggWW'] = {'mode':'constant','factor':1}
globalXSBRMap['ggtt_nonRes']['ggHH_kl_0_kt_1'] = {'mode':'constant','factor':1}
globalXSBRMap['ggtt_nonRes']['ggHH_kl_1_kt_1'] = {'mode':'constant','factor':1}
globalXSBRMap['ggtt_nonRes']['ggHH_kl_2p45_kt_1'] = {'mode':'constant','factor':1}
globalXSBRMap['ggtt_nonRes']['ggHH_kl_5_kt_1'] = {'mode':'constant','factor':1}
globalXSBRMap['ggtt_nonRes']['qqHH_CV_0p5_C2V_1_kl_1'] = {'mode':'constant','factor':1}
globalXSBRMap['ggtt_nonRes']['qqHH_CV_1p5_C2V_1_kl_1'] = {'mode':'constant','factor':1}
globalXSBRMap['ggtt_nonRes']['qqHH_CV_1_C2V_1_kl_1'] = {'mode':'constant','factor':1}
globalXSBRMap['ggtt_nonRes']['qqHH_CV_1_C2V_0_kl_1'] = {'mode':'constant','factor':1}
globalXSBRMap['ggtt_nonRes']['qqHH_CV_1_C2V_1_kl_0'] = {'mode':'constant','factor':1}
globalXSBRMap['ggtt_nonRes']['qqHH_CV_1_C2V_1_kl_2'] = {'mode':'constant','factor':1}
globalXSBRMap['ggtt_nonRes']['qqHH_CV_1_C2V_2_kl_1'] = {'mode':'constant','factor':1}
# For case of inclusive production mode then have no additional factor beyond V branching ratios
globalXSBRMap['example'] = od()
globalXSBRMap['example']['decay'] = {'mode':'hgg'}
globalXSBRMap['example']['GG2H'] = {'mode':'ggH'}
globalXSBRMap['example']['VBF'] = {'mode':'qqH'}
globalXSBRMap['example']['WH2HQQ'] = {'mode':'WH','factor':BR_W_qq}
globalXSBRMap['example']['ZH2HQQ'] = {'mode':'qqZH','factor':BR_Z_qq}
globalXSBRMap['example']['QQ2HLNU'] = {'mode':'WH','factor':BR_W_lnu}
globalXSBRMap['example']['QQ2HLL'] = {'mode':'qqZH','factor':(BR_Z_ll+BR_Z_nunu)}
globalXSBRMap['example']['GG2HQQ'] = {'mode':'ggZH','factor':BR_Z_qq}
globalXSBRMap['example']['GG2HLL'] = {'mode':'ggZH','factor':BR_Z_ll}
globalXSBRMap['example']['GG2HNUNU'] = {'mode':'ggZH','factor':BR_Z_nunu}
globalXSBRMap['example']['TTH'] = {'mode':'ttH'}
globalXSBRMap['example']['BBH'] = {'mode':'bbH'}
globalXSBRMap['example']['THQ'] = {'mode':'tHq'}
globalXSBRMap['example']['THW'] = {'mode':'tHW'}
# ...

# STXS analysis: add factor for bin composition
globalXSBRMap['STXS'] = od()
globalXSBRMap['STXS']['decay'] = {'mode':'hgg'}
# ggH STXS stage 1.2 bins
globalXSBRMap['STXS']['GG2H_FWDH'] = {'mode':'ggH','factor':0.0809}
globalXSBRMap['STXS']['GG2H_PTH_200_300'] = {'mode':'ggH','factor':0.0098}
globalXSBRMap['STXS']['GG2H_PTH_300_450'] = {'mode':'ggH','factor':0.0025}
globalXSBRMap['STXS']['GG2H_PTH_450_650'] = {'mode':'ggH','factor':0.0003}
globalXSBRMap['STXS']['GG2H_PTH_GT650'] = {'mode':'ggH','factor':0.0001}
globalXSBRMap['STXS']['GG2H_0J_PTH_0_10'] = {'mode':'ggH','factor':0.1387}
globalXSBRMap['STXS']['GG2H_0J_PTH_GT10'] = {'mode':'ggH','factor':0.3940}
globalXSBRMap['STXS']['GG2H_1J_PTH_0_60'] = {'mode':'ggH','factor':0.1477}
globalXSBRMap['STXS']['GG2H_1J_PTH_60_120'] = {'mode':'ggH','factor':0.1023}
globalXSBRMap['STXS']['GG2H_1J_PTH_120_200'] = {'mode':'ggH','factor':0.0182}
globalXSBRMap['STXS']['GG2H_GE2J_MJJ_0_350_PTH_0_60'] = {'mode':'ggH','factor':0.0256}
globalXSBRMap['STXS']['GG2H_GE2J_MJJ_0_350_PTH_60_120'] = {'mode':'ggH','factor':0.0410}
globalXSBRMap['STXS']['GG2H_GE2J_MJJ_0_350_PTH_120_200'] = {'mode':'ggH','factor':0.0188}
globalXSBRMap['STXS']['GG2H_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25'] = {'mode':'ggH','factor':0.0063}
globalXSBRMap['STXS']['GG2H_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25'] = {'mode':'ggH','factor':0.0077}
globalXSBRMap['STXS']['GG2H_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25'] = {'mode':'ggH','factor':0.0028}
globalXSBRMap['STXS']['GG2H_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25'] = {'mode':'ggH','factor':0.0032}
# ggZH hadronic: merged with ggH STXS stage 1.2 bins in fit
globalXSBRMap['STXS']['GG2HQQ_FWDH'] = {'mode':'ggZH','factor':0.0273*BR_Z_qq}
globalXSBRMap['STXS']['GG2HQQ_PTH_200_300'] = {'mode':'ggZH','factor':0.1393*BR_Z_qq}
globalXSBRMap['STXS']['GG2HQQ_PTH_300_450'] = {'mode':'ggZH','factor':0.0386*BR_Z_qq}
globalXSBRMap['STXS']['GG2HQQ_PTH_450_650'] = {'mode':'ggZH','factor':0.0077*BR_Z_qq}
globalXSBRMap['STXS']['GG2HQQ_PTH_GT650'] = {'mode':'ggZH','factor':0.0020*BR_Z_qq}
globalXSBRMap['STXS']['GG2HQQ_0J_PTH_0_10'] = {'mode':'ggZH','factor':0.0001*BR_Z_qq}
globalXSBRMap['STXS']['GG2HQQ_0J_PTH_GT10'] = {'mode':'ggZH','factor':0.0029*BR_Z_qq}
globalXSBRMap['STXS']['GG2HQQ_1J_PTH_0_60'] = {'mode':'ggZH','factor':0.0200*BR_Z_qq}
globalXSBRMap['STXS']['GG2HQQ_1J_PTH_60_120'] = {'mode':'ggZH','factor':0.0534*BR_Z_qq}
globalXSBRMap['STXS']['GG2HQQ_1J_PTH_120_200'] = {'mode':'ggZH','factor':0.0353*BR_Z_qq}
globalXSBRMap['STXS']['GG2HQQ_GE2J_MJJ_0_350_PTH_0_60'] = {'mode':'ggZH','factor':0.0574*BR_Z_qq}
globalXSBRMap['STXS']['GG2HQQ_GE2J_MJJ_0_350_PTH_60_120'] = {'mode':'ggZH','factor':0.1963*BR_Z_qq}
globalXSBRMap['STXS']['GG2HQQ_GE2J_MJJ_0_350_PTH_120_200'] = {'mode':'ggZH','factor':0.2954*BR_Z_qq}
globalXSBRMap['STXS']['GG2HQQ_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25'] = {'mode':'ggZH','factor':0.0114*BR_Z_qq}
globalXSBRMap['STXS']['GG2HQQ_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25'] = {'mode':'ggZH','factor':0.0806*BR_Z_qq}
globalXSBRMap['STXS']['GG2HQQ_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25'] = {'mode':'ggZH','factor':0.0036*BR_Z_qq}
globalXSBRMap['STXS']['GG2HQQ_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25'] = {'mode':'ggZH','factor':0.0285*BR_Z_qq}
# qqH STXS stage 1.2 bins: including (qq)VH hadronic processes
globalXSBRMap['STXS']['VBF_FWDH'] = {'mode':'qqH','factor':0.0669}
globalXSBRMap['STXS']['VBF_0J'] = {'mode':'qqH','factor':0.0695}
globalXSBRMap['STXS']['VBF_1J'] = {'mode':'qqH','factor':0.3283}
globalXSBRMap['STXS']['VBF_GE2J_MJJ_0_60'] = {'mode':'qqH','factor':0.0136}
globalXSBRMap['STXS']['VBF_GE2J_MJJ_60_120'] = {'mode':'qqH','factor':0.0240}
globalXSBRMap['STXS']['VBF_GE2J_MJJ_120_350'] = {'mode':'qqH','factor':0.1234}
globalXSBRMap['STXS']['VBF_GE2J_MJJ_GT350_PTH_GT200'] = {'mode':'qqH','factor':0.0398}
globalXSBRMap['STXS']['VBF_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25'] = {'mode':'qqH','factor':0.1026}
globalXSBRMap['STXS']['VBF_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25'] = {'mode':'qqH','factor':0.0385}
globalXSBRMap['STXS']['VBF_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25'] = {'mode':'qqH','factor':0.1509}
globalXSBRMap['STXS']['VBF_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25'] = {'mode':'qqH','factor':0.0425}
globalXSBRMap['STXS']['WH2HQQ_FWDH'] = {'mode':'WH','factor':0.1257*BR_W_qq}
globalXSBRMap['STXS']['WH2HQQ_0J'] = {'mode':'WH','factor':0.0570*BR_W_qq}
globalXSBRMap['STXS']['WH2HQQ_1J'] = {'mode':'WH','factor':0.3113*BR_W_qq}
globalXSBRMap['STXS']['WH2HQQ_GE2J_MJJ_0_60'] = {'mode':'WH','factor':0.0358*BR_W_qq}
globalXSBRMap['STXS']['WH2HQQ_GE2J_MJJ_60_120'] = {'mode':'WH','factor':0.2943*BR_W_qq}
globalXSBRMap['STXS']['WH2HQQ_GE2J_MJJ_120_350'] = {'mode':'WH','factor':0.1392*BR_W_qq}
globalXSBRMap['STXS']['WH2HQQ_GE2J_MJJ_GT350_PTH_GT200'] = {'mode':'WH','factor':0.0088*BR_W_qq}
globalXSBRMap['STXS']['WH2HQQ_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25'] = {'mode':'WH','factor':0.0044*BR_W_qq}
globalXSBRMap['STXS']['WH2HQQ_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25'] = {'mode':'WH','factor':0.0186*BR_W_qq}
globalXSBRMap['STXS']['WH2HQQ_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25'] = {'mode':'WH','factor':0.0009*BR_W_qq}
globalXSBRMap['STXS']['WH2HQQ_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25'] = {'mode':'WH','factor':0.0040*BR_W_qq}
globalXSBRMap['STXS']['ZH2HQQ_FWDH'] = {'mode':'qqZH','factor':0.1143*BR_Z_qq}
globalXSBRMap['STXS']['ZH2HQQ_0J'] = {'mode':'qqZH','factor':0.0433*BR_Z_qq}
globalXSBRMap['STXS']['ZH2HQQ_1J'] = {'mode':'qqZH','factor':0.2906*BR_Z_qq}
globalXSBRMap['STXS']['ZH2HQQ_GE2J_MJJ_0_60'] = {'mode':'qqZH','factor':0.0316*BR_Z_qq}
globalXSBRMap['STXS']['ZH2HQQ_GE2J_MJJ_60_120'] = {'mode':'qqZH','factor':0.3360*BR_Z_qq}
globalXSBRMap['STXS']['ZH2HQQ_GE2J_MJJ_120_350'] = {'mode':'qqZH','factor':0.1462*BR_Z_qq}
globalXSBRMap['STXS']['ZH2HQQ_GE2J_MJJ_GT350_PTH_GT200'] = {'mode':'qqZH','factor':0.0083*BR_Z_qq}
globalXSBRMap['STXS']['ZH2HQQ_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25'] = {'mode':'qqZH','factor':0.0041*BR_Z_qq}
globalXSBRMap['STXS']['ZH2HQQ_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25'] = {'mode':'qqZH','factor':0.0202*BR_Z_qq}
globalXSBRMap['STXS']['ZH2HQQ_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25'] = {'mode':'qqZH','factor':0.0009*BR_Z_qq}
globalXSBRMap['STXS']['ZH2HQQ_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25'] = {'mode':'qqZH','factor':0.0045*BR_Z_qq}
# WH lep STXS stage 1.2 bins
globalXSBRMap['STXS']['QQ2HLNU_FWDH'] = {'mode':'WH','factor':0.1213*BR_W_lnu}
globalXSBRMap['STXS']['QQ2HLNU_PTV_0_75'] = {'mode':'WH','factor':0.4655*BR_W_lnu}
globalXSBRMap['STXS']['QQ2HLNU_PTV_75_150'] = {'mode':'WH','factor':0.2930*BR_W_lnu}
globalXSBRMap['STXS']['QQ2HLNU_PTV_150_250_0J'] = {'mode':'WH','factor':0.0510*BR_W_lnu}
globalXSBRMap['STXS']['QQ2HLNU_PTV_150_250_GE1J'] = {'mode':'WH','factor':0.0397*BR_W_lnu}
globalXSBRMap['STXS']['QQ2HLNU_PTV_GT250'] = {'mode':'WH','factor':0.0295*BR_W_lnu}
# (qq)ZH lep STXS stage 1.2 bins
globalXSBRMap['STXS']['QQ2HLL_FWDH'] = {'mode':'qqZH','factor':0.1121*(BR_Z_ll+BR_Z_nunu)}
globalXSBRMap['STXS']['QQ2HLL_PTV_0_75'] = {'mode':'qqZH','factor':0.4565*(BR_Z_ll+BR_Z_nunu)}
globalXSBRMap['STXS']['QQ2HLL_PTV_75_150'] = {'mode':'qqZH','factor':0.3070*(BR_Z_ll+BR_Z_nunu)}
globalXSBRMap['STXS']['QQ2HLL_PTV_150_250_0J'] = {'mode':'qqZH','factor':0.0516*(BR_Z_ll+BR_Z_nunu)}
globalXSBRMap['STXS']['QQ2HLL_PTV_150_250_GE1J'] = {'mode':'qqZH','factor':0.0427*(BR_Z_ll+BR_Z_nunu)}
globalXSBRMap['STXS']['QQ2HLL_PTV_GT250'] = {'mode':'qqZH','factor':0.0301*(BR_Z_ll+BR_Z_nunu)}
# gg(ZH) lep STXS stage 1.2 bins: separate processes for ll and nunu decays
globalXSBRMap['STXS']['GG2HLL_FWDH'] = {'mode':'ggZH','factor':0.0270*BR_Z_ll}
globalXSBRMap['STXS']['GG2HLL_PTV_0_75'] = {'mode':'ggZH','factor':0.1605*BR_Z_ll}
globalXSBRMap['STXS']['GG2HLL_PTV_75_150'] = {'mode':'ggZH','factor':0.4325*BR_Z_ll}
globalXSBRMap['STXS']['GG2HLL_PTV_150_250_0J'] = {'mode':'ggZH','factor':0.0913*BR_Z_ll}
globalXSBRMap['STXS']['GG2HLL_PTV_150_250_GE1J'] = {'mode':'ggZH','factor':0.2044*BR_Z_ll}
globalXSBRMap['STXS']['GG2HLL_PTV_GT250'] = {'mode':'ggZH','factor':0.0844*BR_Z_ll}
globalXSBRMap['STXS']['GG2HNUNU_FWDH'] = {'mode':'ggZH','factor':0.0271*BR_Z_nunu}
globalXSBRMap['STXS']['GG2HNUNU_PTV_0_75'] = {'mode':'ggZH','factor':0.1591*BR_Z_nunu}
globalXSBRMap['STXS']['GG2HNUNU_PTV_75_150'] = {'mode':'ggZH','factor':0.4336*BR_Z_nunu}
globalXSBRMap['STXS']['GG2HNUNU_PTV_150_250_0J'] = {'mode':'ggZH','factor':0.0905*BR_Z_nunu}
globalXSBRMap['STXS']['GG2HNUNU_PTV_150_250_GE1J'] = {'mode':'ggZH','factor':0.2051*BR_Z_nunu}
globalXSBRMap['STXS']['GG2HNUNU_PTV_GT250'] = {'mode':'ggZH','factor':0.0845*BR_Z_nunu}
# ttH STXS stage 1.2 bins
globalXSBRMap['STXS']['TTH_FWDH'] = {'mode':'ttH','factor':0.0135}
globalXSBRMap['STXS']['TTH_PTH_0_60'] = {'mode':'ttH','factor':0.2250}
globalXSBRMap['STXS']['TTH_PTH_60_120'] = {'mode':'ttH','factor':0.3473}
globalXSBRMap['STXS']['TTH_PTH_120_200'] = {'mode':'ttH','factor':0.2569}
globalXSBRMap['STXS']['TTH_PTH_200_300'] = {'mode':'ttH','factor':0.1076}
globalXSBRMap['STXS']['TTH_PTH_GT300'] = {'mode':'ttH','factor':0.0533}
# bbH STXS stage 1.2 bins
globalXSBRMap['STXS']['BBH_FWDH'] = {'mode':'bbH','factor':0.0487}
globalXSBRMap['STXS']['BBH'] = {'mode':'bbH','factor':0.9513}
# tH STXS stage 1.2 bins: tHq + tHW
globalXSBRMap['STXS']['THQ_FWDH'] = {'mode':'tHq','factor':0.0279}
globalXSBRMap['STXS']['THQ'] = {'mode':'tHq','factor':0.9721}
globalXSBRMap['STXS']['THW_FWDH'] = {'mode':'tHW','factor':0.0106}
globalXSBRMap['STXS']['THW'] = {'mode':'tHW','factor':0.9894}
