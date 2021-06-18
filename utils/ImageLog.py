"""
@Project: AutoFrameWork_WebTps   
@Description: To get screenshot when catch error
@Time:2021/6/7 9:21       
@Author:zexin                
 
"""
import os
import time


def image_log(name):
    now_date = time.strftime("%Y_%m_%d_%H%M%S", time.localtime(time.time()))
    log_path = os.path.dirname(os.path.dirname(os.path.abspath('.'))) + '\\log\\errorimg\\'
    # log_name = log_path + "WebTPSTestLog_%s.log" % now_date
    log_name = log_path + name + "_%s.png" % now_date
    return str(log_name)
