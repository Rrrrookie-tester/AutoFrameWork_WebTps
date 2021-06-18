"""
@Project: AutoFrameWork_WebTps   
@Description: login workflow
@Time:2021/6/7 14:09       
@Author:zexin                
 
"""
from selenium import webdriver

from main.page_elements.loginPage import LoginPage


def login(driver, username, password):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.max_window()
    login_page.input_username(username)
    login_page.input_password(password)
    login_page.click_login_button()