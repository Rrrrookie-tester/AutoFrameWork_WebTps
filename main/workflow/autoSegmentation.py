"""
@Project: AutoFrameWork_WebTps   
@Description: auto segmentation workflow
@Time:2021/6/8 9:51       
@Author:zexin                
 
"""
from time import sleep

from main.page_elements.autosegmentationPage import AutoSegmentationPage
from main.page_elements.counterPage import CounterPage
from main.page_elements.patientPage import PatientPage


def autoSegmentation(driver, part_num):
    counter_page = CounterPage(driver)
    counter_page.autosegmentation_button(5)
    autoSegmentation_page = AutoSegmentationPage(driver)
    autoSegmentation_page.auto_part_button(part_num)
    sleep(3)
    autoSegmentation_page.all_select_button()
    autoSegmentation_page.move_button()
    sleep(3)
    # ----选中外轮廓-----
    autoSegmentation_page.auto_part_button(part_num=4)
    sleep(3)
    autoSegmentation_page.all_select_button()
    autoSegmentation_page.move_button()
    # ----选中外轮廓-----
    autoSegmentation_page.auto_submit_button()
    sleep(90)  # 自动分割等待时间

    counter_page.close()


def switch_series(driver, series_num):
    counter_page = CounterPage(driver)
    counter_page.series_button(series_num)
    sleep(10)


def example_series(driver):
    counter_page = CounterPage(driver)
    counter_page.example_series()
    sleep(10)
