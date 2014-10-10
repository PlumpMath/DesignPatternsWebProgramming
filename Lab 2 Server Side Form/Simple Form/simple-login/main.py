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
        <title>Stacy Faude | Simple Form</title>
        <link href="css/styles.css" rel="stylesheet" type="text/css">
    </head>
    <body>'''


        page_body = '''<form method ="GET">
        <h1>Order your sandwich</h1>
        <hr>
            <label>Name: </label><input type="text" name="user" /><br/>
            <label>Email: </label><input type="text" name="email" /><br/>
            <input type="checkbox" name="bread" value="white" /> White<br/>
            <input type="checkbox" name="bread" value="wheat" /> Wheat<br/>
            <input type="checkbox" name="bread" value="flatbread" /> Flat Bread<br/>
            <p>Select Sandwich</p>
            <select name="sandwich">
                <option value="Pompeii">Pompeii</option>
                <option value="Titan">Titan</option>
                <option value="Erupter">Spartan</option>
                <option value="Erupter">Spartan</option>
                <option value="Quatro">Quatro</option>
                <option value="Apollo">Apollo</option>
            </select>
            <p>Soup of the Day?</p>
            <select name="soup">
                <option value="yes">Yes</option>
                <option value="no">No</option>
            </select>
            <p>Chips</p>
             <select name="chips">
                <option value="yes">Yes</option>
                <option value="no">No</option>
            </select>
            <br/>
            <input type="submit" value="Submit" />'''
        page_close = '''
        </form>
    </body>
</html>'''

        if self.request.GET:
            #stores info we got from the form
            user = self.request.GET['user']
            email = self.request.GET['email']
            bread = self.request.GET['bread']
            sandwich = self.request.GET['sandwich']
            soup = self.request.GET['soup']
            chips = self.request.GET['chips']
            self.response.write(page_head + user + ' ' + email + ' ' + bread + ' ' + sandwich + ' ' + soup + ' ' + chips + page_close)
        else:
            self.response.write(page_head + page_body + page_close) #print

        #self.response.write(page) #printing the info out to the page



#never tough this
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
