import fresh_tomatoes
import media


audition = media.Movie(
    "Audition",
    "A man is unlucky in love.",
    "https://upload.wikimedia.org/wikipedia/en/3/32/Audition-1999-poster.jpg",
    "https://www.youtube.com/watch?v=EBQHp2__AVQ"
)

jules_and_jim = media.Movie(
    "Jules et Jim",
    "French people hang out.",
    "https://upload.wikimedia.org/wikipedia/en/2/2e/Jules_et_jim_affiche.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY"
)

eternal_sunshine = media.Movie(
    "Eternal Sunshine of the Spotless Mind",
    "A man wants to forget a past relationship.",
    "https://upload.wikimedia.org/wikipedia/en/6/62/Eternal_sunshine_of_the_spotless_mind_ver3.jpg",
    "https://www.youtube.com/watch?v=yE-f1alkq9I"
)

children_of_men = media.Movie(
    "Children of Men",
    "A future without babies or hope finds a pregnant woman.",
    "file:///Users/tylerbromley/ProgrammingFoundations/Children_of_men_ver4.jpeg",
    "https://www.youtube.com/watch?v=Q9CFcTY_pik"
)

breathless = media.Movie(
    "A Bout de Souffle",
    "A wandering criminal and his American girlfriend.",
    "https://upload.wikimedia.org/wikipedia/en/3/3f/%C3%80_bout_de_souffle_%28movie_poster%29.jpg",
    "https://www.youtube.com/watch?v=bJFFy3soy9Y"
)

lost_in_translation = media.Movie(
    "Lost In Translation",
    "A bored woman in Tokyo meets an bored "
    "older gentleman.",
    "https://upload.wikimedia.org/wikipedia/en/4/4c/Lost_in_Translation_poster.jpg",
    "https://www.youtube.com/watch?v=W6iVPCRflQM"
)


movies = [
            audition,
            jules_and_jim,
            eternal_sunshine,
            children_of_men,
            breathless,
            lost_in_translation,
]

fresh_tomatoes.open_movies_page(movies)
