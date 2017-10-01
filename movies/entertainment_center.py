import fresh_tomatoes
import media

"""this python script provides the movie objects that are called by the script to provide the user with selected movies"""

#favorite movies instances
toy_story = media.Movie("Toy Story",
                        "A story of a boy and toys come to life",
                        "http://files.doobybrain.com/wp-content/uploads/2009/10/toy-story-3-jessie-poster1.jpg",
                        "https://www.youtube.com/watch?v=JcpWXaA2qeg")


#avatar object
avatar = media.Movie("Avatar",
                     "A marine goes to alien planet",
                     "https://www.movieposter.com/posters/archive/main/105/MPW-52799",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

#battle for LA object
battle_la = media.Movie("Battle Los Anagels",
                        "A squadron of U.S. Marines becomes the last line of defense against a global invasion",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMDg2NzQwOGMtMGRkNC00YjAwLTg4NjgtZWQwYzljZmM1YzA4XkEyXkFqcGdeQXVyNTIzOTk5ODM@._V1_UX182_CR0,0,182,268_AL_.jpg",
                        "https://www.youtube.com/watch?v=ORb3zC8z94w")

#star wars object 
star_wars_last_jedi = media.Movie("Star Wars Last Jedi",
                    "Episode VIII focuses on Rey finding Luke Skywalker",
                    "https://pbs.twimg.com/media/C9YRt1SXkAEYN-k.jpg:large",
                    "https://www.youtube.com/watch?v=VZSKN312BXw")

#lone survivor instance 
lone_survivor = media.Movie("Lone Survivor",
              "Marcus Luttrell and his team set out on a mission to capture or kill notorious Taliban leader Ahmad Shah",
              "https://img.exs.lv/movies/large/4/5/lone-survivor-poster.jpg",
              "https://www.youtube.com/watch?v=yoLFk4JK_RM")

#american sniper instance 
american_sniper = media.Movie("American Sniper",
                "Navy S.E.A.L. sniper Chris Kyle's pinpoint accuracy saves countless lives on the battlefield and turns him into a legend.",
                "http://www.filmofilia.com/wp-content/uploads/2014/10/american-sniper-poster.jpg",
                "https://www.youtube.com/watch?v=99k3u9ay1gs")

#transformers instance
transformers_last_knight = media.Movie("Transformers: The Last Knight",
                                       "Humans are at war with the Transformers, and Optimus Prime is gone.",
                                       "https://pbs.twimg.com/media/DBk3OlmXoAMh3ox.jpg",
                                       "https://www.youtube.com/watch?v=AntcyqJ6brc")

#dark tower instance
dark_tower = media.Movie("Dark Tower",
                         "the last Gunslinger, is locked in an eternal battle with Walter O'Dim, also known as the Man in Black.",
                         "http://nerdist.com/wp-content/uploads/2017/02/The-Dark-Tower-Poster-Idris-Elba.jpeg",
                         "https://www.youtube.com/watch?v=GjwfqXTebIY")

#array of movies in format for fresh tomatoes to consume
movies = [toy_story, avatar, battle_la, star_wars_last_jedi, lone_survivor, american_sniper, transformers_last_knight, dark_tower]

fresh_tomatoes.open_movies_page(movies)


