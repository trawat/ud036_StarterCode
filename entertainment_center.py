"""
Act as a controller/ starting point in our fresh tomatoes application.
Creates a movie list and passes the same to fresh_tomatoes.open_movies_page 
for integration of movie list with applications HTML content.
"""

import media
import fresh_tomatoes

"""
Static movie data. 
Add movie detail to this list for it to appear in the final HTML content.
"""
movie_data = [["Beauty and the Beast", "https://upload.wikimedia.org/wikipedia/en/d/d6/Beauty_and_the_Beast_2017_poster.jpg", "https://www.youtube.com/watch?v=e3Nl_TCQXuw"],
              ["The Fate of the Furious", "https://upload.wikimedia.org/wikipedia/en/2/2d/The_Fate_of_The_Furious_Theatrical_Poster.jpg", "https://www.youtube.com/watch?v=ZsJz2TJAPjw"],
              ["Despicable Me 3", "https://upload.wikimedia.org/wikipedia/en/9/91/Despicable_Me_3_%282017%29_Teaser_Poster.jpg", "https://www.youtube.com/watch?v=gRDbiX3Zm8c"],
              ["Wolf Warriors 2", "https://upload.wikimedia.org/wikipedia/en/b/b5/Wolf_Warriors_2_poster.jpeg", "https://www.youtube.com/watch?v=fkqGiPB2D8M"],
              ["Logan", "https://upload.wikimedia.org/wikipedia/en/3/37/Logan_2017_poster.jpg", "https://www.youtube.com/watch?v=DekuSxJgpbY"],
              ["Transformers: The Last Knight", "https://upload.wikimedia.org/wikipedia/en/2/26/Transformers_The_Last_Knight_poster.jpg", "https://www.youtube.com/watch?v=sQm3djLYWB8"],]

# list to hold media.Movie instances.
movie_list = []

for movie_item in movie_data:
    movie_record = media.Movie(movie_item[0], movie_item[1], movie_item[2])
    movie_list.append(movie_record)
    

fresh_tomatoes.open_movies_page(movie_list)