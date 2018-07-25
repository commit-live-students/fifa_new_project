from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error, r2_score
from math import sqrt
from sklearn.model_selection import train_test_split
from greyatomlib.fifa_project_new.q02_clean_data.build import q02_clean_data, q01_read_data
from sklearn.preprocessing import PolynomialFeatures
import pandas as pd

path= './data/CompleteDataset.csv'
data = q01_read_data(path)
data= q02_clean_data(data)






















""" BONUS Question """

#The new player details
Data={'Name':'Alex Rodriguez', 'Age':23, 'Overall':89, 'Potential':92,'Club':'Manchester United','Preferred Positions':'ST CAM', 'Wage (M)':0.215}
New_Player=pd.DataFrame(Data, index=[0])

""" Use your model to predict the player's Value """    
#73    