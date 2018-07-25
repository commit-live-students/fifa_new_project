import pandas as pd
import numpy as np

from greyatomlib.fifa_project_new.q02_clean_data.build import q02_clean_data, q01_read_data

path= './data/CompleteDataset.csv'
data = q01_read_data(path)
data= q02_clean_data(data)

#Squad 4-3-3 Positions
squad_433 = ['GK', 'LB', 'CB', 'CB', 'RB', 'LM', 'CDM', 'RM', 'LW', 'ST', 'RW']


#Squad 5-3-2 Positions
squad_352 = ['GK', 'LWB', 'CB', 'RWB', 'LM', 'CDM', 'CAM', 'CM', 'RM', 'LW', 'RW']


