import unittest

import HtmlTestRunner
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


class test_User(unittest.TestCase) :

    @classmethod
    def setUpClass(self) :
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.get("https://advisortodo.gntkwhqzn-test.advisortodo.com/#/auth/signin")
        self.driver.set_window_size(1366, 741)

    def test_User_List(self) :
        try :
            self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(1) > .form-control").click()
            self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(1) > .form-control").send_keys(
                "Test@qa.com")
            self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(2) > .form-control").click()
            self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(2) > .form-control").send_keys("Test@123#")
            self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
            self.driver.implicitly_wait(10)

            self.driver.find_element(By.ID, "profileDropdown").click()
            self.driver.find_element_by_xpath("//span[contains(text(),'Logout')]").click()
            print("Task Tested successfully")
            self.driver.implicitly_wait(30)

        except TimeoutException as ex :
            print(ex)

    @classmethod
    def tearDownClass(self) :
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__' :
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./Reports', report_title='Advisortodo Report'))
