"""
Contains only a class - Movie.
See entertainment_center module for usage.
"""

class Movie():
    """Class to create movie instances."""
    
    # Constructor
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        """
        Create and initialize Movie class instance
        """
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url