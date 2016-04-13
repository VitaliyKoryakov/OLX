import unittest
from config.driver import Driver


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = Driver.get()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()