import inspect
import logging
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait as WW


class Utility:


    def __init__(self,driver):
        self.driver = driver

    """functions used to get the title"""
    def title_name(self,title):
        WW(self.driver,5).until(EC.title_is(title))
        return self.driver.title

    """functions used to send keys for the locator"""
    def send_keys(self, by_locator, text):
        WW(self.driver,5).until(EC.presence_of_element_located(by_locator)).send_keys(text)

    """functions used to switch the windows"""
    def switch_windows(self):
        time.sleep(5)
        child_window = self.driver.window_handles[1]
        self.driver.switch_to.window(child_window)

    """functions used to switch back to the initial window of web page """
    def switch_back_window(self):
        child_window = self.driver.window_handles[0]
        self.driver.switch_to.window(child_window)
        time.sleep(3)

    """functions used to click the clickable object"""
    def click(self,by_locator):
        WW(self.driver,5).until(EC.element_to_be_clickable(by_locator)).click()

    """functions used to check the presence of element using locator"""
    def presence_of_element(self,by_locator):
        element = WW(self.driver,5).until(EC.visibility_of_element_located(by_locator))
        return element.text

    """functions used to check  the presence of 'elements' using locator """
    def presence_of_elements(self,by_locator):
        elements = self.driver.find_elements(By.XPATH, "//div[@class='product']/h4")
        for i in elements:
            return i.text

    """functions used to grab the text from the web page"""
    def grab_text(self,by_locator):
        element = WW(self.driver,5).until(EC.visibility_of_element_located(by_locator))
        return element.text

    """functions used to select the items from dropdown using select method"""

    def select_dropdown(self,by_locator,text):
        dropdown = WW(self.driver,5).until(EC.presence_of_element_located(by_locator))
        select = Select(dropdown)
        select.select_by_value(text)

