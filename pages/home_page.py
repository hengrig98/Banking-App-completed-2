from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.login_page import LoginPage

class HomePage(BasePage):


    # class attributes, for selectors like logout button and side menu
    # using * to unpack tuples, logout & side menue element is comma separated (tuple)
    logout_button = By.CSS_SELECTOR, ".controls__logout > span"
    side_menu = By.CSS_SELECTOR, ".aside__label"


    def __init__(self, driver) -> None:
        self.driver = driver

    def logout(self):
        self.driver.find_element(*self.logout_button).click()
        
    def get_side_menus(self):
        side_menus = self.driver.find_elements(*self.side_menu)
        return {menu.text.lower() for menu in side_menus}
