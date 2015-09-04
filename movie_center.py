import fresh_tomatoes
import media

batman_begins = media.Movie("Batman Begins", "Batman Origin", 
						"http://www.gstatic.com/tv/thumb/movieposters/35903/p35903_p_v7_ae.jpg",
						"https://www.youtube.com/watch?v=neY2xVmOfUM")

dark_knight = media.Movie("The Dark Knight", "Batman vs Joker", 
						"http://www.gstatic.com/tv/thumb/movieposters/173378/p173378_p_v7_aa.jpg",
						"https://www.youtube.com/watch?v=EXeTwQWrcwY")

dark_knight_rises = media.Movie("The Dark Knight Rises", "The Legend Ends.", 
						"http://t1.gstatic.com/images?q=tbn:ANd9GcQSGF8_VbDqKF0B_4IQ0NF87VMDSy7_MPKryawR-qLnSIPQwo5z",
						"https://www.youtube.com/watch?v=GokKUqLcvD8")

bvs = media.Movie("Batman v Superman", "Batman fights superman.", 
						"http://t0.gstatic.com/images?q=tbn:ANd9GcSb0Y7-yhSfUlu85u2RcdZArCg6UYCxkNsOducy4f-RMHD9fdkl",
						"https://www.youtube.com/watch?v=0WWzgGyAH6Y")

suicide_squad = media.Movie("Suicide Squad", "Justice has a bad side.", 
						"http://i.movie.as/p/239142.jpg",
						"https://www.youtube.com/watch?v=PLLQK9la6Go")

deadpool = media.Movie("Deadpool", "The superhero with the big mouth.", 
						"http://t3.gstatic.com/images?q=tbn:ANd9GcRqKdJr4TiPGzX0UyvDJJoLKluBu_GnqGNltp1GM_Cum7lY6Ege",
						"https://www.youtube.com/watch?v=M_5twa6PH9k")


#print(batman_begins.storyline)
#batman_begins.show_trailer()

movies = [batman_begins, dark_knight, dark_knight_rises, bvs, suicide_squad, deadpool]
fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.__doc__)