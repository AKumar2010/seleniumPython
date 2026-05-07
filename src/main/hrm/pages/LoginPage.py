from src.main.hrm.locators.LoginLocators import LoginLocators

class LogInPage:


    def __init__(self, driver):
        self.driver = driver
        self.locators = LoginLocators(self.driver)

    def do_login(self, username, password): 
        self.locators.get_username().clear()
        self.locators.get_username().send_keys(username)
        self.locators.get_username().clear()
        self.locators.get_password().send_keys(password)
        self.locators.get_login_button().click()
        
        
