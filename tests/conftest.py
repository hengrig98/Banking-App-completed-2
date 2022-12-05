import pytest
from selenium import webdriver
from datetime import datetime
import os
from pages.login_page import LoginPage
from configs import config
from logs.logger import logger

def launch_app():
    driver = webdriver.Firefox()
    logger.info(f"Launched the {driver.name} {driver.capabilities['browserVersion']}")
    driver.get(config.URL)
    logger.info(f'Navigated to {config.URL}')
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver

def teardown(driver):
    test_name = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1]
    test_name = test_name.split(']')[0]
    test_name = test_name.split(' ')[0]
    timestamp = datetime.now().strftime('%m%d%y_%H%M%S')
    driver.save_screenshot(fr'.\evidence\{test_name}_{timestamp}.png')
    logger.info(f'Completed Test Case: {test_name}')
    driver.quit()
    logger.info('Closed the browser.')


@pytest.fixture()
def setup():
    driver = launch_app()
    yield driver
    teardown(driver)

@pytest.fixture()
def user_setup():
    driver = launch_app()
    login_page = LoginPage(driver)
    login_page.user_login()
    yield driver
    teardown(driver)

@pytest.fixture()
def admin_setup():
    driver = launch_app()
    login_page = LoginPage(driver)
    login_page.admin_login()
    yield driver
    teardown(driver)