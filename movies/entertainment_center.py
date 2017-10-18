import media  # importing media file which contains the class definition
import fresh_tomatoes  # importing fresh_tomatoes which has page rendering
# information such as code for HTML and CSS code


bahubali2 = media.Movie("Bahubali2",
                        "When Shiva, the son of Bahubali, "
                        "learns about his heritage, he begins "
                        "to look for answers. His story is "
                        "juxtaposed with past events that "
                        "unfolded in the Mahishmati Kingdom.",
                        "https://upload.wikimedia.org/wikipedia/en/f/f9/Baahubali_the_Conclusion.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=G62HrubdD6o")
# creating instance for the class Movie
three_hundred = media.Movie("300",
                            "King Leonidas of Sparta and a force "
                            "of 300 men fight the Persians at Thermopylae "
                            "in 480 B.C.",
                            "https://upload.wikimedia.org/wikipedia/en/5/5c/300poster.jpg",  # NOQA
                            "https://www.youtube.com/watch?v=UrIbxk7idYA")

the_great_wall = media.Movie("The Great Wall",
                             "European mercenaries searching for "
                             "black powder become embroiled in the "
                             "defense of the Great Wall of China "
                             "against a horde of monstrous creatures.",
                             "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Great_Wall_%28film%29.png",  # NOQA
                             "https://www.youtube.com/watch?v=avF6GHyyk5c")

rio = media.Movie("Rio", "When Blu, a domesticated macaw "
                  "from small-town Minnesota, meets the "
                  "fiercely independent Jewel, he takes off "
                  "on an adventure to Rio de Janeiro with "
                  "the bird of his dreams.",
                  "https://upload.wikimedia.org/wikipedia/en/b/bb/Rio2011Poster.jpg",  # NOQA
                  "https://www.youtube.com/watch?v=P1GRO31ve5Q")

home_alone = media.Movie("Home Alone",
                         "An eight year old must protect his "
                         "house from a pair of burglars when "
                         "he is accidentally left home alone "
                         "by his family during Christmas vacation.",
                         "https://upload.wikimedia.org/wikipedia/en/a/ab/HomeAloneCollectionDVD.jpg",  # NOQA
                         "https://www.youtube.com/watch?v=CK2Btk6Ybm0")

curve = media.Movie("Curve",
                    "A young woman becomes trapped in her car "
                    "after a hitchhiker causes her to have an "
                    "automobile accident.",
                    "https://upload.wikimedia.org/wikipedia/en/3/38/Curve_Poster.jpg",  # NOQA
                    "https://www.youtube.com/watch?v=O7bR983B_LI")

movies = [bahubali2, three_hundred, rio,
          home_alone, curve, the_great_wall]  # storing the list of
# instances in an array

fresh_tomatoes.open_movies_page(movies)  # passing the movies array to
# open_movies_page method which has the layout to display as a webpage
