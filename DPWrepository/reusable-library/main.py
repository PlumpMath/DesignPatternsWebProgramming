#Stacy Faude
#Design Patters for Web Programming
#10-14-14
#Reusable Library
#

import webapp2
from library import MovieData

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #movie title
        #year the movie was made
        #director of the film
        md1 = MovieData()
        md1.title = "The Princess Bride"
        md1.year = 1989 #this is actually calling a function
        md1.director = "Rob Reiner"





app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
