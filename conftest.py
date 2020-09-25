from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def invokeSetup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name =="chrome":
        driver = webdriver.Chrome(executable_path="D:\python\driver\chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="D:\python\driver\geckodriver.exe")
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


