# Each test case should be independent, meaning opening to close, should not impact eachoter.
# implicit waits and sleep fixes delayed assertion issues
from selenium import webdriver
from time import sleep
# Here we import page class, and class name 'LoginPage' which include methods and values for testing, such as log in as User.
from pages.login_page import LoginPage
import pytest

# Each test case is named based on the page class for testing, makes it easier to run separately...@pytest.mark
@pytest.mark.Login 
def test_landing_page(setup):
    driver = setup 
    assert "div > h1"[0] in driver.page_source

@pytest.mark.Login
def test_user_login(setup):
    driver = setup
    login_page = LoginPage(driver) 
    login_page.user_login()
    assert login_page.text_exists("Account number")

@pytest.mark.Login
def test_admin_login(setup):
    driver = setup
    login_page = LoginPage(driver)
    login_page.admin_login()
    sleep(5)
    assert login_page.text_exists("Log Out")
 
#  Parametrizing/preparing our invalid test data to plug into test methods, this is a list of tuples...value/value/expectation(checkpoint)
invalid_login_data = [
    ("", "", "Field is required."),
    ("test", "test", "Wrong username or password."),
    ("abc", "test", "Should be minimum 4 chars."),
    ("", "test", "Field is required."),
    ("test", "", "Field is required.")
]

@pytest.mark.parametrize("username, password, checkpoint", invalid_login_data)
def test_invalid_login(setup, username, password, checkpoint):
    driver = setup
    login_page = LoginPage(driver) 
    login_page.login(username, password)
    assert login_page.text_exists(checkpoint)

