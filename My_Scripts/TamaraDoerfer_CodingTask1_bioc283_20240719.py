## Exam Task 1 19/07/2024

## To Do: aggregate data for the region (30°West to 10°West and 10°North to 30°North) and March 2020 in one file

## Import necessary packages
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from glob import glob
import os
import numpy as np

## Set path to data
path_to_data = Path("~/GIT/ScientificComputing_2024_TamaraDorfer/Data/mmsi-daily-csvs-10-v2-2020.zip")
path_to_data = path_to_data.expanduser()

##
file_list = path_to_data

for file in file_list:
    open(.csv)
    region_1 = glob(str(path_to_data / ()))

## Cannot look at data files in zip folder and therefore don't know the data structure to search for the relevant entries
