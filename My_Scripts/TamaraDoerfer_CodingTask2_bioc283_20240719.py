## Coding Task 2 19/07/2024

## import relevant packages
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import cartopy

## Define the paths to data and plots
path_to_data = Path("~/GIT/ScientificComputing_2024_TamaraDorfer/Data/AIS_data_2020-03_30W10W_10N30N_combined.txt").expanduser()

path_to_plots = Path("~/GIT/ScientificComputing_2024_TamaraDorfer/Plots/Exam_20240719").expanduser()

## Read in Data
vessel_pos = pd.read_csv(path_to_data, sep="\t") #make sure to read in actual data, not just link to the path_to_data

## Create the Scatterplot
fig = plt.figure(1, figsize=(7, 7))

ax1 = fig.add_axes([0.05, 0.55, 0.8, 0.3], projection=cartopy.crs.PlateCarree())
ax1.set_extent([-30, -10, 10, 30]) #make sure to set correct extent of the map


ax1.add_feature(cartopy.feature.NaturalEarthFeature('physical',
												   'land',
												   '10m',
												   edgecolor='face',
												   facecolor='grey'))

ax1.gridlines(draw_labels=True)


ax1.scatter(x = vessel_pos["cell_ll_lon"], y = vessel_pos["cell_ll_lat"], transform = cartopy.crs.PlateCarree(),
			s=2, color='blue', alpha=0.1)

plot_filename = "vessel_pos_202003.pdf"
path_to_plot_file = path_to_plots / plot_filename

fig.savefig(path_to_plot_file)
