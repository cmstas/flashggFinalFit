import os
import sys

root_files = os.listdir(sys.argv[1])

masses = []
for f in root_files:
  #masses.append(f.split("cat")[0].split("m")[-1])
  masses.append("mx" + f.split("cat")[0].split("mx")[-1])
masses = sorted(set(masses))
#masses = ["mx300my90", "mx400my90", "mx500my90", "mx600my90", "mx700my90", "mx800my90", "mx900my90", "mx1000my90"]
masses = ["mx600my90"]

for m in masses:
  print(m)
