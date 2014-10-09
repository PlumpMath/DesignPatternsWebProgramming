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
            <label>Name: </label><input type="text" name="user" />
            <label>Email: </label><input type="text" name="email" />
            <input type="submit" value="Submit" />
        </form>
    </body>
</html>'''

        #self.request.GET
        #print "hello there"
        print self.request.GET['user']
        self.response.write(page) #printing the info out to the page
        #code goes here


#never tough this
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
