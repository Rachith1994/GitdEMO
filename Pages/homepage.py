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
    select_page_5_locator = (By.XPATH, "//span[contains(text(),'4')]")
    fruit_name_locator = (By.XPATH, "//td[contains(text(),'Banana')]")
    one_item_select_locator = (By.XPATH, "//div[@class='products']//div[1]//div[3]//button[1]")
    cart_empty_text = (By.XPATH, "//div[@class='cart-preview active']//div//div//h2[contains(text(),'You cart is empty!')]")

    cancel_item = (By.CLASS_NAME, "product-remove")

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

    def get_switch_window(self):
        self.switch_windows()

    def get_switch_back_window(self):
        self.switch_back_window()

    def get_keys(self,text):
        self.send_keys(self.search_send_keys,text)



    def get_click_cart_icon(self):
        self.click(self.click_cart_icon)

    def get_click_proceed_icon(self):
        self.click(self.click_proceed_button)

    def get_topdeals_page(self):
        self.click(self.presence)

    def get_page_5(self):
        self.click(self.select_page_5_locator)

    def get_fruit_name(self):
        return self.presence_of_element(self.fruit_name_locator)

    def get_click_one_item(self):
        self.click(self.one_item_select_locator)

    def get_cart_message(self):
        return self.presence_of_element(self.cart_empty_text)

    def get_cancel_item(self):
        self.click(self.cancel_item)






