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

        else:
            self.__year = y