from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from math import log, sin
import time


def count(x):
    return str(log(abs(12*sin(x))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:

    browser = webdriver.Chrome()
    browser.get(link)
    # browser.implicitly_wait(1)

    # browser.find_element_by_id("button")

    # button = browser.find_element_by_id("verify")

    button = browser.find_element_by_id("book")
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button.click()

    x = browser.find_element_by_css_selector("#input_value")
    x_num = int(x.text)
    y = count(x_num)

    browser.find_element_by_name("text").send_keys(y)
    browser.find_element_by_css_selector("#solve").click()

finally:
    time.sleep(5)
    browser.quit()