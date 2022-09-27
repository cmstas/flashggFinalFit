
mgg_res = 90
mgg_low = 65.
mgg_high =120.
mgg_veto_low =  mgg_res - 10
mgg_veto_high = mgg_res + 10

fit_window	= 5
MHLow 	=  	str(mgg_res - fit_window)
MHHigh 	= 	str(mgg_res + fit_window)
MHNominal	= str(mgg_res)
