import webbrowser

class Movie():
	"""This class provides a way to store information related to movies."""
	#the above documentation can be accessed by using media.Movie.__doc__
	
	VALID_RATINGS = ["G", "PG", "PG13", "R"] #this is a class variable
	#class variables should be upper class according to styleguide.

	def __init__(self, movie_title, movie_storyline, poster_image,
				 trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)