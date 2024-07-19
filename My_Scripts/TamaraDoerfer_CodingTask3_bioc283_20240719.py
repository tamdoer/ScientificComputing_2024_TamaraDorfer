## Coding Task 3 19/07/2024

## import relevant packages
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO
from pathlib import Path
import cartopy

## Define the paths to data and plots
path_to_data = Path("~/GIT/ScientificComputing_2024_TamaraDorfer/Data/AIS_data_2020-03_30W10W_10N30N_combined.txt").expanduser()

path_to_plots = Path("~/GIT/ScientificComputing_2024_TamaraDorfer/Plots/Exam_20240719").expanduser()

## Read in Data
vessel_pos = pd.read_csv(path_to_data, sep="\t") #make sure to read in actual data, not just link to the path_to_data

## Assemble the Data
# extract / calculate the average fishing hours per day
avg_fish_hours = vessel_pos.groupby(['cell_ll_lat', 'cell_ll_lon'])['fishing_hours'].mean().reset_index()
print(avg_fish_hours)

## Create the Scatterplot
fig = plt.figure(1, figsize=(7, 7))

ax1 = fig.add_axes([0.05, 0.05, 0.8, 0.9], projection=cartopy.crs.PlateCarree())
ax1.set_extent([-20, -15, 15, 20]) #make sure to set correct extent of the map


ax1.add_feature(cartopy.feature.NaturalEarthFeature('physical',
												   'land',
												   '10m',
												   edgecolor='face',
												   facecolor='grey'))

ax1.gridlines(draw_labels=True)


plt.scatter(x=avg_fish_hours["cell_ll_lon"], y = avg_fish_hours["cell_ll_lat"], transform = cartopy.crs.PlateCarree(),
            c=avg_fish_hours["fishing_hours"], cmap="viridis", alpha=0.8)

# now need to include a colour bar, title, but didn't manage that

plot_filename = "avg_fishing_hours_202003.pdf"
path_to_plot_file = path_to_plots / plot_filename

fig.savefig(path_to_plot_file)


