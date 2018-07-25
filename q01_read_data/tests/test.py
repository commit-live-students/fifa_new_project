import pandas as pd
from unittest import TestCase
from ..build import q01_read_data
from inspect import getfullargspec

path = './data/CompleteDataset.csv'
data = q01_read_data(path)


class Test_fifa_setup(TestCase):
    def test_fifa_setup_to_df_args(self):
        arg = getfullargspec(q01_read_data).args
        self.assertEqual(len(arg), 1, "Expected argument(s) %d, Given %d" % (1, len(arg)))

    def test_data_to_df_return_instance(self):
        self.assertIsInstance(data, pd.DataFrame,
                              "The Expected return type does not match with the given return type")

    def test_read_csv_data_to_df_return_shape(self):
        self.assertEqual(data.shape, (17981, 9), "The Expected return shape does not match with the given return shape")