from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_basket_button(browser):
    time.sleep(30)
    assert browser.find_element(By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket'), print ('Not find button')