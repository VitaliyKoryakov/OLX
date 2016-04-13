#-*- coding: utf-8 -*-

import config.olx_config as CONST
from tests.base_test import BaseTest
from pages.olx_page import OlxPage


class TestOLX(BaseTest):
    def test_crocodile(self):
        olx_page = OlxPage()
        olx_page.choose_category(CONST.categoty_zhivotnye)
        olx_page.choose_category(CONST.categoty_drugie_zhivotnye)
        olx_page.search(u'крокодил')
        self.assertTrue(olx_page.offers_presence(), 'offers dont exists')
