"""
@Project: AutoFrameWork_WebTps   
@Description: To test auto segmentation
@Time:2021/6/8 10:13       
@Author:zexin                
 
"""
from time import sleep

import pytest
from selenium import webdriver

from main.workflow.autoSegmentation import autoSegmentation, switch_series, example_series
from main.workflow.login import login
from main.workflow.paWorkflow import enter_counter


class TestAutoSegmentation:

    @pytest.mark.parametrize('series_num', range(1, 16))
    def test_chest_auto_segmentation(self, series_num):
        driver = webdriver.Chrome(r'D:\chromedriver\chromedriver_win32\chromedriver.exe')
        username = 'xzx'
        password = '1q2w3E*'
        patient_name = "AutoTest_Chest_AutoSegmentation"
        part_num = 2   # 4为胸腔
        login(driver, username, password)
        enter_counter(driver, patient_name)
        sleep(20)
        switch_series(driver, series_num)
        autoSegmentation(driver, part_num)

    @pytest.mark.parametrize('series_num', range(1, 16))
    def test_rectum_auto_segmentation(self, series_num):
        driver = webdriver.Chrome(r'D:\chromedriver\chromedriver_win32\chromedriver.exe')
        username = 'xzx'
        password = '1q2w3E*'
        patient_name = "AutoTest_Rectum_AutoSegmentation"
        part_num = 4  # 4为胸腔
        login(driver, username, password)
        enter_counter(driver, patient_name)
        sleep(20)
        switch_series(driver, series_num)
        autoSegmentation(driver, part_num)


if __name__ == '__main__':
    pytest.main(['-s', 'test_autosegmentation.py'])