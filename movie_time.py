import webbrowser


class Movie:
    def __init__(self, title, story_line, poster, trailer):
        self.title = title
        self.story_line = story_line
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer

    def show_trailer(self):
        webbrowser.open_new_tab(self.trailer_youtube)


