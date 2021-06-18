"""
@Project: AutoFrameWork_WebTps   
@Description: To local and control counter page elements
@Time:2021/6/8 9:37       
@Author:zexin                
 
"""
from utils.BasePage import BasePage
from utils.ReadYaml import ReadYaml
from utils.StructureSelector import structure_selector_by_all


class CounterPage(BasePage):
    elements_config = ReadYaml("main\\page_data\\counterPage.yaml")

    def autosegmentation_button(self, btn_num):
        element_name = "autosegmentation_button"
        autosegmentation_button = self.find_elements_wait(element_name, *self.elements_config['operate_button'])[btn_num]
        self.click(autosegmentation_button, element_name)

    def result_promte_button(self):
        element_name = "result_promte_button"
        result_promte_button = self.find_element_wait(element_name, *self.elements_config[element_name])
        self.click(result_promte_button, element_name)

    def series_button(self, num):
        element_name = "series_button"
        selector = structure_selector_by_all(num, self.elements_config[element_name][1], self.elements_config[element_name][2])
        series_button = self.find_element(element_name, self.elements_config[element_name][0], selector)
        self.double_click(series_button, element_name)

    def example_series(self):
        element_name = "example_series"
        series_button = self.find_element(element_name, *self.elements_config[element_name])
        self.double_click(series_button, element_name)