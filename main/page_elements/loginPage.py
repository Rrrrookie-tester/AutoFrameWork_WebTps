"""
@Project: AutoFrameWork_WebTps   
@Description: To local and control login page elements
@Time:2021/6/7 13:48       
@Author:zexin                
 
"""
from utils.BasePage import BasePage
from utils.ReadYaml import ReadYaml


class LoginPage(BasePage):
    elements_config = ReadYaml("main\\page_data\\loginPage.yaml")

    def input_username(self, une):
        element_name = "username_input"
        username_input = self.find_element_wait(element_name, *self.elements_config[element_name])
        self.send_keys(username_input, une, element_name)

    def input_password(self, pwd):
        element_name = "password_input"
        password_input = self.find_element_wait(element_name, *self.elements_config[element_name])
        self.send_keys(password_input, pwd, element_name)

    def click_login_button(self):
        element_name = "login_button"
        login_button = self.find_element_wait(element_name, *self.elements_config[element_name])
        self.click(login_button, element_name)