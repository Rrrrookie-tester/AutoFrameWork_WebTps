"""
@Project: AutoFrameWork_WebTps   
@Description: Patient page workflow
@Time:2021/6/7 19:50       
@Author:zexin                
 
"""
from selenium import webdriver

from main.page_elements.patientPage import PatientPage


def enter_counter(driver, patient_name):
    patient_page = PatientPage(driver)
    patient_page.input_patient_name(patient_name)
    patient_page.click_search_button()
    patient_page.click_select_patient()
    patient_page.enter_counter()
