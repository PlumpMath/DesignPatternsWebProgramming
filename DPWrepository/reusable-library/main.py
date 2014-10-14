#Stacy Faude
#Design Patters for Web Programming
#10-14-14
#Reusable Library
#

import webapp2
#from library import MovieData
from library import MovieData, FavoriteMovies #Changing what data to import
from ResultsPages import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):

        p = Page()
        lib = FavoriteMovies()

        #movie title
        #year the movie was made
        #director of the film
        md1 = MovieData()
        md1.title = "The Princess Bride"
        md1.year = 1989 #this is actually calling a function
        md1.director = "Rob Reiner"

        md2 = MovieData()
        md2.title = "Dune"
        md2.year = 1986 #this is actually calling a function
        md2.director = "David Lynch"


        self.response.write(p.print_out())



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
