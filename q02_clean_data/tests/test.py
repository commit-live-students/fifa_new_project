
import pandas as pd
from unittest import TestCase
from ..build import q02_clean_data, q01_read_data
from inspect import getfullargspec

path= './data/CompleteDataset.csv'
data = q01_read_data(path)
data=q02_clean_data(data)

class Test_fifa_setup(TestCase):
    def test_fifa_setup_to_df_args(self):
        arg = getfullargspec(q02_clean_data).args
        self.assertEqual(len(arg), 1, "Expected argument(s) %d, Given %d" % (1, len(arg)))

    def test_convert_df_return_instance(self):
        self.assertIsInstance(data, pd.DataFrame,
                              "The Expected return type does not match with the given return type")

    def test_convert_df_return_shape(self):
        self.assertEqual(data.shape, (17981, 12),
                         "The Expected return shape does not match with the given return shape")

    def test_convert_value(self):
        self.assertEqual(data['Value (M)'][1], 105.0,
                         "The Expected return value does not match with the given return value")

    def test_convert_wage(self):
        self.assertEqual(data['Wage (M)'][1], 0.565,
                         "The Expected return value does not match with the given return value")

