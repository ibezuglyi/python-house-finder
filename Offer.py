# coding=utf-8
__author__ = 'dit'


class Offer():
    def __init__(self, offer, details, price, date, href, params):
        self.offer = offer
        self.details = details
        self.price = get_price_from_string(self.safestr(price))
        self.date = date
        self.href = href
        self.square = self.get_square(params)
        #self.street = self.get_street(params)
        self.rooms = self.get_rooms(params)
        self.price_m2 = self.get_price_m2(params)
        self.market = self.get_market(params)
        self.offer_from = self.get_offer_from(params)


    def safestr(self, str):
        if str is None:
            return " "

        return str

    def get_str(self):
        #               self.street + ';' + \
        return '\n' + self.date.strftime("%d.%m.%Y") + ';' + self.price + ';' + unicode(self.offer).encode('utf8') + ';' + unicode(self.square).encode('utf8') + ';' + unicode(self.rooms).encode('utf8') + ';' + unicode(self.price_m2).encode('utf8') + ';' + unicode(self.market).encode('utf8') + ';' + unicode(self.offer_from).encode('utf8')

    def get_square(self, params):
        return read_dict(params, "powierzchnia").replace(" m2", "")

    def get_rooms(self, params):
        return read_dict(params, "liczba pokoi")

    def get_price_m2(self, params):
        val = read_dict(params, "cena za m2")
        if val:
            return get_price_from_string(val)
        return ""

    def get_market(self, params):
        r = read_dict(params, "rynek")
        if r.startswith("wt"):
            return "2"
        return "1"

    def get_offer_from(self, params):
        return read_dict(params, "oferta od")


def read_dict(params, key):
    if key in params:
        return params[key].strip().lower()
    return ""


def get_price_from_string(price):
    return unicode(price.replace(" ", "")).encode('utf8').replace("zł", "")