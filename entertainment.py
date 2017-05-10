import movies
import fresh_tomatoes

""" importing movies.py and fresh_tomatoes.py to access class variables"""
# things important in this are 79 character limit per line, add one space after every block of code

guardians = movies.media(
    "Guardians of Galaxy 2",
    "https://www.technobuffalo.com/wp-content/uploads/2017/03/guardians-of-the-galaxy-vol-2-posters-003-200x200.jpg",
    "https://www.youtu.be/dW1BIid8Osg",
    "May 5, 2017",
    "Chris Pratt, Zoe Saldana, Elizabeth Debicki, Bradley Cooper, Karen Gillan, Vin Diesel, Dave Bautista, Kurt Russell, Nathan Fillion, Tommy Flanagan, Pom " "Klementieff, Michael Rooker, Chris Sullivan, Glenn Close, Sean Gunn",
    "The team struggles to keep its newfound family together as it tires to unravel the mystery of Peter Quill's true parentage in the outer reaches of the galaxy.",
    )

mummy = movies.media(
    "The Mummy",
    "https://avatarfiles.alphacoders.com/686/thumb-68668.jpg",
    "https://www.youtu.be/sCdV3esMr9M",
    "June 9, 2017",
    "Sofia Boutella, Tom Cruise, Annabelle Wallis, Russell Crowe, Jake Johnson, Courtney B. Vance",
    "An ancient princess is awakened from her crypt beneath the desert,bringing with her malevolence grown over millennia, and terrors that defy human comprehension",
    )

wonder = movies.media(
    "The Wonder Woman",
    "https://qph.ec.quoracdn.net/main-thumb-t-1802479-200-hvmgdcwdrikgplimbrgjgtsmtiefktfy.jpeg",
    "https://www.youtu.be/1Q8fG0TtVAY",
    "June 23, 2017",
    "Gal Gadot, Chris Pine, Robin Wright, Danny Huston, David Thewlis, Ewen Bremner, Said Taghmaoui, Elena Anaya, Lucy Davis, Connie Nielsen",
    "Before she was Wonder Woman she was Diana, princess of the Amazons, trained warrior."
    " When a pilot crashes and tells of conflict in the outside world, she leaves home to fight a war to end all wars, discovering her full powers and true destiny.",
    )

pirates = movies.media(
    "Pirates of the Caribbean: Dead Men Tell No Tales",
    "http://cdn.movieweb.com/img.news.tops/NEEnkKMg5cVSIF_2_b.jpg",
    "https://www.youtu.be/2qY3w9NTxxA",
    "July 7, 2017",
    "Johnny Depp, Geoffrey Rush, Javier Bardem, Kevin R. McNally, Stephen Graham, Golshifteh Farahani, Kaya Scodelario, Brenton Thwaites, Orlando Bloom",
    "Thrust into an all-new adventure, a down-on-his-luck Capt. Jack Sparrow (Johnny Depp) feels the winds of ill-fortune blowing even more strongly when deadly ghost" "sailors led by his old nemesis, the evil Capt. Salazar (Javier Bardem), escape from the Devil's Triangle. Jack's only hope of survival lies in seeking out the" "legendary Trident of Poseidon, but to find it, he must forge an uneasy alliance with a brilliant and beautiful astronomer and a headstrong young man in the British" "navy.",
    )

thor = movies.media (
    "Thor: Ragnarok",
    "https://upload.wikimedia.org/wikipedia/en/thumb/7/7d/Thor_Ragnarok_poster.jpg/220px-Thor_Ragnarok_poster.jpg",
    "https://www.youtu.be/v7MGUNV8MxU",
    "November 3, 2017",
    "Tom Hiddleston, Chris Hemsworth, Idris Elba, Karl Urban, Mark Ruffalo, Jeff Goldblum, Cate Blanchett, Anthony Hopkins, Tessa Thompson, Lou Ferrigno, Jasper Bagg",
    "Imprisoned on the other side of the universe, the mighty Thor (Chris Hemsworth) finds himself in a deadly gladiatorial contest that pits him against the Hulk (Mark Ruffalo), his former ally and fellow Avenger. Thor's quest for survival leads him in a race against time to prevent the all-powerful Hela (Cate Blanchett) from destroying his home world and the Asgardian civilization.",
    )

star = movies.media(
    "Star Wars: The Last Jedi",
    "https://upload.wikimedia.org/wikipedia/en/thumb/7/7f/Star_Wars_The_Last_Jedi.jpg/220px-Star_Wars_The_Last_Jedi.jpg",
    "https://www.youtu.be/zB4I68XVPzQ",
    "December 15, 2017",
    "Mark Hamill, Carrie Fisher, Adam Driver, Daisy Ridley, John Boyega, Oscar Isaac, Lupita Nyong’o, Domhnall Gleeson, Anthony Daniels, Gwendoline Christie, Andy Serkis, Benicio Del Toro, Laura Dern, Kelly Marie Tran",
    "Having taken her first steps into a larger world in Star Wars: The Force Awakens (2015), Rey continues her epic journey with Finn, Poe and Luke Skywalker in the next chapter of the saga.",
    )
# all ways give space after ""#""
# movie data list
movies = [guardians, mummy, wonder, pirates, thor ,star]
# calling fresh_tomatoes to create a movie pages with above movie data list
fresh_tomatoes.open_movies_page(movies)
