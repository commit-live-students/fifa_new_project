from unittest import TestCase
from ..build import q06_model_improvement, q01_read_data, q02_clean_data
from inspect import getfullargspec

path= './data/CompleteDataset.csv'
data = q01_read_data(path)
data= q02_clean_data(data)
MAE, RMSE, R2= q06_model_improvement(data)


class Test_fifa_plot(TestCase):
    def test_fifa_setup_to_df_args(self):
        arg = getfullargspec(q06_model_improvement).args
        self.assertEqual(len(arg), 1, "Expected argument(s) %d, Given %d" % (1, len(arg)))

    
    def test_MAE(self):
        self.assertAlmostEqual(MAE,0.5326507223889104 ,1,
                              "The Expected return value does not match with the given return value")

    def test_RMSE(self):
        self.assertAlmostEqual(RMSE, 1.3885943075947467, 1,
                              "The Expected return value does not match with the given return value")
        
    
    def test_R20(self):
        self.assertAlmostEqual(R2,0.9307805489704964,1,
                              "The Expected return value does not match with the given return value")


    