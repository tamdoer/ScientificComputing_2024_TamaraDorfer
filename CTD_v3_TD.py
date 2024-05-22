#Script for plotting data from Meteor cruise M158
#want to generate a simple scatter plot depth vs. O2
#in v3 we use actual data

#1) deal with path issues using pathlib
#2) load data - to do so we use the pandas module to create a dataframe
#2) plot the variables
#3) visualize and safe the plot


import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

#to get a file, access it from ScientificComputing_2024
#when Rainer updates something we have to PULL first!
path_to_data = Path("~/GIT/ScientificComputing_2024/Data")
path_to_data = path_to_data.expanduser()

path_to_plots = Path("~/GIT/ScientificComputing_2024/Plots")
path_to_plots = path_to_plots.expanduser()

"""
Mac path: /
Windows: \
"""

filename = path_to_data / 'met_181_1_055.ctd'

#find out how many lines the header has

file = open(filename, 'r')

for line in file:
    print(line)

quit()


df = pd.read_csv(path_to_data / 'met_181_1_055.ctd', sep=',')

#print(df)
print(df.columns)

plt.scatter(df['o'], df['z']*-1)

#plt.show()
plt.savefig(path_to_plots / "Depth_vs_o2_v2.pdf")