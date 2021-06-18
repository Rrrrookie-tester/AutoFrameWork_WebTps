"""
@Project: AutoFrameWork_WebTps   
@Description: To package selenium common function
@Time:2021/6/7 9:34       
@Author:zexin                
 
"""
import os
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from utils.Exception import deal_exception_with_image
from utils.Logger import Logger
from utils.ReadYaml import ReadYaml


class BasePage(object):
    logger = Logger("BasePage.py").getlog()
    # 初始化

    def __init__(self, driver):
        config_data = ReadYaml("data\\config.yaml")
        self.base_url = config_data['base_url']
        self.driver = driver
        self.timeout = 30

    # 定义打开登录页面方法
    def _open(self):
        # try:
        #     url = self.base_url
        #     self.driver.get(url)
        # except:
        #     deal_exception_with_image(self.driver, self.logger, "open " + url + "error !")
        #     os._exit(0)
        url = self.base_url
        self.driver.get(url)
        # self.driver.switch_to.frame('放射治疗计划系统软件')  # 切换到登录窗口的iframe　　# 定义定义open方法，调用_open()进行打开

    def open(self):
        self._open()

    def close(self):
        self.driver.close()

    def max_window(self):
        self.driver.maximize_window()

    # 定位方法封装
    def find_element(self, element_name, *loc):
        try:
            return self.driver.find_element(*loc)
        except:
            deal_exception_with_image(self.driver, self.logger, "get element： " + element_name + " error !")

    def find_elements(self, elements_name, *loc):
        try:
            return self.driver.find_elements(*loc)
        except:
            deal_exception_with_image(self.driver, self.logger, "get element： " + elements_name + " error !")

    # 常用操作方法封装
    def click(self, element, element_name):
        try:
            element.click()
        except:
            deal_exception_with_image(self.driver, self.logger, "click %s error !" % element_name)

    def move_to_click(self, x, y):
        try:
            ActionChains(self.driver).move_by_offset(x, y).click().perform()
        except:
            deal_exception_with_image(self.driver, self.logger, "move to (" + str(x) + "," + str(y) + ") click error !")

    def exec_javascript(self, js):
        try:
            self.driver.execute_script(js)
        except:
            deal_exception_with_image(self.driver, self.logger, "execute js: %s error !" % js)

    def double_click(self, element, element_name):
        try:
            ac = ActionChains(self.driver)
            ac.double_click(element).perform()
        except:
            deal_exception_with_image(self.driver, self.logger, "double click %s error !" % element_name)

    def move_to_element(self, element, element_name):
        try:
            ac = ActionChains(self.driver)
            ac.move_to_element(element).perform()
        except:
            deal_exception_with_image(self.driver, self.logger, "move to %s error !" % element_name)

    def find_element_wait(self, element_name, *loc):
        try:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            deal_exception_with_image(self.driver, self.logger, "find element: %s error !" % element_name)

    def find_elements_wait(self, element_name, *loc):
        try:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc))
            return self.driver.find_elements(*loc)
        except:
            deal_exception_with_image(self.driver, self.logger, "find element: %s error !" % element_name)

    def send_keys(self, element, key_value, element_name):
        try:
            element.send_keys(key_value)
        except:
            deal_exception_with_image(self.driver, self.logger, "send key to %s error !" % element_name)