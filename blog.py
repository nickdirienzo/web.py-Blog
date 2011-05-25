#Author: Nick DiRienzo
#Began On: 05.22.2011
import web, os, datetime
from datetime import date

urls = ('/', 'index', '/blog', 'blog')
render = web.template.render('templates')
app = web.application(urls, globals())

class index: #This will become a landing page eventually
	def GET(self):
		return render.index(self)
		
class blog:
	def GET(self):
		postsFile = open(os.getcwd()+'/posts', 'r')
		
		postsFromFile = []
		for post in postsFile: #reads posts file
			postsFromFile.append(post)
			
		postTitles = []
		for i in xrange(0, len(postsFromFile), 3): #gets post titles
			postTitles.append(postsFromFile[i].rstrip().upper())
			
		postDates = []
		for i in xrange(1, len(postsFromFile), 3): #gets post dates
			postDate = date.fromtimestamp(float(postsFromFile[i]))
			postDates.append(self.getMonthName(postDate.month) + ' ' + str(postDate.day) + ', ' + str(postDate.year))
			
		postContents = []
		for i in xrange(2, len(postsFromFile), 3): #gets the content of each post
			postsFromFile[i] = postsFromFile[i].replace('\\n', '<br /><br />') #converts "newlines" to two HTML breaks
			postContents.append(postsFromFile[i])
			
		postId = web.input(id=None)
		if postId.id == None:
			return render.blog(postTitles, postDates, postContents, None)
		elif int(postId.id) >= 0:
			return render.blog(postTitles, postDates, postContents, int(postId.id))
		
		
	#Converts number of month to name of month
	def getMonthName(self, monthNum):
		months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
		'August', 'September', 'October', 'November', 'December']
		return months[monthNum-1]
	
if __name__ == '__main__':
	app.run()
