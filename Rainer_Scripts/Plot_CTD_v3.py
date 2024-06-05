#Script for plotting data from Meteor cruise M158
#want to generate a simple scatter plot depth vs. O2

#1a) deal with path issues using pathlib
#1b) find out how many lines the header contains
#2) load data - to do so we use the pandas module to create a dataframe
#2) plot the variables
#3) visualize and safe the plot


import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

path_to_data = Path("~/GIT/ScientificComputing_2024_TamaraDorfer/Data/met_181_1_ctd_rel3")
path_to_data = path_to_data.expanduser()

path_to_plots = Path("~/GIT/ScientificComputing_2024_TamaraDorfer/Plots")
path_to_plots = path_to_plots.expanduser()

"""
Mac path: /
Windows: \
"""

filename = path_to_data / 'met_181_1_055.ctd'

#####find out how many lines the header has using a for loop

file = open(filename, 'r')

#done_w_header = False
line_counter = 0
#header_line_count = None

for line in file:
	#print(line.strip())
	line_counter = line_counter + 1
	print(line_counter)
	if line.startswith('Columns  ='):  #two empty here!!!
		print(line)
		header_line_count = line_counter


print(line_counter, header_line_count)
file.close()



print(line_counter)


####for loop no longer needed, we now can skip the header lines

df = pd.read_csv(filename, skiprows= header_line_count, sep='\s+')



#print(df)
print(df.columns)

#redefining the column names
df.columns = ["tim","lon","lat","p","z","t","s","o","ss","sth","chl2_raw","turb_raw","nox","par","spar","chl"]

print(df.columns)

#plt.scatter(df['o'], df['z']*-1)

#plt.show()
#plt.savefig(path_to_plots / "Depth_vs_o2_v3.pdf")

# now use a loop to generate plots for Temp, salinity, and oxygen and save them to pdfs

variables_list = ["t", "s", "o"]

for x in variables_list:
	plt.scatter(df['o'], df['z']*-1)
	plot_name = "Depth_vs_" + x + "_w_a_loop_v3.pdf"
	plt.savefig(path_to_plots / plot_name)
	plt.close()







