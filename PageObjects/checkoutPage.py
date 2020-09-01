from selenium.webdriver.common.by import By


class CheckPage:

    def __init__(self, driver):
        self.driver = driver

    preview = (By.XPATH, "//div[@class='cart-preview active']/div/button")
    list = (By.CSS_SELECTOR, "p[class='product-name']")
    before = (By.CSS_SELECTOR, "span[class='discountAmt']")
    Promo = (By.CSS_SELECTOR, "input[type='text']")
    promoButton = (By.CSS_SELECTOR, "button[class='promoBtn']")
    cartTotal = (By.XPATH, "//table[@class='cartTable']/tr/td[5]/p")
    CheckTotal = (By.CSS_SELECTOR, "span[class='totAmt']")
    after = (By.CSS_SELECTOR, "span[class='discountAmt']")



    def GetPreview(self):
        self.driver.find_element(*CheckPage.preview).click()
        return CheckPage(self.driver)

    def GetList(self):
        return self.driver.find_elements(*CheckPage.list)

    def GetBefore(self):
        return self.driver.find_element(*CheckPage.before)

    def GetPromo(self):
        return self.driver.find_element(*CheckPage.Promo)

    def GetPromoButton(self):
        return self.driver.find_element(*CheckPage.promoButton)

    def GetCartTotal(self):
        return self.driver.find_elements(*CheckPage.cartTotal)

    def GetCheckTotal(self):
        return self.driver.find_element(*CheckPage.CheckTotal)


    def GetAfter(self):
        return self.driver.find_element(*CheckPage.after)



