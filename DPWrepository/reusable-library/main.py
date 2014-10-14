#Stacy Faude
#Design Patters for Web Programming
#10-14-14
#Reusable Library
#

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #movie title
        #year the movie was made
        #director of the film





app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
