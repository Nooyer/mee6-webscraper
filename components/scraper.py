import requests


class Scraper:

    def __init__(self, url):
        self.web_page = requests.get(url)

    def get_leaderboard(self):
        # scrapes 
        leaderboard_raw = self.web_page.json()

        user_list = []
        users = leaderboard_raw.get('players')
        for user in users:
            player = {'id': user.get('id'), 'level': user.get('level'), 'message_count': user.get('message_count'),
                      'xp': user.get('xp')}
            user_list.append(player)

        if len(user_list) > 0:
            return user_list
        else:
            return
