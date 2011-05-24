#Build: 05.22.2011.0
import web, os
from datetime import date

urls = ('/', 'index', '/blog', 'blog')
render = web.template.render('templates')
app = web.application(urls, globals())

class index:
	def GET(self):
		return render.index(self)
		
class blog:
	def GET(self):
		postsFile = open(os.getcwd()+'/posts', 'r')
		
		postsFromFile = []
		for post in postsFile:
			postsFromFile.append(post)
			
		postTitles = []
		for i in xrange(0, len(postsFromFile), 3):
			postTitles.append(postsFromFile[i])
			
		postDates = []
		for i in xrange(1, len(postsFromFile), 3):
			postDate = date.fromtimestamp(float(postsFromFile[i]))
			postDates.append(str(postDate.month) + ' ' + str(postDate.day) + ' ' + str(postDate.year))
			
		postContents = []
		for i in xrange(2, len(postsFromFile), 3):
			postContents.append(postsFromFile[i])
		
		print "Post Titles: " + str(len(postTitles)) + " Dates: " + str(len(postDates)) + " Content: " + str(len(postContents))
		return render.blog(postTitles, postDates, postContents)
		
	def getMonthName(monthNum):
		if monthNum == 1:
			return 'January'
		elif monthNum == 2:
			return 'February'
if __name__ == '__main__':
	app.run()
