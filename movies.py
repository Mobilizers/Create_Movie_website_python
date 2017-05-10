import webbrowser

# two blank lines before a class name is must
class media():
    """This class provides a way to store movie related information.

    Attributes:
        title: A string to store the title of the movie.
        poster_image_url: A string to store the URL of the movie poster.
        trailer_youtube_url: A string to store the URL of the movie trailer.
        wikipedia: A string to store the URL of wikipedia
        storyline: A string to store the basic plot of the movie.
        release_date: A string to store the release date of the movie.
        cast_crew: A string with all cast names
    """
    def __init__(self, movie_titles,poster_image_url,trailer_youtube_url,
    release_date,cast_crew,movie_storyline):
        """Initialises Movie class instance variables."""
        self = self
        self.titles = movie_titles
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.release_date = release_date
        self.cast_crew = cast_crew
        self.movie_storyline = movie_storyline
    def show_trailer(self):
        """Plays the movie trailer in the web browser."""
        webbrowser.open(self.trailer_url)
#noqa is used to override mistakes
