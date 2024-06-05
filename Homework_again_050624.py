import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import glob
import os


path_to_data = Path("~/GIT/ScientificComputing_2024_TamaraDorfer/Data/met_181_1_ctd_rel3")
path_to_data = path_to_data.expanduser()

path_to_plots = Path("~/GIT/ScientificComputing_2024_TamaraDorfer/Plots")
path_to_plots = path_to_plots.expanduser()

search_dir = path_to_data
os.chdir(search_dir) # chose directory for the following commands
pattern = '*.ctd'
matched_files = glob.glob(pattern)
print(matched_files) #nice it actually printed them!

# now the main loop(s)
for station in matched_files:
    file = open(station, 'r')

    line_counter = 0

    for line in file:
        # print(line.strip())
        line_counter = line_counter + 1
        #print(line_counter)
        if line.startswith('Columns  ='):  # two empty here!!!
            #print(line)
            header_line_count = line_counter

    df = pd.read_csv(station, skiprows=header_line_count, sep='\s+')
    df.columns = ["tim","lon","lat","p","z","t","s","o","ss","sth","chl2_raw","turb_raw","nox","par","spar","chl"]

    for o in station:
        plt.scatter(df['o'], df['z'] * -1)
        plot_name = "Depth_vs_o_" + station + "_v3.pdf"
        plt.savefig(path_to_plots / plot_name)
        plt.close()

print(station)