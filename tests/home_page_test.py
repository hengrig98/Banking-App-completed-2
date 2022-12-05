from selenium import webdriver
from time import sleep
from pages.home_page import HomePage
from pages.login_page import LoginPage
import pytest

def test_logout_as_user(setup):
    driver = setup
    login_page = LoginPage(driver)
    login_page.user_login()
    home_page = HomePage(driver)
    home_page.logout()
    # sleep(5)
    # assert "Sign In" in driver.page_source
    assert home_page.text_exists('Login')

def test_user_allowed_menu_items(setup):
    driver = setup
    driver = LoginPage(driver)
    LoginPage.user_login()
    home_page = HomePage(driver)
    actual_user_menus = home_page.get_side_menus()
    expected_admin_menus = {'accounts', 'messages', 'transfers', 'reports', 'news', 'profiles', 'requests', 'settings', 'system log'}
    diff = actual_user_menus.difference()
