#Script for plotting data from Meteor cruise M158
#want to generate a simple scatter plot depth vs. O2

#1) load data - to do so we use the pandas module to create a dataframe
#2) plot the variables
#3) visualize and safe the plot


import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('../Data/met_181_1_055_test.ctd', sep=',')

#print(df)
print(df.columns)

print(df['o'])

plt.scatter(df['o'], df['z']*-1)

#plt.show()
plt.savefig("../Plots/Depth_vs_o2_v2.pdf")