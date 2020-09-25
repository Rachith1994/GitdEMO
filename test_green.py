import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Pages.checkout import CheckOut
from Pages.homepage import HomePage
from Utility.baseclass import BaseClass
from data_for_test import Datas


class TestCases(BaseClass):


    """verify the title is present or not """
    def test_for_title(self):
        log = self.GetLogger()
        log.info("Checking for main title"+Datas.site_title)
        homepage = HomePage(self.driver)
        title = homepage.get_title(Datas.site_title)
        assert title == Datas.site_title
    """checking for the top deals link presence"""
    def test_for_presence_of_TopDeals(self):
        homepage = HomePage(self.driver)
        flag1 = homepage.get_presence_of_topDeals()
        assert flag1

    def test_for_flight_application(self):
        log = self.GetLogger()
        log.info("getting titile of application" +Datas.flight_title)
        homepage = HomePage(self.driver)
        homepage.click_flight()
        homepage.get_flight()
        flag3 = homepage.get_title(Datas.flight_title)
        assert flag3
        self.driver.close()


    """testing for the presence of element Item in the home page"""
    def test_for_presence_of_Item(self):
        time.sleep(3)
        homepage = HomePage(self.driver)
        homepage.get_back_from_flight()
        flag2 = homepage.get_presence_cart_icon_items()
        assert flag2
    """testing for the add vegitables is present in the given input"""
    def test_for_vegitables_search(self):

        r = []
        homepage = HomePage(self.driver)
        homepage.get_keys(Datas.vegitable_select)
        time.sleep(5)
        list = self.driver.find_elements(By.XPATH, HomePage.vegies_locator)
        for i in list:
            items = i.text
            r.append(items)
        assert Datas.vegitable in r
    """to verify the added list is present in the checkout page"""
    def test_add_cart(self):
        r1 = []
        time.sleep(5)
        buttons = self.driver.find_elements(By.XPATH, HomePage.button_locator_to_click)
        for button in buttons:
            button.click()
        homepage = HomePage(self.driver)
        homepage.get_click_cart_icon()
        homepage.get_click_proceed_icon()
        names = self.driver.find_elements(By.CSS_SELECTOR, "p[class='product-name']")
        for i in names:
            items = i.text
            r1.append(items)
        assert Datas.vegitable in r1

    """checking for the discount amount when valid and invalid coupen is given """
    def test_amount_discounted(self):
        checkout = CheckOut(self.driver)
        total = checkout.get_total_amount()
        checkout.get_coupen_code(Datas.coupen_code)
        checkout.get_click_coupen()
        time.sleep(6)
        discount = checkout.get_discount_amount()
        assert total > discount
    """verify the selected country is correct"""
    def test_for_country(self):
        checkout = CheckOut(self.driver)
        checkout.get_proceed()
        checkout.get_country(Datas.Country)
        time.sleep(5)
        country = checkout.check_country()
        assert country == Datas.Country
    """verify the order has been successfully accepted"""
    def test_for_success(self):
        chekout = CheckOut(self.driver)
        chekout.get_submit()
        success = chekout.again_homepage()
        assert success == Datas.Home_logo




