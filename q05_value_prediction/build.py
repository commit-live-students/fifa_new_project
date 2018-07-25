
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error, r2_score
from math import sqrt
from sklearn.model_selection import train_test_split
from greyatomlib.fifa_project_new.q02_clean_data.build import q02_clean_data, q01_read_data

path= './data/CompleteDataset.csv'
data = q01_read_data(path)
data= q02_clean_data(data)


def q05_value_prediction(data):
    "write your solution here"
  



