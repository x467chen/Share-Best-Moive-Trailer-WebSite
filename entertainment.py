import media
import fresh_tomatoes


breathe = media.Moive("Breathe", 
                      "https://static.rogerebert.com/uploads/movie/movie_poster/breathe-2017/large_image001.jpg",
                      "https://www.youtube.com/watch?v=7_YnYrLfjxA")
the_circle = media.Moive("THE CIRCLE", "https://static.electronicsweekly.com/wp-content/uploads/2017/09/05090926/The-Circle-poster-Tom-Hanks.jpg",
                         "https://www.youtube.com/watch?v=ZkzpcfY9JAo")
gifted = media.Moive("Gifted",
                     "https://www.nagc.org/sites/default/files/images/Gifted_film_poster.jpg",
                     "https://www.youtube.com/watch?v=hqTSKqBCdf0")

before_we_go = media.Moive("Before We Go",
                           "https://upload.wikimedia.org/wikipedia/en/e/e7/Before_We_Go_Poster.jpg",
                           "https://www.youtube.com/watch?v=VrNwcGVGrBw")
one_day = media.Moive("One Day",
                      "http://www.earlyword.com/wp-content/uploads/2011/02/ONE-DAY-POSTER.jpg",
                      "https://www.youtube.com/watch?v=zVuuooZqVaU")
if_i_stay = media.Moive("If I Stay",
                        "https://www.booktopia.com.au/http_coversbooktopiacomau/big/9781909531239/if-i-stay.jpg",
                        "https://www.youtube.com/watch?v=wH6PNeTy6Nc")


def main():
    # print the main function of my super class
    print("class Video"+media.Video.__doc__)

    # make a moive list and print the basic inforamtion of them
    moives = [breathe, before_we_go, gifted, the_circle, one_day, if_i_stay]
    print("Moive List: ")
    for m in moives:
        m.show_information()

    # generate the website of my moive tailers
    fresh_tomatoes.open_movies_page(moives)

if __name__ == "__main__":
    main()


