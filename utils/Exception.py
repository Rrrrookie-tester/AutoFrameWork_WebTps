"""
@Project: AutoFrameWork_WebTps   
@Description: To catch and deal exception
@Time:2021/6/7 9:21       
@Author:zexin                
 
"""

import traceback

from utils.ImageLog import image_log


def deal_exception(logger, detail):
    logger.error(detail)
    logger.error(str(traceback.format_exc()))
    quit()


def deal_exception_with_image(driver, logger, detail):
    image_name = detail.replace(' ', '_')
    driver.get_screenshot_as_file(image_log(image_name.rstrip('_!')))
    logger.error(detail)
    logger.error(str(traceback.format_exc()))
    driver.close()
    quit()
