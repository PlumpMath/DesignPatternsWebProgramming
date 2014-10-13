'''
Stacy Faude
10-4-14
class-html
'''
import webapp2
from pages import Page #from package inport Class

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #self.response.write('Hello world!')
        p = Page()
        p.title = "My Page"
        p.css = "css/style.css"
        p.body = "This is Stacys Python Example"
        self.response.write(p.print_out())


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
