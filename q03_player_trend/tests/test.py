
from unittest import TestCase
from ..build import q03_player_trend, q02_clean_data, q01_read_data
from inspect import getfullargspec

path= 'data/CompleteDataset.csv'
data = q01_read_data(path)
data = q02_clean_data(data)


q03_player_trend(data)

class Test_fifa_plot(TestCase):
    def test_fifa_setup_to_df_args(self):
        arg = getfullargspec(q03_player_trend).args
        self.assertEqual(len(arg), 1, "Expected argument(s) %d, Given %d" % (1, len(arg)))# -*- coding: utf-8 -*-

