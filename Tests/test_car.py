import time

from PageObjects.HomePage import HomePage
from PageObjects.checkoutPage import CheckPage
from utilities.BaseClass import BaseClass


class TestVeg(BaseClass):
    def test_cart(self):
        log = self.GetLogger()
        veg = HomePage(self.driver)
        veg.GetVeg().send_keys("ber")
        time.sleep(3)
        select = HomePage(self.driver)
        buttons = select.GetSelect()
        for button in buttons:
            button.click()
        Bagicon = HomePage(self.driver)
        preview = Bagicon.GetBag()
        list = preview.GetPreview()
        veggis = list.GetList()
        for vegi in veggis:
            FinalPAge = vegi.text
        log.info(FinalPAge)
        self.VerifyLink("promoCode")
        before = CheckPage(self.driver)
        Beforediscount = before.GetBefore().text
        print(f"Your order before Discount is {Beforediscount} ")
        promo = CheckPage(self.driver)
        promo.GetPromo().send_keys("rahulshettyacademy")
        promoButton = CheckPage(self.driver)
        promoButton.GetPromoButton().click()
        self.VerifyLink('promoInfo')
        Amounts = CheckPage(self.driver)
        Total = Amounts.GetCartTotal()
        sum = 0
        for total in Total:
            sum = sum + int(total.text)
        log.info(f"Total amount of your cart is {sum}")
        C_Total = CheckPage(self.driver)
        CheckTotal = C_Total.GetCheckTotal()
        assert sum == int(CheckTotal.text)
        After = CheckPage(self.driver)
        AfterDiscount = After.GetAfter().text
        log.info(f"Your order after Discount is {AfterDiscount} ")
        DiscountAmount = int(Beforediscount) - float(AfterDiscount)
        log.info(f"your Discount amount is {DiscountAmount}")















































