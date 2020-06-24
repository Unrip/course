import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WdW
from selenium.webdriver.support import expected_conditions as ec


browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/explicit_wait2.html'
my_price = '100'
home_price = 'price'
book_btn_locator = 'book'


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser.get(link)

    booking = WdW(browser, 13).until(ec.text_to_be_present_in_element((By.ID, home_price), my_price))
    book_btn = browser.find_element(By.ID, book_btn_locator)
    book_btn.click()

    x = browser.find_element(By.ID, 'input_value').text
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(calc(x))

    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    alert = WdW(browser, 20).until_not(ec.alert_is_present())
finally:
    browser.quit()
