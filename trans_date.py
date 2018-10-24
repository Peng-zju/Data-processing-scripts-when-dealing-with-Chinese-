# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 13:39:20 2018

@author: yipeng
"""

import pandas as pd
import re

class to_date:
    def Trans_date(date):
        '''
        二O一四年五月十六日 转化为 2014/5/16
        '''
        date_dict = {"一": "1", "二": "2", "三": "3", "四": "4", "五": "5",
                     "六": "6", "七": "7", "八": "8", "九": "9", "十": "10",
                     "十一": "11", "十二": "12", "十三": "13", "十四": "14", "十五": "15",
                     "十六": "16", "十七": "17", "十八": "18", "十九": "19", "二十": "20",
                     "二十一": "21", "二十二": "22", "二十三": "23", "二十四": "24", "二十五": "25",
                     "二十六": "26", "二十七": "27", "二十八": "28", "二十九": "29", "三十": "30","三十一": "31"}
        year = (date_dict[date[3]])
        pat_month = re.compile('年.+?月')
        month = (date_dict[pat_month.findall(date)[0][1:-1]])
        pat_day = re.compile('月.+?日')
        day = (date_dict[pat_day.findall(date)[0][1:-1]])
        return('201'+year+'/'+month+'/'+day)
        
