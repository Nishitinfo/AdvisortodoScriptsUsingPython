import unittest

import HtmlTestRunner
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class test_tasks(unittest.TestCase) :

    @classmethod
    def setUpClass(self) :
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.get("https://advisortodo.gntkwhqzn-test.advisortodo.com/#/auth/signin")
        self.driver.set_window_size(1366, 741)

    def test_User_tasks(self) :
        try :
            self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(1) > .form-control").click()
            self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(1) > .form-control").send_keys(
                "Test@qa.com")
            self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(2) > .form-control").click()
            self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(2) > .form-control").send_keys("Test@123#")
            self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
            self.driver.implicitly_wait(10)
            self.driver.find_element(By.XPATH,
                                     "/html[1]/body[1]/div[1]/div[1]/div[1]/nav[1]/ul[1]/li[3]/a[1]/span[1]").click()
            element = self.driver.find_element(By.ID, "addTask")
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            element = self.driver.find_element(By.CSS_SELECTOR, "body")
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            self.driver.find_element(By.CSS_SELECTOR, ".fa-plus").click()
            element = self.driver.find_element(By.CSS_SELECTOR, ".fa-plus")
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            element = self.driver.find_element(By.CSS_SELECTOR, "body")
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            self.driver.find_element(By.ID, "combobox1").click()
            self.driver.find_element(By.ID, "combobox1").send_keys("Task for test")
            self.driver.find_element(By.ID, "combobox1").send_keys(Keys.ENTER)
            self.driver.find_element(By.CSS_SELECTOR, ".m-0").click()
            self.driver.find_element(By.XPATH, "//div[@id=\'taskPriority\']/div[2]/div/div").click()
            self.driver.find_element(By.XPATH, "//div[@id=\'taskPriority\']/div[2]/div[2]/div/div[2]").click()
            self.driver.find_element(By.ID, "taskDueDate").click()
            self.driver.find_element(By.CSS_SELECTOR, ".react-datepicker__day--016").click()
            self.driver.find_element(By.CSS_SELECTOR, ".row:nth-child(5) .form-control").click()
            self.driver.find_element(By.CSS_SELECTOR, ".react-datepicker__day--016").click()
            self.driver.find_element(By.XPATH,
                                     "//div[@id=\'root\']/div/div/div/div/div/div[2]/div/div[2]/form/div[6]/div/div/div/div[2]/div/div").click()
            self.driver.find_element(By.XPATH,
                                     "//div[@id=\'root\']/div/div/div/div/div/div[2]/div/div[2]/form/div[6]/div/div/div/div[2]/div[2]/div/div[2]").click()
            self.driver.find_element(By.CSS_SELECTOR, ".css-1pahdxg-control > .css-1hwfws3").click()
            self.driver.find_element(By.CSS_SELECTOR, ".css-1pahdxg-control .css-1uccc91-singleValue").click()
            self.driver.find_element(By.CSS_SELECTOR, ".react-tagsinput-input").click()
            self.driver.find_element(By.CSS_SELECTOR, ".react-tagsinput-input").send_keys("test")
            self.driver.find_element(By.CSS_SELECTOR, ".react-tagsinput-input").send_keys(Keys.ENTER)
            self.driver.find_element(By.CSS_SELECTOR, ".react-tagsinput-input").send_keys("task")
            self.driver.find_element(By.CSS_SELECTOR, ".react-tagsinput-input").send_keys(Keys.ENTER)
            self.driver.find_element(By.CSS_SELECTOR, ".react-tagsinput-input").send_keys("nishit")
            self.driver.find_element(By.CSS_SELECTOR, ".react-tagsinput-input").send_keys(Keys.ENTER)
            self.driver.find_element(By.XPATH,
                                     "//div[@id=\'root\']/div/div/div/div/div/div[2]/div/div[2]/form/div[9]/div/div/div/div[2]/div/div/div").click()
            self.driver.find_element(By.XPATH,
                                     "//div[@id=\'root\']/div/div/div/div/div/div[2]/div/div[2]/form/div[9]/div/div/div/div[2]/div[2]/div/div").click()
            element = self.driver.find_element(By.ID, "cloneTask")
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            element = self.driver.find_element(By.CSS_SELECTOR, "body")
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            self.driver.find_element(By.CSS_SELECTOR, "#cloneTask > .fa").click()
            element = self.driver.find_element(By.ID, "cloneTask")
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            element = self.driver.find_element(By.CSS_SELECTOR, "body")
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            self.driver.find_element(By.CSS_SELECTOR, ".col-lg-4").click()
            self.driver.find_element(By.CSS_SELECTOR, ".col-lg-2 > .mr-2").click()
            self.driver.find_element(By.CSS_SELECTOR, ".col-lg-2 > .mr-2").send_keys("test")
            self.driver.find_element(By.CSS_SELECTOR, ".col-lg-2 > .mr-2").send_keys(Keys.ENTER)
            self.driver.find_element(By.XPATH,
                                     "//div[@id=\'root\']/div/div/div/div/div/div/div/div/div/div[3]/div/div/div/div").click()
            self.driver.find_element(By.XPATH,
                                     "//div[@id=\'root\']/div/div/div/div/div/div/div/div/div/div[3]/div/div[2]/div/div[2]").click()
            self.driver.find_element(By.CSS_SELECTOR, ".css-127g5zj:nth-child(2) > .css-1t70qfw").click()
            self.driver.find_element(By.XPATH, "//div[2]/div/div[2]").click()
            self.driver.find_element(By.CSS_SELECTOR, ".css-127g5zj:nth-child(2) .css-1uccc91-singleValue").click()
            self.driver.find_element(By.XPATH, "//div[2]/div/div[2]").click()
            self.driver.find_element(By.CSS_SELECTOR, ".css-127g5zj:nth-child(2) > .css-1t70qfw").click()
            self.driver.find_element(By.XPATH, "//div[2]/div/div[3]").click()
            self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(1) .checkbox").click()
            self.driver.find_element(By.XPATH,
                                     "//div[@id=\'root\']/div/div/div/div/div/div/div/div/div/div[4]/div/div/div").click()
            self.driver.find_element(By.XPATH,
                                     "//div[@id=\'root\']/div/div/div/div/div/div/div/div/div/div[4]/div/div[2]/div/div[3]").click()
            self.driver.find_element(By.CSS_SELECTOR, ".m-0").click()
            element = self.driver.find_element(By.ID, "deleteTask")
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            self.driver.find_element(By.ID, "deleteTask").click()
            self.driver.find_element(By.XPATH,
                                     "//div[@id=\'root\']/div/div/div/div/div/div/div/div/div/div[4]/div/div/div").click()
            self.driver.find_element(By.XPATH,
                                     "//div[@id=\'root\']/div/div/div/div/div/div/div/div/div/div[4]/div/div[2]/div/div").click()
            self.driver.find_element(By.CSS_SELECTOR, ".m-0 > span").click()
            element = self.driver.find_element(By.CSS_SELECTOR, ".fa-trash")
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            element = self.driver.find_element(By.CSS_SELECTOR, "body")
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            element = self.driver.find_element(By.ID, "deleteTask")
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            self.driver.find_element(By.ID, "deleteTask").click()
            self.driver.find_element(By.ID, "profileDropdown").click()
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
