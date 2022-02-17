class RankingGame:
    def __init__(self, id, game_id, name, rate, rate_count, cover_url):
        self.id = id
        self.game_id = game_id
        self.name = name
        self.rate = rate
        self.count_rates = rate_count
        self.cover_url = cover_url


class DetailGame:
    def __init__(self, game_id, name, rate, rate_count, cover_url, genres, platforms, release_date, summary):
        self.game_id = game_id
        self.name = name
        self.rate = rate
        self.count_rates = rate_count
        self.cover_url = cover_url
        self.genres = genres
        self.platforms = platforms
        self.release_date = release_date
        self.summary = summary
