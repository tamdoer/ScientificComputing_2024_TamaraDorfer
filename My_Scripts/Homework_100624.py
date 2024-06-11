#Homework for the 11th of June;

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import glob
import os


path_to_data = Path("~/GIT/ScientificComputing_2024_TamaraDorfer/Data/UVP_data_M158_M181_processed_m.tsv")
path_to_data = path_to_data.expanduser()

path_to_plots = Path("~/GIT/ScientificComputing_2024_TamaraDorfer/Plots")
path_to_plots = path_to_plots.expanduser()

filename = path_to_data
file = open(filename, 'r')

done_w_header = False
line_counter = 0
header_line_counter = None

# reopen the file object before each loop
for line in file:
    #print(line)
    line_counter = line_counter + 1
    print(line_counter) #print is basically just to check what the status of a project is!
    if line.startswith('Columns  ='):
        print(line)
        header_line_counter = line_counter
print(line_counter, header_line_counter)

df = pd.read_csv(filename, skiprows= header_line_counter, delimiter='\t')
#df.columns = ["Profile","Rawfilename","Date_Time","Project","Pressure [dbar]","Vol [L] (sampled for this depth bin)","Latitude","Longitude","Flux_mgC_m2_d","Part conc frac [#/l] (ESD: 0.1 to 0.512 mm)","Part conc frac [#/l] (ESD: 0.512 to 16.4 mm)"]
#df.columns unnecessary because column names are right above the data

profile_list = df['Profile'].unique() # need this so we have an iterable item

for profile in profile_list:
    profile_data = df[df['Profile'] == profile]
    #print(profile_data)
    plt.scatter(df['Pressure [dbar]'], df['Flux_mgC_m2_d'] * -1)
    plot_name = "Pressure_vs_Flux" + profile + ".pdf"
    plt.savefig(path_to_plots / plot_name)
    plt.close()