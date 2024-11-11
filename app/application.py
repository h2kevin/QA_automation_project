from pages.base_page import Page
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.market_page import MarketPage


class Application:

    def __init__(self, driver):
        self.base_page = Page(driver)
        self.login_page = LoginPage(driver)
        self.main_page = MainPage(driver)
        self.market_page = Market(driver)
