class FavoriteMovies(object):
    def __init__(self):
        self.__movie_list = []
        pass
        #have an array to hold movie info
        #some way to add to the array
        #generate a list of movies at the end
        #calculate the time span between movies

    def addMovie(self, m):
        self.__movie_list.append(m)
        print m.title #check to see if the code is working

    def compileList(self):
        output = ''
        for movie in self.__movie_list: #for statement for each movie in array
            output += 'Title: ' + movie.title + '(' + str(movie.year) + ') Directed by: ' + movie.director + '<br />'
        return output


class MovieData(object): #Data Object
    def __init__(self):
        self.title = ''
        self.__year = 0 #check for valid year
        self.director = ''

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, y):
        if y > 2014: #if the date isnt valid
            print "Error invalid date!"
            self.__year = 2014
        else:
            self.__year = y