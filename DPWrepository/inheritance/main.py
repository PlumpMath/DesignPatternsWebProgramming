
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        self.response.write(p.print_out())

class Page(object): #borrowing stuff from the object class
    def __init__(self):
        self._head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title></title>
    </head>
    <body>'''
        self._body = 'content'
        self._close = '''
    </body>
</html>'''

    def print_out(self):
        return self._head + self._body + self._close

class FormPage(Page):
    def __init__(self):
        #constructor function for the super class
        super(FormPage, self).__init__() # or Page.__init__()
        self._form_open = '<form method="GET">'
        self._form_close = '</form>'
        #<label>First Name</label><input type="text" value="" name="first_name" placeholder="first name"/>
        #<label>Last Name</label><input type="text" value="" name="last_name" placeholder="first name"/>
        #<input type="submit" value="submit" />

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
