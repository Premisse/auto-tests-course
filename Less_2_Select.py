from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


def count(a, b):
    c = a + b
    return c


link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_css_selector("#num1")
    a = int(num1.text)
    num2 = browser.find_element_by_css_selector("#num2")
    b = int(num2.text)
    result = count(a, b)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(result))

    submit = browser.find_element_by_css_selector("button.btn")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()