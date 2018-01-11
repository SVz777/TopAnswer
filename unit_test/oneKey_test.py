import unittest

from lib.oneKey import OneKey


class TestOneKey(unittest.TestCase):
    def test_output(self):
        oneKey=OneKey()
        choices=["a","b","c"]
        counts=[1,2,3]
        oneKey.output(choices,counts)

    def test_baiducount(self):
        oneKey=OneKey()
        question='11.斯诺克比赛中在对手不失误的情况下,单杆最高得分是多少'
        choices=["145","146","147"]
        oneKey.search_baiducount(question,choices)

    def test_count(self):
        oneKey=OneKey()
        question='11.斯诺克比赛中在对手不失误的情况下,单杆最高得分是多少'
        choices=["145","146","147"]
        oneKey.search_count(question,choices)