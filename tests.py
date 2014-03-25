# coding=utf-8

import unittest
from HouseConverter import HouseConverter
from TablicaCrawler import TablicaCrawler
from TimeConverter import TimeConverter

__author__ = 'dit'

import unittest2


class TestClass(unittest2.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.crawler = TablicaCrawler("http://tablica.pl/nieruchomosci/mieszkania/sprzedaz/wroclaw/")
        cls.css_class = "brbottdashc8"

    def test_can_run_crawler(self):
        data = self.crawler.getRawData
        self.assertIsNotNone(data)

    def test_can_reach_offers(self):
        offers = self.crawler.get_raw_offers(self.css_class)
        self.assertGreater(len(offers), 0)

    def test_can_get_offers(self):
        offers = self.crawler.get_offers(self.css_class)
        self.assertIsNotNone(offers[0].offer)

    def test_can_get_offers_with_href(self):
        offers = self.crawler.get_offers(self.css_class)
        print offers[0].href
        self.assertIsNotNone(offers[0].href)

    def test_can_count_pages_number(self):
        pages_count = self.crawler.get_pages_count()
        self.assertGreater(pages_count, 10)

    def test_can_get_last_page_number_and_href(self):
        pages = self.crawler.get_pages()
        self.assertAlmostEqual(pages[-1].number, 123, delta=10)
        self.assertIsNotNone(pages[-1].href)

    def test_can_get_second_page_offers(self):
        offers = self.crawler.get_page(2).get_offers(self.css_class)
        self.assertGreater(len(offers), 0)

    def test_can_get_hundreth_page_offers(self):
        offers = self.crawler.get_page(100).get_offers(self.css_class)
        print offers
        self.assertGreater(len(offers), 0)

    @unittest2.skip("skipped")
    def test_can_get_pages_offers(self):
        all_offers = self.crawler.get_all_offers(self.css_class)
        self.assertGreater(len(all_offers), 1000)


    def test_can_convert_date(self):
        date = "3 mar"
        converter = TimeConverter()
        cdate = converter.get_date(date)
        self.assertIsNotNone(cdate)

    def test_can_convert_date2(self):
        date = "dzisiaj 21.54"
        converter = TimeConverter()
        cdate = converter.get_date(date)
        self.assertIsNotNone(cdate)


    def test_can_fetch_rooms_count(self):
        offers = self.crawler.get_page(2).get_offers(self.css_class)
        offer = offers[0]
        self.assertIsNotNone(offer.rooms)


    def test_can_fetch_square(self):
        offers = self.crawler.get_page(2).get_offers(self.css_class)
        offer = offers[0]
        self.assertIsNotNone(offer.square)

    def test_can_fetch_street(self):
        offers = self.crawler.get_page(2).get_offers(self.css_class)
        offer = offers[0]
        self.assertIsNotNone(offer.street)

if __name__ == "__main__":
    unittest2.main()




