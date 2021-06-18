"""
@Project: AutoFrameWork_WebTps   
@Description: To structure elements css selector
@Time:2021/6/7 9:28       
@Author:zexin                
 
"""


def structure_selector(*selector_part, num):
    return selector_part[0] + str(num) + selector_part[1]


def structure_selector_by_all(num, selector_part1, selector_part2):
    # print(selector_part1 + str(num) + selector_part2)
    return selector_part1 + str(num) + selector_part2