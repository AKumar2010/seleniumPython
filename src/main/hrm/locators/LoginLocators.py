
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By



class LoginLocators:


    def __init__(self,driver):
        self.driver = driver

    def get_username(self)->WebElement:
        user_elememt=self.driver.find_element(By.XPATH,"//input[@name='username']")     
        return user_elememt

    def get_password(self):
        return self.driver.find_element(By.XPATH, "//input[@name='password']")

    def get_login_button(self):
        return self.driver.find_element(By.XPATH, "//button[@type='submit']")
    