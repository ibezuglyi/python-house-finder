# coding=utf-8
import time

__author__ = 'dit'
import re
from bs4 import BeautifulSoup


class HouseConverter():
    def get_house_details(self, house_html):
        start = time.time()
        params = dict()
        bs = BeautifulSoup(house_html)
        trs = bs.find_all("tr", {"class": "brbottdashc8"})
        tdsSet = map((lambda tr: tr.find_all("td")), trs)
        rows = map((lambda tdset: tdset[0:3]), tdsSet)
        for row in rows:
            for td in row:
                if td.div:
                    keys = td.div.text.split(":")
                    params[keys[0].strip().lower()] = keys[1]
                else:
                    print td
        print time.time() - start
        return params






