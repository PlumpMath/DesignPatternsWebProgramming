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
        lib.add_movie(md1)

        md2 = MovieData()
        md2.title = "Dune"
        md2.year = 1986 #this is actually calling a function
        md2.director = "David Lynch"
        lib.add_movie(md2)

        md3 = MovieData()
        md3.title = "Star Wars"
        md3.year = 1977 #this is actually calling a function
        md3.director = "George Lucas"
        lib.add_movie(md3)

        #lib.movie_list = [md1, md2] you could do this if it was public

        lib.calc_time_span()
        p.body = lib.compile_list() #change the body before it prints it out - lib.compile list is outputting the string and going it the atribute we have in that class - now the html code will show

        self.response.write(p.print_out())



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
