# Config file: options for signal fitting

_year = '2018'

signalScriptCfg = {
  
  # Setup
  'inputWSDir':'/home/hep/mdk16/PhD/ggtt/CMSSW_10_2_0/src/HHToGGTT/output_trees/ws/signal_%s'%_year,
  'procs':'auto', # if auto: inferred automatically from filenames
  'cats':'auto', # if auto: inferred automatically from (0) workspace
  'ext':'test_%s'%_year,
  'analysis':'ggtt_resonant', # To specify which replacement dataset mapping (defined in ./python/replacementMap.py)
  'year':'%s'%_year, # Use 'combined' if merging all years: not recommended
  'massPoints':'125',

  #Photon shape systematics  
  'scales':'',
  'scalesCorr':'',
  'scalesGlobal':'',
  'smears':'',

  # Job submission options
  'batch':'local', # ['condor','SGE','IC','local']
  'queue':'hep.q'
  #'batch':'condor', # ['condor','SGE','IC','local']
  #'queue':'espresso',

}
