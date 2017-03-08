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

        driver = self.driver
        #driver.maximize_window()
        driver.get('https://thameslink.stage.otrl.io/search')

        # <Step 1: Click on Season tickets tab.>
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/div[2]/nav/a[2]").click()
        time.sleep(2)
        # <Result 1: Season tickets tab opened.>

        # <Step 2: Enter 'West Hampstead' in Leaving From box.>
        driver.find_element_by_xpath(locators['entry_for_start_location']).send_keys("West Hampstead")
        time.sleep(2)
        # <Result 2: 'West Hampstead' is seen in the Leaving From box.>

        # <Step 3: In Tickets tab, Going To box, enter 'East Croydon'.>
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/section[1]/div/ul/li[3]/label/div/input").send_keys("East Croy")
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/section[1]/div/ul/li[3]/label/div/div/div").click()
        time.sleep(2)
        # <Result 3: 'East Croydon' is seen in the Going To box.>

        # <Step 4: In Tickets tab, click on the Outbound Calendar.>
        driver.find_element_by_xpath("//*[@id='loadDateSelect']").click()
        time.sleep(5)
        # <Result 4: 'The Outbound Calendar is opened.>

        # <Step 5: Click on date March 15 2017 in the Calendar.>
        driver.find_element_by_xpath("//*[@id='rw_3_calendar__month_2-15']/span").click()
        time.sleep(5)
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div[3]/div/button[2]").click()
        # <Result 5: 'March 15 2017 is selected as the Outbound travel date.>

        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/section[3]/div[2]/div/div/div[1]/div/div/label/span").click()
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/section[3]/div[2]/div/div/div[2]/div/div/label/span").click()






        # <Step 6: Click on the 'Passengers and Railcards button'.>
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/section[3]/button").click()
        time.sleep(5)
        # <Result 6: The 'Passengers and Railcards' dialog is opened.>

        # <Step 7: In 'Passengers and Railcards' dialog, click 'Select' button.>
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div[3]/div/button[2]").click()
        time.sleep(10)
        # <Result 7: The default of '1 Adult - No railcards added' is saved and the dialog is closed.>

        # <Step 7: Click on the 'Find trains' button.>
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/footer/button").click()
        time.sleep(10)
        # <Result 7: The 'Choose an outbound service' list of trains is displayed.>

        # <Step 8: Click on the second train service down from the top.>
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/div/div[1]/ul/li[3]/div/div[1]/div[2]/div/button").click()
        time.sleep(5)
        # <Result 8: The list of available tickets for the second train service down from the top is opened.>

        # <Step 9: Click on the 'Carnet Peak 5' ticket in the list.>
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div[2]/div[2]/div/ul/li[3]/label/div[2]/div").click()
        time.sleep(5)
        # <Result 9: The 'Carnet Peak 5' ticket is shown as selected.>

        # <Step 10: Click on the 'Continue' button.>
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div[3]/div/button[2]").click()
        time.sleep(5)
        # <Result 10: The 'Would you like any extras?' page is displayed.>

        # <Step 11: Click on the 'Continue' button.>
        driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[3]/div[2]/button[2]").click()
        time.sleep(5)
        # <Result 11: The journey is added to the basket and the 'Order summary' is displayed.>

        # <Step 12: Click on '1st Class Mail' in 'Collection preferences'.>
        #driver.find_element_by_xpath("//*[@id='container']/div/div/section/div/div[1]/section/div[2]/div").click()
        #time.sleep(5)
        # <Result 12: '1st Class Mail' option is selected in the list of collection preferences.>

        # <Step 13: Enter 'Miss Michelle Gust' in the 'First name' field.>
        driver.find_element_by_xpath("//*[@id='contactName']").send_keys("Miss Michelle Gust")
        time.sleep(5)
        # <Result 13: 'Miss Michelle Gust' is seen in the 'First name' field.>

        # <Step 14: Enter '30 Great Guildford Street' in the 'Address line 1' field.>
        driver.find_element_by_xpath("//*[@id='addressline1']").send_keys("30 Great Guildford Street")
        time.sleep(5)
        # <Result 14: '30 Great Guildford Street' is seen in the 'Address line 1' field.>

        # <Step 15: Enter 'London' in the 'Town/City' field.>
        driver.find_element_by_xpath("//*[@id='towncity']").send_keys("London")
        time.sleep(5)
        # <Result 15: 'London' is seen in the 'Town/City' field.>

        # <Step 16: Enter 'London' in the 'Postcode' field.>
        driver.find_element_by_xpath("//*[@id='postcode']").send_keys("SE1 0HS")
        time.sleep(5)
        # <Result 16: 'London' is seen in the 'Postcode' field.>


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()