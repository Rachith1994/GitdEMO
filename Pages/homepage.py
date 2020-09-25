import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Utility.utility import Utility


class HomePage(Utility):

    presence = (By.LINK_TEXT, "Top Deals")
    search_send_keys = (By.XPATH, "//input[@placeholder='Search for Vegetables and Fruits']")
    cart_icon_items = (By.XPATH, "//td[contains(text(),'Items')]")
    vegies_locator = "//div[@class='product']/h4"
    button_locator_to_click =  "//div[@class='product-action']/button"
    click_cart_icon = (By.XPATH, "//a[@class='cart-icon']//img[contains(@class,'')]")
    click_proceed_button = (By.XPATH, "//button[contains(text(),'PROCEED TO CHECKOUT')]")
    flight_locator = (By.LINK_TEXT, "Flight Booking")

    def __init__(self,driver):
        super().__init__(driver)


    def get_title(self,title):
       return self.title_name(title)

    def get_presence_of_topDeals(self):
        return self.presence_of_element(self.presence)

    def get_presence_cart_icon_items(self):
        return self.presence_of_element(self.cart_icon_items)

    def click_flight(self):
        self.click(self.flight_locator)

    def get_flight(self):
        self.switch_windows()

    def get_back_from_flight(self):
        self.switch_back_window()

    def get_keys(self,text):
        self.send_keys(self.search_send_keys,text)



    def get_click_cart_icon(self):
        self.click(self.click_cart_icon)

    def get_click_proceed_icon(self):
        self.click(self.click_proceed_button)




