# Stacy Faude
#10-14-14
# Design Patters for Web Programming
#Reusable Library

import webapp2
#from form input form data
from library import Order


class MainHandler(webapp2.RequestHandler):
    def get(self):
        order1 = Order()

        self.response.write(order1)

#Dont Touch This
app = webapp2.WSGIApplication([
  ('/', MainHandler)
], debug=True)
