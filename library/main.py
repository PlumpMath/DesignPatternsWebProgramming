#Stacy Faude
#10-14-14
# Design Patters for Web Programming
#Reusable Library

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
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
            <label>Phone: </label><input type="text" name="phone" /><br/>
            <p>Type of Bread?</p>
            <input type="checkbox" name="bread" value="white" /> White<br/>
            <input type="checkbox" name="bread" value="wheat" /> Wheat<br/>
            <input type="checkbox" name="bread" value="flatbread" /> Flat Bread<br/>
            <p>Select Sandwich</p>
            <select name="sandwich">
                <option value="Pompeii">Pompeii</option>
                <option value="Titan">Titan</option>
                <option value="Erupter">Erupter</option>
                <option value="Spartan">Spartan</option>
                <option value="Quatro">Quatro</option>
                <option value="Apollo">Apollo</option>
            </select>
            <p>Quantity</p>
            <input type="number" name="quantity" min="1" max="20" />
            <p>Chips?</p>
             <input type="radio" name="chips" value="yes">yes
             <input type="radio" name="chips" value="no">no
            <br/>
            <input type="submit" value="Submit" />'''
        page_close = '''
        </form>
    </body>
</html>'''

        if self.request.GET:
            #stores info we got from the form
            user = self.request.GET['user']
            phone = self.request.GET['phone']
            bread = self.request.GET['bread']
            sandwich = self.request.GET['sandwich']
            quantity = self.request.GET['quantity']
            chips = self.request.GET['chips']
            self.response.write(page_head + user + ' ' + phone + ' ' + bread + ' ' + quantity + ' ' + sandwich + ' ' + ' ' + chips + page_close)
        else:
            self.response.write(page_head + page_body + page_close) #print

        #self.response.write(page) #printing the info out to the page


#Dont Touch This
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
