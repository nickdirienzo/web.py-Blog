#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from datetime import date

class Blog_Post:
    
    def __init__(self, title, content, date_posted = None):
        self.__title = title
        self.__content = self.__modify_content(content)
        
        if date_posted == None:
			self.__date = self.__date_posted()
        else:
            self.__date = date_posted
		
	self.title = self.__title
	self.content = self.__content
	self.date = self.__date
        
    def __str__(self):
        return str(self.__title + '\n' + self.__content + '\n' + self.__date + '\n')
        
    def __date_posted(self):
        post_date = date.fromtimestamp(time.time())
        return self.__get_month_name(post_date.month) + ' ' + str(post_date.day) + ', ' + str(post_date.year)
        
    def __modify_content(self, content):
        return content.replace('\n', '<br />')
        
    def __get_month_name(self, month_num):
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        return months[month_num-1]
