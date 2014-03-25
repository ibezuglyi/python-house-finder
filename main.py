# coding=utf-8

import codecs
import csv
from TablicaCrawler import TablicaCrawler

__author__ = 'dit'

def main():

    crawler = TablicaCrawler("http://tablica.pl/nieruchomosci/mieszkania/sprzedaz/wroclaw/")

    all_offers = crawler.get_all_offers("brbottdashc8", 10)
    myfile = open("d:\houses.csv", 'w')
    for o in all_offers:
        row = '{0}'.format(o.get_str())
        myfile.write(row)
    myfile.close()

if __name__ == "__main__":
    main()