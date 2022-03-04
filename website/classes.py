class ApiConfiguration:
    def __init__(self):
        self._apiUri = 'https://api.igdb.com/v4'
        self._headers = {
            'Client-ID': '5mxvhx4wsmpqqere91pcd3ula4vec6',
            'Authorization': 'Bearer u8m7oulqxfj8g0yg4f0t3a9z43h1p8'
        }

    def get_apiUri(self):
        return self._apiUri

    def get_headers(self):
        return self._headers



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
