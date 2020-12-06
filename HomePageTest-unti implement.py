import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage

class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):

        homepage = HomePage(self.driver)
        homepage.getName().send_keys(getData[0])
        homepage.getEmail().send_keys(getData[1])
        homepage.getCheck().click()
        self.selectOptionByText(homepage.getGender(),getData[2])
        homepage.getSubmit().click()
        alertText = homepage.getSuccessMessage().text
        assert ('Success' in alertText)
        self.driver.refresh()

    @pytest.fixture(params=[("Vivek",'Anand','Male'), ("asder",'bva','Male') ])
    def getData(self, request):
        return request.param
