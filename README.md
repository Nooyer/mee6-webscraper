# Discord Mee6 Web Scraper

This program is designed to scrape the Mee6 leaderboard and export it into a JSON file.\
It will scrape the following info of every Mee6 players in your server:
* User's Discord ID
* Level
* Number of messages sent in total
* Number of experience points in total
### Prerequsites
* Python 3.8+
* `requests` library

## How to Run the Scraper
1. Install the following libraries:
```
pip install -r requirements.txt
```

2. Replace `123456789012345678` in `main.py` with the intended server leaderboard URL number
```
url = "https://mee6.xyz/api/plugins/levels/leaderboard/123456789012345678?page="
```

3. Execute the program with:
```
python main.py
```
or
```
python3 main.py
```
