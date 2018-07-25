# Default imports

import matplotlib.pyplot as plt
from greyatomlib.fifa_project_new.q02_clean_data.build import q02_clean_data, q01_read_data
import seaborn as sns

path= './data/CompleteDataset.csv'
data = q01_read_data(path)
data = q02_clean_data(data)


