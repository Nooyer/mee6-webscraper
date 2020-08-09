import json

from components.scraper import Scraper


def main():
    url = "https://mee6.xyz/api/plugins/levels/leaderboard/123456789012345678?page="
    page_number = 0
    end_of_leaderboard = False
    json_user_list = []

    # loops until it reaches the end of the player list
    while not end_of_leaderboard:
        scraper = Scraper(url + str(page_number))
        leaderboard = scraper.get_leaderboard()
        if leaderboard is None:
            end_of_leaderboard = True
        else:
            json_user_list.append(leaderboard)
            page_number += 1

    # exports the parsed leaderboard list into a JSON file
    with open('leaderboard_list', 'w') as json_file:
        json.dump(json_user_list, json_file, indent=3)

    print("File Downloaded!")


if __name__ == '__main__':
    main()
