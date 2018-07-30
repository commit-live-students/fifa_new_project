from unittest import TestCase
from ..build import q05_value_prediction, q01_read_data, q02_clean_data
from inspect import getfullargspec

path= './data/CompleteDataset.csv'
data = q01_read_data(path)
data= q02_clean_data(data)
MAE, RMSE, R2= q05_value_prediction(data)


class Test_fifa_plot(TestCase):
    def test_fifa_setup_to_df_args(self):
        arg = getfullargspec(q05_value_prediction).args
        self.assertEqual(len(arg), 1, "Expected argument(s) %d, Given %d" % (1, len(arg)))

    
    def test_MAE(self):
        self.assertAlmostEqual(MAE, 1.394595127663726,1,
                              "The Expected return value does not match with the given return value")

    def test_RMSE(self):
        self.assertAlmostEqual(RMSE, 2.6582616839240867, 1,
                              "The Expected return value does not match with the given return value")
        
    
    def test_R20(self):
        self.assertAlmostEqual(R2, 0.746327813472971,1,
                              "The Expected return value does not match with the given return value")


    