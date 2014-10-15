#Stacy Faude
#10-14-14
# Design Patters for Web Programming
#Reusable Library

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
