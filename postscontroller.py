#!/usr/bin/env python
# -*- coding: utf-8 -*-

from blogpost import Blog_Post
import os

class Posts_Controller:
    
    def __init__(self):
        self.__blog_posts = self.__get_blog_posts()
        
    def __get_blog_posts(self):
        posts_file = open(os.getcwd()+'/posts', 'r')
        
        posts_from_file = posts_file.readlines()
        
        if len(posts_from_file) != 0:
            post_titles = []
            for i in xrange(0, len(posts_from_file), 3): 
                post_titles.append(posts_from_file[i].rstrip())
            
            post_contents = []    
            for i in xrange(1, len(posts_from_file), 3): 
                post_contents.append(posts_from_file[i].rstrip())
                
            post_dates = []
            for i in xrange(2, len(posts_from_file), 3): 
                post_dates.append(posts_from_file[i].rstrip())
                
            blog_posts = []
            for i in xrange(len(post_titles)):
                blog_posts.append(Blog_Post(post_titles[i], post_contents[i], post_dates[i]))
            
        posts_file.close()
        return blog_posts
        
    def add_post(self, Blog_Post):
        posts_file = open(os.getcwd()+'/posts', 'a')
        posts_file.write(str(Blog_Post))
        posts_file.close()
        self.__blog_posts = self.__get_blog_posts()

    def get_posts(self):
        return self.__blog_posts
        
    def del_post(post_id):
        if post_id > 0:
            del self.__blog_posts[post_id - 1]
