#!/bin/bash

tag=$1
combine_result="combine_results_"$tag".txt"
stats_result="stat_only_"$tag".txt"
full_limits=($(awk '/Expected/ { print $5 }' "$combine_result"))
stat_limits=($(awk '/Expected/ { print $5 }' "$stats_result"))

echo "\\begin{tabular}{|c|c|c|}"
echo "\\hline"
echo "& (stat) & (stat+syst)"
echo "\\hline"
echo "mean & ${stat_limits[i]} & ${expected_limits[i]} \\hline"
echo "\\hline"
echo "\\end{tabular}"

echo "\\begin{table} [htb!]"
echo "        \\centering"
echo "        \\begin{tabular}{ l | c c}"
echo "        \\multicolumn{3}{c}{Upper limits on SM \\ttHH cross-section} \\ \\hline \\hline"
echo "      & $\\sigma_{\\text{UL}}$/$\\sigma_{\\text{SM}}$ \$(\\text{stat})$ &  $\\sigma_{\\text{UL}}gsigma_{\\text{SM}}(\\text{stat+syst})$\\ \\hline"
echo "                mean & ${stat_limits[2]}     &  ${expected_limits[2]}     \\  "
echo "                \\hline"
echo "\\multirow{2}{*}{68\\%}& ${stat_limits[1]}     & ${expected_limits[1]}    \\  "
echo "                     & ${stat_limits[3]}     & ${expected_limits[3]}    \\  "
echo "                     \hline"
echo "\\multirow{2}{*}{95\\%}& ${stat_limits[0]}     & ${expected_limits[0]}       \\"
echo "                     & ${stat_limits[4]}     & ${expected_limits[4]}    \\  "
echo "    \\hline \\hline"
echo "        \\end{tabular}"
echo "    \\caption{Expected signal sensitivity, given in mutiples of the SM cross section}"
echo "    \\label{tab:SMresults}"
echo "\\end{table}"
