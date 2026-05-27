# Config file: options for signal fitting

_year = '2022preEE'

signalScriptCfg = {
  
  # Setup
  'inputWSDir':'/home/users/jachisma/CMSSW_14_1_0_pre4/src/workspaces/signal',
  'procs':'xhh_m300', # if auto: inferred automatically from filenames
  'cats':'', # if auto: inferred automatically from (0) workspace
  'ext':'test_sig_m300',
  'analysis':'XHH', # To specify which replacement dataset mapping (defined in ./python/replacementMap.py)
  'year':'combined', # Use 'combined' if merging all years: not recommended
  'massPoints':'125',

  #Photon shape systematics  
  'scales':'Scale', # separate nuisance per year
  'scalesCorr':'', # correlated across years
  'scalesGlobal':'', # affect all processes equally, correlated across years
  'smears':'Smearing', # separate nuisance per year

  # Job submission options
  'batch':'local', # ['condor','SGE','IC','local']
  'queue':'espresso',

}
