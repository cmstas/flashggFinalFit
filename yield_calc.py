import pandas as pd

input_dir = 'Datacard/yields_SM_23Sep22_fixed_lf_and_hf/'
#input_dir = 'Datacard/yields_SM_23Sep22_with_HHGGXX/'

df1 = pd.read_pickle(input_dir+'SR2.pkl')
df2 = pd.read_pickle(input_dir+'SR2.pkl')

SM = ['ttHHggbb_', 'ttHHggWW_', 'ttHHggTauTau_']
TwoHDM= ['2HDMbbM300_', '2HDMWWM300_', '2HDMTAUTAUM300_']
backgrounds = ['VBFH_', 'VH_', 'ggH_', 'ttH_', 'HHGGbb_', 'HHGGWWsemileptonic_', 'HHGGWWdileptonic_', 'HHGGTauTau_']
signals = SM
if 'ttHHggbb_' not in signals:
    backgrounds += SM
procs = signals+backgrounds+['bkg_mass','data_obs']
years = ['2016', '2017', '2018']

unyieldy1 = pd.Series(df1.nominal_yield.values, index=df1.proc).to_dict()
unyieldy2 = pd.Series(df2.nominal_yield.values, index=df2.proc).to_dict()

yields1 = {}
yields2 = {}
total = {}
for proc in procs:
    if proc not in yields1:
        yields1[proc] = 0
        yields2[proc] = 0
        total[proc] = 0

for proc in yields1:
    for year in years:
        tmp = proc+year+'_hgg'
        if tmp not in unyieldy1:
            continue
        yields1[proc] += unyieldy1[tmp]

for proc in yields2:
    for year in years:
        tmp = proc+year+'_hgg'
        if tmp not in unyieldy2:
            continue
        yields2[proc] += unyieldy2[tmp]

for proc in total:
    total[proc]=yields1[proc]+yields2[proc]

sig_tot_SR1 = 0
sig_tot_SR2 = 0
sig_tot_TOT = 0
bkg_tot_SR1 = 0
bkg_tot_SR2 = 0
bkg_tot_TOT = 0

for proc in yields1:
    if proc in signals:
        sig_tot_SR1 += yields1[proc]
        sig_tot_SR2 += yields2[proc]
        sig_tot_TOT += yields1[proc]+yields2[proc]
    else:
        bkg_tot_SR1 += yields1[proc]
        bkg_tot_SR2 += yields2[proc]
        bkg_tot_TOT += yields1[proc]+yields2[proc]

table = ''
table += '\\begin{center}\n'
table += '\\begin{tabular}{c|c|c||c|}\n'
table += 'Process & SR1 & SR2 & Tot \\\\\\hline\n'
for proc in signals:
    table += proc[:-1]+' & {:.4f} & {:.4f} & {:.4f} \\\\\\hline\n'.format(yields1[proc], yields2[proc], (yields1[proc]+yields2[proc]))
#table += 'Signal Tot & {:.4f} & {:.4f} & {:.4f} \\\\\\hline\\hline\n'.format(sig_tot_SR1, sig_tot_SR2, sig_tot_TOT)

for proc in backgrounds:
    table += proc[:-1]+' & {:.4f} & {:.4f} & {:.4f} \\\\\\hline\n'.format(yields1[proc], yields2[proc], (yields1[proc]+yields2[proc]))
#table += 'Bkg Tot & {:.4f} & {:.4f} & {:.4f} \\\\\\hline\n'.format(bkg_tot_SR1, bkg_tot_SR2, bkg_tot_TOT)
    table += 'bkg_mass & {:.4f} & {:.4f} & {:.4f} \\\\\\hline\n'.format(yields1['bkg_mass'], yields2['bkg_mass'], (yields1['bkg_mass']+yields2['bkg_mass']))
table += '\\end{tabular}\n'
table += '\\end{center}\n'
print(table)
