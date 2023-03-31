import time

import pytest
from selenium.webdriver.common.by import By
from base.webdriver_listener import WebDriverWrapper
from utilities import data_source


class TestLogin(WebDriverWrapper):

    email = "johndoe@email.com"
    password = "examplepassword"

    def test_valid_login(self):
        # Click "Sign in" button
        sign_in_btn =  self.driver.find_element(By.XPATH, "//button[@data-selenium='header-sign-in']")
        sign_in_btn.click()

        # Enter the login details in the form
        email_input = self.driver.find_element(By.XPATH, "//input[@name='email']")
        email_input.send_keys(self.email)

        password_input = self.driver.find_element(By.XPATH, "//input[@name='password']")
        password_input.send_keys(self.password)

        # Click "Login" button
        login_btn = self.driver.find_element(By.XPATH, "//button[@data-selenium='login-form-submit-button']")
        login_btn.click()

        # Wait for the page to load and check for successful login
        time.sleep(5)
        assert "agoda.com: Smarter Hotel Booking" in self.driver.title
        assert "My Account" in self.driver.page_source
        assert "Sign out" in self.driver.page_source

    """Invalid Login Test - Data Driven Using .csv file"""

    @pytest.mark.parametrize("mobile,error", data_source.test_invalid_login_data)
    def test_invalid_login(self, mobile, error):
        sign_in_btn = self.driver.find_element(By.XPATH, "//button[@data-selenium='header-sign-in']")
        sign_in_btn.click()

        # Enter the login details in the form
        email_input = self.driver.find_element(By.XPATH, "//input[@name='email']")
        email_input.send_keys(self.email)

        password_input = self.driver.find_element(By.XPATH, "//input[@name='password']")
        password_input.send_keys(self.password)

        # Click "Login" button
        login_btn = self.driver.find_element(By.XPATH, "//button[@data-selenium='login-form-submit-button']")
        login_btn.click()

        # Wait for the page to load and check for error message
        time.sleep(5)
        assert "The email and password you entered are incorrect." in self.driver.page_source