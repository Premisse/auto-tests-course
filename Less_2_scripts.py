from selenium import webdriver
import time
from math import log, sin


def count(x):
    result = log(abs(12*sin(x)))
    return str(result)

link = "http://SunInJuly.github.io/execute_script.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element_by_css_selector("#input_value")
    num_x = int(x.text)
    y = count(num_x)

    answer = browser.find_element_by_css_selector("#answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
    answer.send_keys(y)

    browser.find_element_by_css_selector("#robotCheckbox").click()
    browser.find_element_by_css_selector("#robotsRule").click()

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    assert True
finally:
    time.sleep(5)
    browser.quit()