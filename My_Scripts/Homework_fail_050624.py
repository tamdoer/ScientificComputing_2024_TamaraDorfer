import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import glob


path_to_data = Path("/Data/met_181_1_ctd_rel3")
path_to_data = path_to_data.expanduser()

path_to_plots = Path("/Plots")
path_to_plots = path_to_plots.expanduser()

#import os
#directory_path = "~/GIT/ScientificComputing_2024_TamaraDorfer/Data/met_181_1_ctd_rel3"

#def list_directory_items(directory_path):
 #   items = os.listdir(directory_path)
#    return items


line_counter = 0
files = ("met_181_1_001.ctd", "met_181_1_002.ctd", "met_181_1_003.ctd", "met_181_1_004.ctd", "met_181_1_005.ctd", "met_181_1_006.ctd", "met_181_1_007.ctd", "met_181_1_008.ctd", "met_181_1_009.ctd", "met_181_1_010.ctd", "met_181_1_011.ctd", "met_181_1_012.ctd")
filename = ("met_181_1_001.ctd", "met_181_1_002.ctd", "met_181_1_003.ctd", "met_181_1_004.ctd", "met_181_1_005.ctd", "met_181_1_006.ctd", "met_181_1_007.ctd", "met_181_1_008.ctd", "met_181_1_009.ctd", "met_181_1_010.ctd", "met_181_1_011.ctd", "met_181_1_012.ctd")
for line in files:
    open(filename, 'r')
    line_counter = line_counter + 1
    if line.startswith('Columns  ='):
        print(line)
        header_line_count = line_counter


for o in files:
    df = pd.read_csv(files, skiprows=header_line_count, sep='\s+')
    plt.scatter(df['o'], df['z'] * -1)
    plot_name = "Depth_vs_o_" + files + "_v3.pdf"
    plt.savefig(path_to_plots / plot_name)
    plt.close()

#items = list_directory_items(directory_path)
#for item in items:
    #print(item)

#for file in directory:




#def list_files_in_directory(met_181_1_ctd_rel3):
 #   files = os.listdir(met_181_1_ctd_rel3)
  #  return files

#for filename in path_to_data:
#    if filename.endswith('.csv'):  # Assuming the files are CSV
#        file_path = os.path.join(directory, filename)

# now use a loop to generate plots for Temp, salinity, and oxygen and save them to pdfs

#variables_list = ["t", "s", "o"]

#for x in variables_list:
#	plt.scatter(df[x], df['z']*-1)
#	plot_name = "Depth_vs_" + x + "_w_a_loop_v3.pdf"
#	plt.savefig(path_to_plots / plot_name)
#	plt.close()

# now make a loop for oxygen plots for at least 10 files


