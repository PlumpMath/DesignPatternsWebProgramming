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


        page_body = '''
        <a href="?email=stacy@istacy.com&user=Stacy">Stacy</a><br/>
        <a href="?email=matthew@istacy.com&user=Matthew">Matthew</a><br/>
        <a href="?email=tyler@istacy.com&user=Tyler">Tyler</a><br/>
        <a href="?email=canon@istacy.com&user=Canon">Canon</a><br/>
        '''
        page_close = '''
        </form>
    </body>
</html>'''

        if self.request.GET:
            #stores info we got from the form
            user = self.request.GET['user']
            email = self.request.GET['email']
            self.response.write(page_head + user + ' ' + email + page_close)
        else:
            self.response.write(page_head + page_body + page_close) #print

        #self.response.write(page) #printing the info out to the page



#never tough this
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
