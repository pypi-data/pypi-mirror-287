import unittest
from scrapper_boilerplate import init_crawler


def test_get_request(self):
    soap = init_crawler("https://quotes.toscrape.com/")
    print(soap.text)
    assert not None in soap
