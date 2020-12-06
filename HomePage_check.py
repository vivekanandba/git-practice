import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from utilities.BaseClass import BaseClass

class TestHomePage:

    def test_formSubmission(self):

        driver = webdriver.Chrome(executable_path="F:\\Learning\\Programming\\Automation Testing\\drivers\\chromedriver.exe")
        driver.get('https://rahulshettyacademy.com/angularpractice/')
        driver.maximize_window()
        driver.find_element_by_css_selector("[name='name']").send_keys('Rahul')
        driver.find_element_by_name('email').send_keys('vivek')
        driver.find_element_by_id('exampleCheck1').click()
        sel = Select(driver.find_element_by_id('exampleFormControlSelect1'))
        sel.select_by_visible_text('Male')
        driver.find_element_by_xpath("//input[@value='Submit']").click()

        alertText = driver.find_element_by_css_selector("[class*='alert-success']").text

        assert ('Success' in alertText)