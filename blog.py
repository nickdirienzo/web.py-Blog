#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
from web import form

from postscontroller import Posts_Controller
from blogpost import Blog_Post

urls = (
    '/', 'index', 
    '/blog', 'blog', 
    '/blog/new', 'new_post'
)
render = web.template.render('templates', base='base')
app = web.application(urls, globals())
Posts_Controller = Posts_Controller()

class index: #This will become a landing page eventually
    def GET(self):
        return render.index(self)
        
class blog:
        
    def GET(self):
        posts = Posts_Controller.get_posts()
        postId = web.input(id=None)
        if postId.id == None:
            return render.blog(posts, None)
        elif int(postId.id) >= 0:
            return render.blog(posts, int(postId.id))
        
class new_post:
    
    new_post_form = form.Form(
        form.Textbox('title', description='Title: ', size=25), 
        form.Textarea('content', description='Content: ', rows=30, cols=50), 
        form.Button('Submit Post')
    )

    def GET(self):
        new_post_form = self.new_post_form()
        return render.new_post(new_post_form)
        
    def POST(self):
        new_post_form = self.new_post_form()
        if not new_post_form.validates():
            return render.new_post(new_post_form)
        else:
            Posts_Controller.add_post(Blog_Post(new_post_form.d.title, new_post_form.d.content))
            return render.new_post(None)
            
if __name__ == '__main__':
    app.run()
