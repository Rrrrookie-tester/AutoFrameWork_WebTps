"""
@Project: AutoFrameWork_WebTps   
@Description: To get data from .yaml
@Time:2021/6/7 9:25       
@Author:zexin                
 
"""
import os

import yaml


def ReadYaml(yaml_dic_name):
    current_path = os.path.dirname(os.path.realpath(__file__))
    yaml_path = os.path.join(os.path.abspath(os.path.join(current_path, "..")), yaml_dic_name)
    f = open(yaml_path, 'r', encoding='utf-8',  errors='ignore')
    data = yaml.load(f.read())
    return data