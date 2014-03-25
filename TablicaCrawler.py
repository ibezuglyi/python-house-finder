import urllib2
from bs4 import BeautifulSoup
from HouseConverter import HouseConverter
from Offer import Offer
from Page import Page
from TimeConverter import TimeConverter

__author__ = 'dit'


class TablicaCrawler():
    def init_crawler(self, src):
        if src is not None:
            self.source = src
        self.data = None


    def __init__(self, src=None):
        self.init_crawler(src)
        self.time_converter = TimeConverter()
        self.houseConverter = HouseConverter()


    def getRawData(self):
        if not self.data:
            data = get_html(self.source)
            self.data = data

        return self.data

    def get_raw_offers(self, css_class):
        data = self.getRawData()
        soup = BeautifulSoup(data)
        self.raw_offers = soup.find_all("td", {'class': css_class})
        return self.raw_offers

    def get_offers(self, css_class):
        raw_offers = self.get_raw_offers(css_class)
        offers = [_as_offer(raw_offer, self.time_converter, self.houseConverter) for raw_offer in raw_offers]
        return offers

    def get_pages_count(self):
        pages = self.get_pages()
        return len(pages)

    def get_pages(self):
        page_data = self.getRawData()
        soup = BeautifulSoup(page_data)
        pager = soup.find_all("div", {'class': 'pager'})[0]
        pages = [_as_page(p) for p in pager.find_all("span", {'class': 'item'})]
        return pages

    def generate_page_href(self, page, page_number):
        pattern = page.href
        href = pattern.replace("3", page_number)
        return href

    def get_page(self, page_number):
        pages = self.get_pages()
        page = [p for p in pages if p.number == page_number]
        if page:
            href = page[0].href
        else:
            href = self.generate_page_href(pages[2], str(page_number))

        href = href is None and self.source or href

        self.init_crawler(href)
        print "parsing %s" % href
        return self

    def get_all_offers(self, css_class, upper_range=None):
        pages = self.get_pages()
        all_offers = []
        if upper_range is None:
            up_border = pages[-1].number
        else:
            up_border = upper_range

        for p in range(1, up_border):
            o = self.get_page(p).get_offers(css_class)
            all_offers.extend(o)

        return all_offers


def _as_page(raw_page):
    number = raw_page.span.contents[0]
    if raw_page.span.span:
        number = raw_page.span.span.string
    href = None
    atags = raw_page.find_all('a')
    if atags:
        href = atags[0]['href']

    return Page(number, href)


def get_html(src):
    req = urllib2.Request(src)
    res = urllib2.urlopen(req)
    data = res.read()
    return data


def _as_offer(raw_offer, time_converter, houseConverter):
    tds = raw_offer.find_all("td")
    if tds[0].p.br:
        tds[0].p.br.extract()
    date = " ".join([t.string.strip() for t in tds[0].p])
    offer = tds[2].div.h3.a.span.contents[0]
    href = tds[2].div.h3.a['href']
    details = tds[2].div.p.small.contents[2]
    price = tds[3].div.p.strong.string.strip()
    raw_house = get_html(href)
    params = houseConverter.get_house_details(raw_house)

    return Offer(offer, details, price, time_converter.get_date(date), href, params)


