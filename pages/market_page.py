from pages.base_page import Page
from selenium.webdriver.common.by import By
class Market(Page):
    Check_all_market = (By.XPATH, "//div[@class='tag-text-proparties' and text()='ALL']")
    Check_agencies = (By.XPATH, "//div[@class='tag-text-proparties' and text()='Agencies']")
    Check_developers = (By.XPATH, "//div[@class='tag-text-proparties' and text()='Developers']")
    def verify_the_market_url(self):
        self.verify_url('https://soft.reelly.io/market-companies')
    def Check_all_market(self):
        self.check_all_market('market', *self.Check_all_market)
    def Check_agencies(self):
        self.check_agencies('agencies', *self.Check_agencies)
    def Check_developers(self):
        self.check_developers('developers',*self.Check_developers)