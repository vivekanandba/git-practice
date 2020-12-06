import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage

class TestHomePage(BaseClass):

    def test_formSubmission(self):

        homepage = HomePage(self.driver)
        homepage.getName().send_keys('Vivek')
        homepage.getEmail().send_keys('vivek@gadjoy.in')
        homepage.getCheck().click()
        sel = Select(homepage.getGender())
        sel.select_by_visible_text('Male')
        homepage.getSubmit().click()
        alertText = homepage.getSuccessMessage().text

        assert ('Success' in alertText)