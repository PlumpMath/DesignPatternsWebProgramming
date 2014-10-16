# Stacy Faude
#10-14-14
# Design Patters for Web Programming
#Reusable Library

import webapp2
#from form input form data
from library import Order
from form import OrderSandwich
from receipt import Receipt


class MainHandler(webapp2.RequestHandler):
    def get(self):
        order1 = Order()

        form = OrderSandwich()

        #page for receipt

        r = Receipt()

        self.response.write(form.print_out())
        self.response.write(r.print_out())

#Dont Touch This
app = webapp2.WSGIApplication([
  ('/', MainHandler)
], debug=True)
