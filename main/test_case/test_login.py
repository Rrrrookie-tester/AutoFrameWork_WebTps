"""
@Project: AutoFrameWork_WebTps   
@Description: To test login
@Time:2021/6/7 14:23       
@Author:zexin                
 
"""
import pytest
from selenium import webdriver

from main.workflow.login import login
from utils.Logger import Logger


# logger = Logger("test_login.py").getlog()
#
#
# @pytest.fixture(autouse=True)
# def func_fixure(request):
#     i = request.param
#     # logger.debug("----test:login;num:%s start----" % i)
#     # yield i
#     # logger.debug("----test:login;num:%s end----" % i)
#     print("第%s次开始" % i)
#     yield i
#     print("第%s次结束" % i)
#
#
# def test_login():
#     username = 'xzx'
#     password = '1q2w3E*'
#     login(username, password)


class TestLogin:

    @pytest.mark.parametrize('execute_num', range(1, 6))
    def test_login(self, execute_num):
        driver = webdriver.Chrome(r'D:\chromedriver\chromedriver_win32\chromedriver.exe')
        username = 'xzx'
        password = '1q2w3E*'
        login(driver, username, password)


if __name__ == '__main__':
    pytest.main(['-s', 'test_login.py'])
