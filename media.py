import webbrowser


class Video():
    """This class provides the method to store the information of video"""
    """Copyright: Xuanqi Chen"""
    """2017/11/05"""
    def __init__(self, title, poster_image_url):
        self.title = title
        self.poster_image_url = poster_image_url

    def show_information(self):
        print("Video name" + self.title)


# inheratance and create a class to store the information of moives
class Moive(Video):
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        Video.__init__(self, title, poster_image_url)
        self.trailer_youtube_url = trailer_youtube_url

    def show_information(self):
        print("Moive name: " + self.title)


# inheritance create a class to store the information of Tv Shows
class TvShow(Video):
    def __init__(self, title, poster_image_url, trailer_youtube_url, season, episode):
        Video.__init__(self, title, poster_image_url)
        self.trailer_youtube_url = trailer_youtube_url
        self.season = season
        self.episode = episode

    def show_information(self):
        print("TV Show name" + self.title)
