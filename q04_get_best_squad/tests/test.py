#TEST
import pandas as pd

from unittest import TestCase
from ..build import q04_get_best_squad, q02_clean_data, q01_read_data
from inspect import getfullargspec


path= './data/CompleteDataset.csv'
data = q01_read_data(path)
data= q02_clean_data(data)

squad_433 = ['GK', 'LB', 'CB', 'CB', 'RB', 'LM', 'CDM', 'RM', 'LW', 'ST', 'RW']

squad_352 = ['GK', 'LWB', 'CB', 'RWB', 'LM', 'CDM', 'CAM', 'CM', 'RM', 'LW', 'RW']



Dataframe, List = q04_get_best_squad(data, squad_433, squad_352)


class Test_fifa_setup(TestCase):
    def test_fifa_setup_to_df_args(self):
        arg = getfullargspec(q04_get_best_squad).args
        self.assertEqual(len(arg), 3, "Expected argument(s) %d, Given %d" % (3, len(arg)))

    def test_data_to_df_return_instance(self):
        self.assertIsInstance(Dataframe, pd.DataFrame,
                              "The Expected return type does not match with the given return type")

    def test_read_csv_data_to_df_return_shape(self):
        self.assertEqual(Dataframe.shape, (11, 3),
                         "The Expected return shape does not match with the given return shape")
        
    def test_values_df(self):
        self.assertEqual(Dataframe['Player'][4], 'Carvajal',
                         "You haven't picked the best team. Best RB is Carvajal, you picked ",Dataframe['Player'][4])
   
    def test_values_list(self):
        self.assertEqual(List[4], 'RB',
                         "You haven't picked the best formation. your, your formation doesn't have RB")
         