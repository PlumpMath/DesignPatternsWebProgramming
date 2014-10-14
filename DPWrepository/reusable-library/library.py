class MovieData(object): #Data Object
    def __init__(self):
        self.title = ''
        self.__year = 0 #check for valid year
        self.director = ''

        