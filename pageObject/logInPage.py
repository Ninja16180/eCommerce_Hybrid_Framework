from selenium import webdriver
from selenium.webdriver.common.by import By


class logInPage:
    textbox_username_id = "Email"
    textbox_pwd_id = "Password"
    button_login_xpath = "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button"
    link_logout_xpath = '//*[@id="navbarText"]/ul/li[3]/a'

    def __init__(self,driver):
        self.driver = driver

    def setUserName(self,username):  #username will be coming from the testcase class using this loginpage class
        self.driver.find_element(by=By.ID, value=self.textbox_username_id).clear()
        self.driver.find_element(by=By.ID, value=self.textbox_username_id).send_keys(username)

    def setPassWord(self,pwd):
        self.driver.find_element(by=By.ID, value=self.textbox_pwd_id).clear()
        self.driver.find_element(by=By.ID, value=self.textbox_pwd_id).send_keys(pwd)

    def clickLogIn(self):
        self.driver.find_element(by=By.XPATH, value=self.button_login_xpath).click()

    def clickLogOut(self):
        self.driver.find_element(by=By.XPATH, value=self.link_logout_xpath).click()
