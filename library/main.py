#Stacy Faude
#10-14-14
# Design Patters for Web Programming
#Reusable Library

import webapp2
#from form input form data
from form import OrderSandwich
from receipt import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):

    f = form()



#Dont Touch This
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
