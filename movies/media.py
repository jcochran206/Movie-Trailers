import webbrowser #module needed to open website

#class that provides ratings, title, storyline, poster image, and trailer
class Movie():
    # the movie class creats the movie object for the entertinment script
    VALID_RATINGS = ["G","PG","PG-13","R"]
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        #the constructur calls its self and provides a title, poster image, trailer 
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        # this function opens the url for the trailer from Youtube
        webbrowser.open(self.trailer_youtube_url)

        
