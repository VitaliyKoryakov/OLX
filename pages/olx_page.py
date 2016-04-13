#-*- coding: utf-8 -*-

from base_page import BasePage
from config import olx_config as CONST
from selenium.common.exceptions import NoSuchElementException


class OlxPage(BasePage):
    def __init__(self):
        super(OlxPage, self).__init__(CONST.olx_url)

    def choose_category(self, category):
        self.driver.find_element_by_xpath(category).click()

    def search(self, search_text):
        search_field = self.driver.find_element_by_id(CONST.search_field_id)
        search_field.send_keys(search_text)
        self.driver.find_element_by_id(CONST.search_submit_id).click()

    def offers_presence(self):

        import time
        time.sleep(2)
        try:
            self.driver.find_element_by_class_name(CONST.search_result_class_name)
            return True
        except NoSuchElementException:
            return False
