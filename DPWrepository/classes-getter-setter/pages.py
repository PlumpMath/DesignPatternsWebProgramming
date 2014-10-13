
class Page(object):
    def __init__(self):
        self.__title = "Welcome"
        self.__css = "css/style.css"
        self.head = """

<!DOCTYPE HTML>
<html>
    <head>
        <title>{self.title}</title>
        <link href="{self.css}" rel="stylesheet" type="text/css" />
    </head>
    <body>
        """

        self.body = "Welcome to my OOP Python Page"
        self.close = """

    </body>
</html>
    """

    def print_out(self):
        all = self.head + self.body + self.close
        all = all.format(**locals())
        return all

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, new_title):
        self.__title = new_title

    @property
    def css(self):
        return self.__css

    @css.setter
    def css(self, new_css_file):
        self.__css = new_css_file