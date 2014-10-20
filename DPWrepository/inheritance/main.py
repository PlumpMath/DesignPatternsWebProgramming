
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage()
        p.inputs = [['first_name', 'text', 'First Name'], ['last_name', 'text', 'Last Name'], ['Submit', 'submit']]
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
        super(FormPage, self).__init__()  # or Page.__init__()
        self._form_open = '<form method="GET">'
        self._form_close = '</form>'
        self.__inputs = []
        self._form_inputs = ''

        #<label>First Name</label><input type="text" value="" name="first_name" placeholder="first name"/>
        #looking for an array as such: ['first_name', 'text', 'First Name']
        #place holder, type, value
        #<label>Last Name</label><input type="text" value="" name="last_name" placeholder="first name"/>
        #<input type="submit" value="Submit" />

    @property
    def inputs(self):
        pass

    @inputs.setter
    def inputs(self, arr):
        #change my private inputs variable
        self.__inputs = arr
        #sort through the mega array and create HTML inputs based on info there
        for item in arr:
            self._form_inputs += '<input type="' + item[1] + '" name="' + item[0]
            #if there is a third item... add it in...
            try:
                self._form_inputs += '"placeholder="'+item[2]+'" />'

            #otherwise ... end the tag
            except:
                self._form_inputs += '" />'

        print self._form_inputs


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
