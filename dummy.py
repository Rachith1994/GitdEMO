
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="D:\python\driver\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/country")
driver.find_element_by_xpath("//a[@class='cart-icon']//img[contains(@class,'')]").click()
time.sleep(1)
driver.find_element_by_xpath("//a[@class='cart-icon']//img[contains(@class,'')]").click()
time.sleep(2)
driver.find_element_by_tag_name("button").click()
time.sleep(4)

dropdown = driver.find_element_by_xpath("//div[@class='wrapperTwo']//div//select")
select = Select(dropdown)
select.select_by_value("India")
element = driver.find_element_by_tag_name("select")
Value = element.get_attribute('value')
print(Value)
child_window = driver.window_handles(1)
driver.switch_to.window(child_window)

driver.
