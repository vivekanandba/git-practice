import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage
from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage

#@pytest.mark.usefixtures('setup')
class TestOne(BaseClass):

    def test_e2e(self):

        homePage = HomePage(self.driver)
        homePage.shopItems().click()

        checkOutPage = CheckoutPage(self.driver)
        products = checkOutPage.getCardTitles()
        for _ in products:
            product_Name = checkOutPage.productName
            if product_Name == 'Blackberry':
                checkOutPage.getCardFooter().click()

        checkOutPage.getCheckOutbutton().click()
        checkOutPage.getConfirmButton().click()

        confirmPage = ConfirmPage(self.driver)
        confirmPage.getCountry().send_keys('ind')
        wait = WebDriverWait(self.driver,7)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))

        confirmPage.getselectCountry().click()
        confirmPage.getclickCountry().click()
        confirmPage.getsubmitbutton().click()
        success_text = confirmPage.getassertmsg().text
        assert 'Success' in success_text