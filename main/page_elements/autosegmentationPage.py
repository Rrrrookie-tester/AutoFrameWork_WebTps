"""
@Project: AutoFrameWork_WebTps   
@Description: To local and control auto segmentation page elements
@Time:2021/6/8 9:44       
@Author:zexin                
 
"""
from utils.BasePage import BasePage
from utils.ReadYaml import ReadYaml
from utils.StructureSelector import structure_selector_by_all


class AutoSegmentationPage(BasePage):
    elements_config = ReadYaml("main\\page_data\\autosegmentationPage.yaml")

    def auto_part_button(self, part_num):
        element_name = "auto_part_button"
        selector = structure_selector_by_all(part_num, self.elements_config[element_name][1], self.elements_config[element_name][2])
        auto_part_button = self.find_element_wait(element_name, self.elements_config[element_name][0], selector)
        self.click(auto_part_button, element_name)

    def all_select_button(self):
        element_name = "all_select_button"
        all_select_button = self.find_element(element_name, *self.elements_config[element_name])
        self.click(all_select_button, element_name)

    def move_button(self):
        element_name = "move_button"
        move_button = self.find_element_wait(element_name, *self.elements_config[element_name])
        self.click(move_button, element_name)

    def auto_submit_button(self):
        element_name = "auto_submit_button"
        auto_submit_button = self.find_element_wait(element_name, *self.elements_config[element_name])
        self.click(auto_submit_button, element_name)

