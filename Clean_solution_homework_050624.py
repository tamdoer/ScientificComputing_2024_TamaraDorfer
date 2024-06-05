import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from glob import glob
import os

# set paths to input and output directories
path_to_data = Path("~/GIT/ScientificComputing_2024_TamaraDorfer/Data/met_181_1_ctd_rel3")
path_to_data = path_to_data.expanduser()

path_to_plots = Path("~/GIT/ScientificComputing_2024_TamaraDorfer/Plots/Profiles")
path_to_plots = path_to_plots.expanduser()

try:
    os.mkdir(path_to_plots) # only works for running the first time because after that, the directory already exists
except FileExistsError:
    print("Folder already exists!") # you can also say pass if you want nothing to happen
print(str(path_to_data))

# gather file list from directory
file_list = glob(str(path_to_data/"*.ctd")) # use str to define path_to_data as a string
file_list = file_list[:6]
print(file_list)

for filename in file_list:
    list = filename.split("_")
    profile_number = list[-1].replace(".ctd", "")
    file = open(filename, 'r')
    line_counter = 0
    for line in file:
        # print(line.strip())
        line_counter = line_counter + 1
        print(line_counter)
        if line.startswith('Columns  ='):  # two empty here!!!
            print(line)
            header_line_count = line_counter

    print(line_counter, header_line_count)
    file.close()

    print(line_counter)

    df = pd.read_csv(filename, skiprows=header_line_count, sep='\s+')

    # print(df)
    print(df.columns)

    # redefining the column names
    df.columns = ["tim", "lon", "lat", "p", "z", "t", "s", "o", "ss", "sth", "chl2_raw", "turb_raw", "nox", "par",
                  "spar", "chl"]

    print(df.columns)

    variables_list = ["t", "s", "o"]

    for x in variables_list:
        plt.scatter(df['o'], df['z'] * -1)
        plot_name = profile_number + "_depth_vs_" + x + "_v3.pdf"
        plt.savefig(path_to_plots / plot_name)
        plt.close()
#plot runs but overwrites all the plots
# isolate the ctd number from the filename and add it to plot name
#list = filename.split("_")
#profile_number = list[-1].replace(".ctd", "")

