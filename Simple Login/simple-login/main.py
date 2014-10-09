'''
Stacy Faude
10-8-14
Design Patterns for Web Programming
Simple Form
'''
import webapp2 #use the webapp2 library

class MainHandler(webapp2.RequestHandler):#declaring a class
    def get(self): #function that starts everything. Catalyst
        page = '''<!DOCTYPE HTML>
<html>
    <head>
        <title>Stacy Faude | Simple Login</title>
    </head>
    <body>
        <form method ="GET">
            <label>Name: </label><input type="text" />
            <label>Email: </label><input type="text" />
        </form>
    </body>
</html>'''
        self.response.write(page)
        #code goes here


#never tough this
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
