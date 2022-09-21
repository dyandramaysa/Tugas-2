from django.test import TestCase
from django.urls import reverse, resolve
from mywatchlist.views import show_watchlist, show_xml, show_json, show_html

class TestUrls(TestCase):
    def test_show_watchlist(self):
        url = reverse('mywatchlist:show_watchlist')
        self.assertEquals(resolve(url).func, show_watchlist)

    def test_show_xml(self):
        url = reverse('mywatchlist:show_xml')
        self.assertEquals(resolve(url).func, show_xml)

    def test_show_json(self):
        url = reverse('mywatchlist:show_json')
        self.assertEquals(resolve(url).func, show_json)

    def test_show_html(self):
        url = reverse('mywatchlist:show_html')
        self.assertEquals(resolve(url).func, show_html)