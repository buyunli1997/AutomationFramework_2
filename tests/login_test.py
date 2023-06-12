import time

import allure
import moment
import pytest
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from utils import utils as utils


@pytest.mark.usefixtures("test_setup")
class TestLogin:
    def test_login(self):
        driver = self.driver
        driver.get(utils.URL)
        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_login()
        time.sleep(3)

    def test_logout(self):
        try:
            driver = self.driver
            homepage = HomePage(driver)
            homepage.click_profile()
            homepage.click_logout()
            x = driver.title
            assert x == 'Orange'
        except AssertionError as error:
            print('There was an AssertionError!')
            print(error)
            time.sleep(3)
            currentTime = moment.now().strftime('%d-%m-%Y_%H-%M-%S')
            testName = utils.whoami()
            screenshotMame = testName+ "_" + currentTime
            allure.attach(self.driver.get_screenshot_as_png(),name=screenshotMame,attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("C:/Users/buyun/PycharmProjects/uiautomation/AutomationFramework_1/screenshots/" + screenshotMame + ".png")
            raise
        except:
            print('There was an exception!')
        else:
            print('No exception occurred')
        finally:
            print("I am inside finally block")




