import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

locators = {
    'entry_for_start_location': "//*[@id='container']/div/div/section/div/div[1]/section[1]/div/ul/li[1]/label/div/input"
}

class regressionclass(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_thameslink_buy_ticket(self):





    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()