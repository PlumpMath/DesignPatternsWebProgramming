'''
Stacy Faude
10-8-14
Design Patterns for Web Programming
Simple Form
'''
import webapp2 #use the webapp2 library

class MainHandler(webapp2.RequestHandler):#declaring a class
    def get(self): #function that starts everything. Catalyst
        page_head = '''<!DOCTYPE HTML>
<html>
    <head>
        <title>Stacy Faude | Simple Login</title>
    </head>
    <body>'''


        page_body = '''<form method ="GET">
            <label>Name: </label><input type="text" name="user" />
            <label>Email: </label><input type="text" name="email" />
            <input type="submit" value="Submit" />'''
        page_close = '''
        </form>
    </body>
</html>'''

        if self.request.GET:
            #stores info we got from the form
            user = self.request.GET['user']
            email = self.request.GET['email']
            self.response.write(page_head + user + ' ' + email + page_body + page_close)
        else:
            self.response.write(page_head + page_body + page_close) #print

        #self.response.write(page) #printing the info out to the page



#never tough this
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
