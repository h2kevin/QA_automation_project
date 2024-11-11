from pages.base_page import Page
from selenium.webdriver.common.by import By

class LoginPage(Page):
    Enter_email = (By.ID, "email-2")
    Enter_password = (By.ID, "field")
    Continue_btn = (By.CSS_SELECTOR, ".login-button.w-button")

    def enter_login_information(self,email,password,continue_btn):
        self.input_text( *self.Enter_email)
        self.input_text(*self.Enter_password)
        self.click(*self.Continue_btn)
