"""
@Project: AutoFrameWork_WebTps   
@Description: To local and control patient page elements
@Time:2021/6/7 17:53       
@Author:zexin                
 
"""
from utils.BasePage import BasePage
from utils.ReadYaml import ReadYaml


class PatientPage(BasePage):
    elements_config = ReadYaml("main\\page_data\\patientPage.yaml")

    def input_patient_name(self, patient_name):
        element_name = "patient_name_input"
        patient_name_input = self.find_element_wait(element_name, *self.elements_config[element_name])
        self.send_keys(patient_name_input, patient_name, element_name)

    def click_search_button(self):
        element_name = "search_button"
        search_button = self.find_element_wait(element_name, *self.elements_config[element_name])
        self.click(search_button, element_name)

    def click_select_patient(self):
        element_name = "select_patient"
        select_patient = self.find_element_wait(element_name, *self.elements_config[element_name])
        self.double_click(select_patient, element_name)

    def enter_counter(self):
        element_name = "counter_button"
        counter_button = self.find_elements_wait(element_name, *self.elements_config[element_name])[9]
        self.click(counter_button, element_name)