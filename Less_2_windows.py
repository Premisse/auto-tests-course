from selenium import webdriver
import time
from math import log, sin


def count(x):
    return str(log(abs(12*sin(x))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:

    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector("button.trollface").click()
    new_window = browser.window_handles[1]
    first_window = browser.window_handles[0]

    browser.switch_to.window(new_window)
    x = browser.find_element_by_css_selector("#input_value")
    x_num = int(x.text)

    y = count(x_num)

    browser.find_element_by_name("text").send_keys(y)

    browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(10)
    browser.quit()