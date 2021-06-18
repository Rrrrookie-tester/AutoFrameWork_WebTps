"""
@Project: AutoFrameWork_WebTps   
@Description: To test enter counter
@Time:2021/6/7 19:57       
@Author:zexin                
 
"""
from time import sleep

import pytest
from selenium import webdriver

from main.workflow.login import login
from main.workflow.paWorkflow import enter_counter


class TestLogin:

    @pytest.mark.parametrize('execute_num', range(1, 6))
    def test_enter_counter(self, execute_num):
        driver = webdriver.Chrome(r'D:\chromedriver\chromedriver_win32\chromedriver.exe')
        username = 'xzx'
        password = '1q2w3E*'
        patient_name = "阿童木"
        login(driver, username, password)
        enter_counter(driver, patient_name)


if __name__ == '__main__':
    pytest.main(['-s', 'test_enter_counter.py'])
