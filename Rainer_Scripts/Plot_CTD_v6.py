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
from glob import glob
import os


path_to_data = Path("~/GIT/ScientificComputing_2024_TamaraDorfer/Data/") #shortened again
path_to_data = path_to_data.expanduser()

path_to_plots = Path("~/GIT/ScientificComputing_2024_TamaraDorfer/Plots/Profiles")
path_to_plots = path_to_plots.expanduser()

"""
Mac path: /
Windows: \
"""

try:
	os.mkdir(path_to_plots)
except FileExistsError:
	print("Folder exists")



file_list = glob(str(path_to_data / "met*/*.ctd")) #modified to find files from M158 and M181


file_list.sort() #sort works in place

#print(file_list)


test = 1

if test == 1:
	file_list_end = file_list[-4:] #taking also some files from the end for full testing
	file_list = file_list[:4]
	file_list.extend(file_list_end) #extend also works in place
	print(file_list)


for filename in file_list:

	#filename = path_to_data / 'met_181_1_055.ctd'
	#isolate the ctd number from the filename

	list = filename.split("_")
	profile_number =  list[-1]
	profile_number = profile_number.replace(".ctd","")


	#####find out how many lines the header has using a for loop

	file = open(filename, 'r')

	#done_w_header = False
	line_counter = 0
	#header_line_count = None

	for line in file:
		#print(line.strip())
		line_counter = line_counter + 1
		#print(line_counter)
		if line.startswith('Columns  ='):  #two empty here!!!
			print(line)
			header_line_count = line_counter
			header = line #isolating the header line here


	print(line_counter, header_line_count)
	print(header)
	file.close()


	#!!!! Explain the need for header = None

	df = pd.read_csv(filename, skiprows= header_line_count, sep='\s+', header = None)
	print(df.columns)
	print(df[4])


	#print(df)
	#print(df.columns)

	#code to dynamically define the header
	header = header.strip() #getting rid of return at the end of the line
	header = header.replace(" tim", "tim")
	header = header.replace("Columns  =","")
	print(header)
	header = header.split(":")

	print(header)


	#redefining the column names
	df.columns = header

	print(df.columns)

    #defining figure size

	fig = plt.figure(figsize=(3.5, 3.5))
	plt.rcParams.update()
    #generating two axes to plot on
	ax1 = fig.add_axes([0.2, 0.15, 0.35, 0.8], ylim = [-6000, 0], xlim = [0, 35])
	ax2 = fig.add_axes([0.6, 0.15, 0.35, 0.8], ylim = [-6000, 0], xlim = [         ])

	ax1.plot(df['t'], df['z']*-1, color = "lightseagreen") # .scatter generates a scatter plot
	ax1.set_xlabel("Temperature [degC]")
	ax1.set_ylabel("Depth [m]")
	ax2.plot(df['o'], df['z'] * -1, color = "forestgreen") # .plot generates a line plot
	ax2.set_xlabel("Oxygen [µmol/kg]")

	plot_name = filename.split("/")[-1]
	plot_name = plot_name.replace(".ctd","")
	plot_name = plot_name + "_depth_vs_" + "o_and_t" + ".pdf"
	plt.savefig(path_to_plots / plot_name)
	plt.close() #need to close the plot, to avoid all plots accumulating





