import webbrowser

class Movie():
    """This class provides a way to store movie related information."""
    
    # constructor
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        # types of related information:
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    
    # show_trailer opens up the film's trailer.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
        

