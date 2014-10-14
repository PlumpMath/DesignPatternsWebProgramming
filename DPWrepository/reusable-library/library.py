class FavoriteMovies(object):
    def __init__(self):
        self.__movie_list = []
        pass
        #have an array to hold movie info
        #some way to add to the array
        #generate a list of movies at the end
        #calculate the time span between movies



class MovieData(object): #Data Object
    def __init__(self):
        self.title = ''
        self.__year = 0 #check for valid year
        self.director = ''

    @property
    def year(self):
        pass

    @year.setter
    def year(self, y):
        if y > 2014: #if the date isnt valid
            print "Error invalid date!"
            self.__year = 2014
        else:
            self.__year = y