import sys
import math

step_sf = float(sys.argv[1])
m = sys.argv[2]
masses = sys.argv[3:]

mx = int(m.split("mx")[1].split("my")[0])
my = int(m.split("my")[1])
mys = sorted([int(mass.split("my")[1]) for mass in masses if int(mass.split("mx")[1].split("my")[0]) == mx ])
print(my)
exit()

import numpy as np
assert len(np.unique(mys)) == len(mys)

res = lambda mgg: (mgg/125) * 1.4

i = mys.index(my)

step = int(math.floor(res(my)) * step_sf) 
if step == 0: step = 1
if i == 0:
  my_next = mys[i+1]
  mid_point = (my_next+my)/2

  #print(step, my_next, mid_point)
  to_fit_my = [str(my+step*i) for i in range(int(math.ceil((mid_point-my)/step))+1)]
elif i == len(mys) - 1:
  my_last = mys[i-1]
  mid_point = (my+my_last)/2

  #print(step, my_last, mid_point)
  to_fit_my = [str(my-step*i) for i in range(int(math.ceil((my-mid_point)/step))+1)][::-1]
else:
  my_last = mys[i-1]
  my_next = mys[i+1]
  mid_point_last = (my+my_last)/2
  mid_point_next = (my_next+my)/2

  #print(step, my_last, my_next, mid_point_last, mid_point_next)
  to_fit_my = [str(my-step*i) for i in range(1, int(math.ceil((my-mid_point_last)/step))+1)][::-1]
  to_fit_my += [str(my+step*i) for i in range(int(math.ceil((mid_point_next-my)/step))+1)]

print(" ".join(to_fit_my))
