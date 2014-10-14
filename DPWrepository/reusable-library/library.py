class FavoriteMovies(object):
    def __init__(self):
        self.__movie_list = []
        pass
        #have an array to hold movie info
        #some way to add to the array
        #generate a list of movies at the end
        #calculate the time span between movies

    def add_movie(self, m):
        self.__movie_list.append(m)
        #print m.title #check to see if the code is working
        #<movie data object>

    def compile_list(self):
        output = ''
        for movie in self.__movie_list: #for statement for each movie in array
            output += 'Title: ' + movie.title + '(' + str(movie.year) + ') Directed by: ' + movie.director + '<br />'
        return output

    #adding an utility function
    def calc_time_span(self):
        '''
        calculate the time between movies
        '''
        #years
        #create a years array
        years = []
        for movie in self.__movie_list:
            years.append(movie.year)

        print years
        #sort years from low to high
        years.sort()

        #subtract the low year from the high year
        num = len(years) - 1
        span = years [num] - years[0] #last number - first number

        #return the span
        return 'The span between films is ' + str(span)

    @property
    def movie_list(self):
        return self.__movie_list


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