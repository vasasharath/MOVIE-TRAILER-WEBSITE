import webbrowser  # importing webbrowser package which will help to open the
# youtube url of the specific movie


class Movie():
    """ This is a Movie class whiich contains the necessary attributes
        and methods that each movie should have in order to work the
        website as we think"""
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):  # defining list of parameters in the init
        # method that each movie should have

        self.title = movie_title   # initializing each property with respective
        # attribute
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)  # This will open the
        # specified url in a browser
