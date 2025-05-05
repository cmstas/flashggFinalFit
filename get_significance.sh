#!/usr/bin/env bash

set -e

mh=125

mggl=$1
mggh=$2
mx=$3
my=$4
mh=$5
procTemplate=$6

m="mx${mx}my${my}"
mo="mx${mx}my${my}mh${mh}"

pushd Combine  
# Asymptotic limits
  echo "calculate significance"
#  combine -M Significance Datacard_ggbbres_mx${mx}my${my}.txt --freezeParameters MH,MX,MY --setParameters MX=${mx},MY=${my} -m ${my}  > significance_mx${mx}my${my}.txt
  combine --redefineSignalPOI r --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 -M Significance Datacard_ggbbres_mx${mx}my${my}_ggbbres.root --freezeParameters MH,MX,MY --setParameters MX=${mx},MY=${my} -m ${my} --rMin -1 --uncapped 1 > significance_mx${mx}my${my}.txt
popd
