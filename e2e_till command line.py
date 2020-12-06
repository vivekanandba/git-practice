import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass

#@pytest.mark.usefixtures('setup')
class TestOne(BaseClass):

    def test_e2e(self):

        self.driver.find_element_by_css_selector("a[href*='shop']").click()
        products = self.driver.find_elements_by_xpath("//div[@class='card h-100']")
        #//div[@class='card h-100']/div/h4/a
        for product in products:
            productName = product.find_element_by_xpath("div/h4/a").text
            if productName == 'Blackberry':
                #//div[@class='card h-100']/div[2]/button
                # Add item into cart
                product.find_element_by_xpath("div/button").click()

        self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
        assert (self.driver.find_element_by_xpath("//h4[@class='media-heading']")).text == 'Blackberry'

        self.driver.find_element_by_css_selector("button[class*='btn-success']").click()
        #driver.find_element_by_xpath["//button[@class='btn btn-success']"].click()
        self.driver.find_element_by_id('country').send_keys('ind')

        wait = WebDriverWait(self.driver,7)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
        self.driver.find_element_by_link_text("India").click()
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()

        self.driver.find_element_by_css_selector("[type='submit']").click()
        #print(driver.find_element_by_css_selector("div[class*='alert-dismissible']").text)
        #succ = "Success! Thank you! Your order will be delivered in next few weeks :-)."
        success_text = self.driver.find_element_by_class_name('alert-success').text
        assert 'Success' in success_text
        self.driver.save_screenshot('screen.png')
        self.driver.get_screenshot_as_file('screen1.png')