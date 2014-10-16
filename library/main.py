#Stacy Faude
#10-14-14
# Design Patters for Web Programming
#Reusable Library

import webapp2
#from form input form data
from form import OrderSandwich
from receipt import Receipt

class MainHandler(webapp2.RequestHandler):
    def get(self):

    form = OrderSandwich()

    self.response.write(OrderSandwich.print_out())

#Dont Touch This
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
