import pytest
from selenium import webdriver
from utilities import read_utils

"""Browser Configuration"""


class WebDriverWrapper:
    driver = None

    @pytest.fixture(scope="function", autouse=True)
    def browser_config(self):
        browser_name = read_utils.get_value_from_json("../test_data/data.json", "browser")

        if browser_name == "edge":

            self.driver = webdriver.Edge()
        elif browser_name == "ff":
            self.driver = webdriver.Firefox()
        elif browser_name == "chrome":
            opt = webdriver.ChromeOptions()
            opt.add_argument("start-maximized")
            self.driver = webdriver.Chrome()
        else:
            print("Please mention browser name inside data.json file")

        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get("https://www.agoda.com/")
        yield
        self.driver.quit()