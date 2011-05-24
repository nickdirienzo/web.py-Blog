#Author: Nick DiRienzo
#Began On: 05.22.2011
import web, os
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
			postTitles.append(postsFromFile[i])
			
		postDates = []
		for i in xrange(1, len(postsFromFile), 3): #gets post dates
			postDate = date.fromtimestamp(float(postsFromFile[i]))
			postDates.append(self.getMonthName(postDate.month) + ' ' + str(postDate.day) + ', ' + str(postDate.year))
			
		postContents = []
		for i in xrange(2, len(postsFromFile), 3): #gets the content of each post
			postsFromFile[i] = postsFromFile[i].replace('\\n', '<br /><br />') #converts "newlines" to two HTML breaks
			postContents.append(postsFromFile[i])
		
		return render.blog(postTitles, postDates, postContents)
		
	#Converts number of month to name of month
	def getMonthName(self, monthNum):
		if monthNum == 1:
			return 'January'
		elif monthNum == 2:
			return 'February'
		elif monthNum == 3:
			return 'March'
		elif monthNum == 4:
			return 'April'
		elif monthNum == 5:
			return 'May'
		elif monthNum == 6:
			return 'June'
		elif monthNum == 7:
			return 'July'
		elif monthNum == 8:
			return 'August'
		elif monthNum == 9:
			return 'September'
		elif monthNum == 10:
			return 'October'
		elif monthNum == 11:
			return 'November'
		elif monthNum == 12:
			return 'December'
		else:
			return 'Invalid Month'
		
if __name__ == '__main__':
	app.run()
