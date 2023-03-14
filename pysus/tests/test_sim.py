# -*- coding:utf-8 -*-
u"""
Created on 23/09/2020
by gabrielmcf
license: GPL V3 or Later
"""

import unittest

from numpy.testing import (
    assert_array_almost_equal,
    assert_array_equal,
    assert_equal,
)

from pysus.online_data.SIM import download
from pysus.preprocessing import SIM, decoders
from pysus.online_data import parquets_to_dataframe as to_df


class TestDecoder(unittest.TestCase):
    def test_group_and_count(self):
        df = to_df(download("se", 2010)[0])
        df = decoders.translate_variables_SIM(df)
        variables = ["CODMUNRES", "SEXO", "IDADE_ANOS"]
        counts = SIM.group_and_count(df, variables)
        self.assertGreater(counts.COUNTS.sum(), 0)

    def test_redistribute_missing(self):
        df = to_df(download("se", 2010)[0])
        df = decoders.translate_variables_SIM(df)
        variables = ["CODMUNRES", "SEXO", "IDADE_ANOS"]
        counts = SIM.group_and_count(df, variables)
        sum_original = counts["COUNTS"].sum()
        counts = SIM.redistribute_missing(counts, variables)
        sum_redistributed = counts["COUNTS"].sum()

        self.assertEqual(sum_original, sum_redistributed)



    def test_redistribute_missing_partial(self):
        df = to_df(download("se", 2010)[0])
        df = decoders.translate_variables_SIM(
            df, age_classes=True, classify_cid10_chapters=True
        )
        group_variables = ["CODMUNRES", "SEXO", "IDADE_ANOS", "CID10_CHAPTER"]
        counts = SIM.group_and_count(df, group_variables)
        counts["COUNTS_ORIGINAL"] = counts["COUNTS"]
        sum_original = counts["COUNTS"].sum()
        counts = SIM.redistribute_missing(counts, group_variables[:3])
        sum_redistributed = counts["COUNTS"].sum()

        assert_equal(sum_original, round(sum_redistributed))
        # sample = counts[counts['COUNTS'] != 0]['COUNTS'].sample(20,random_state=0).tolist()
        # assert_array_almost_equal(sample, [1.0026605509150972, 3.0076529330337682, 10.0, 3.0, 1.0, 7.030611240693058, 2.0, 1.0, 1.0003988761766138, 1.0, 5.0, 1.0, 2.0, 1.0, 1.0011890475332716, 1.0007766913402458, 3.0, 3.0, 1.0, 1.0], decimal=5)
