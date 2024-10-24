# Config file: options for signal fitting

_tag="dummy"
_my="my_mass"
_mx="mx_mass"

backgroundScriptCfg = {
  
  # Setup
  'inputWSDir':'/home/users/fsetti/flashggFinalFit_resonant/CMSSW_10_2_13/src/flashggFinalFit/files/%s/Data/ws/'%(_tag), # location of 'allData.root' file
  'cats':'auto', # auto: automatically inferred from input ws
  'catOffset':0, # add offset to category numbers (useful for categories from different allData.root files)  
  'ext':'%s_MX%s_MY%s'%(_tag,_mx,_my), # extension to add to output directory
  'year':'combined', # Use combined when merging all years in category (for plots)

  # Job submission options
  'batch':'local', # [condor,SGE,IC,local]
  'queue':'hep.q' # for condor e.g. microcentury
  
}
