from selenium.webdriver.common.by import By

from Utility.utility import Utility


class CheckOut(Utility):

    products_in_checkout = "p[class='product-name']"
    total_amount = (By.XPATH, "//span[@class='totAmt']")
    discount_total_amount = (By.XPATH, "//span[@class='discountAmt']")
    coupen_enter_locator = (By.XPATH, "//input[@placeholder='Enter promo code']")
    click_for_coupen_locator = (By.XPATH, "//button[@class='promoBtn']")
    place_order_locator = (By.XPATH, "//button[contains(text(),'Place Order')]")
    country_select_locator = (By.XPATH, "//div[@class='wrapperTwo']//div//select")
    check_box_locator = (By.XPATH, "//input[@class='chkAgree']")
    sumbit_button_locator = (By.XPATH, "//button[contains(text(),'Proceed')]")
    again_homepage_locator = (By.XPATH, "//div[@class='brand greenLogo']")

    def __init__(self,driver):
        super().__init__(driver)

    def get_total_amount(self):
        return self.grab_text(self.total_amount)

    def get_coupen_code(self,text):
        self.send_keys(self.coupen_enter_locator,text)

    def get_click_coupen(self):
        self.click(self.click_for_coupen_locator)

    def get_discount_amount(self):
        return self.grab_text(self.discount_total_amount)

    def get_proceed(self):
        self.click(self.place_order_locator)

    def get_country(self,text):
        self.select_dropdown(self.country_select_locator,text)

    def check_country(self):
        element = self.driver.find_element(By.XPATH, "//div[@class='wrapperTwo']//div//select")
        value = element.get_attribute('value')
        return value

    def get_submit(self):
        self.click(self.check_box_locator)
        self.click(self.sumbit_button_locator)

    def again_homepage(self):
        return self.presence_of_element(self.again_homepage_locator)




