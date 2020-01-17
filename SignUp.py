import unittest

import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class test_signUp(unittest.TestCase) :

    @classmethod
    def setUpClass(self) :
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.get("https://advisortodo.gntkwhqzn-test.advisortodo.com/#/auth/signin")
        self.driver.set_window_size(1366, 741)

    def test_User_signUp(self) :
        self.driver.find_element(By.LINK_TEXT, "Sign Up").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        self.driver.find_element(By.ID, "exampleInputFirstName").click()
        self.driver.find_element(By.ID, "exampleInputFirstName").send_keys("Nishit")
        self.driver.find_element(By.ID, "exampleInputLastName").send_keys("sheth")
        self.driver.find_element(By.ID, "organization").send_keys("TestingAdvisortodo")
        self.driver.find_element(By.ID, "exampleInputEmail1").click()
        self.driver.find_element(By.ID, "exampleInputEmail1").send_keys("Test@qa.com")
        self.driver.find_element(By.ID, "exampleInputPassword1").send_keys("Test@123#")
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        self.driver.get("https://advisortodo.gntkwhqzn-test.advisortodo.com/#/auth/signin")
        print('Sign Up completed')

    def test_user_Forgot_Password(self) :
        self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(1) > .form-control").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".col-lg-4")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.CSS_SELECTOR, ".col-lg-4")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, ".col-lg-4")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.CSS_SELECTOR, ".col-lg-4").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        self.driver.implicitly_wait(15)
        self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(1) > .form-control").send_keys("Test@qa.com")
        self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(2) > .form-control").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        self.driver.find_element(By.LINK_TEXT, "Forgot Password?").click()
        self.driver.find_element(By.CSS_SELECTOR, ".form-control").click()
        self.driver.find_element(By.CSS_SELECTOR, ".form-control").click()
        self.driver.find_element(By.CSS_SELECTOR, ".form-control").send_keys("")
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        self.driver.find_element(By.CSS_SELECTOR, ".form-control").send_keys("Test@qa.com")
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        self.driver.find_element(By.LINK_TEXT, "Back to Sign In").click()
        print('Forgot Password completed')

    def test_User_SignIn(self) :
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        self.driver.implicitly_wait(15)
        self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(1) > .form-control").click()
        self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(1) > .form-control").send_keys("Test@qa.com")
        self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(2) > .form-control").click()
        self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(2) > .form-control").send_keys("Test@123#")
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        self.driver.find_element_by_id("profileDropdown").click()
        self.driver.find_element_by_xpath("//div[@id='root']/div/nav/div[2]/ul/li[2]/div/div[3]/span").click()
        print('Sign in completed')
        self.driver.implicitly_wait(5)

    @classmethod
    def tearDownClass(self) :
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__' :
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./Reports', report_title='Advisortodo Report'))
