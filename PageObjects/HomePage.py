from selenium.webdriver.common.by import By

from PageObjects.checkoutPage import CheckPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver


    Veg = (By.CSS_SELECTOR, "input[type='search']")
    Items = (By.XPATH, "//div[@class='product']/h4")
    select = (By.XPATH, "//div[@class='product-action']/button")
    BagIcon = (By.CSS_SELECTOR, "img[src='./images/bag.png']")



    def GetVeg(self):
        return self.driver.find_element(*HomePage.Veg)

    def GetItems(self):
        return self.driver.find_elements(*HomePage.Items)

    def GetSelect(self):
        return self.driver.find_elements(*HomePage.select)

    def GetBag(self):
        self.driver.find_element(*HomePage.BagIcon).click()
        preview = CheckPage(self.driver)
        return preview

