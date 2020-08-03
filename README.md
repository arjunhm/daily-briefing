# Description
Daily Briefing is a script written in Python to automate the tasks in your daily life.
It's configured to
- Open webpages of your choice.
- Display information on the weather in your city.
- Display the trending posts on your favorite subreddits.
- Display the current standings of football clubs in the Premier League.
- Display information on stocks of your choice. (Only NSE)

# Setup 

Install necessary packages by running  
```pip install -r requirements.txt```

# Configuration

For enabling Reddit API, basic knowledge on how reddit works is required.  
- Create a Reddit App at [this page](https://www.reddit.com/prefs/apps)
- Create a name for the app and select "script" for the type of app.  
- Set the redirect URI to "https://localhost:8000".

Make the following changes in settings.py
- Set the CLIENT_ID to the client ID in the Reddit Apps page. (Value is right below the app name)
- Set CLIENT_SECRET to the secret value in the Reddit Apps page. (Value is in bold letters in the Apps page)
- Set the CLIENT_AGENT to the name of the app.
- Add your favorite subreddits to the SUBREDDITS list. 
- Set the POST_LIMIT to a value of your choice. By default, the top 10 posts are displayed for each subreddit.


For enabling the Weather API
- Create an account at [this page](https://openweathermap.org/api)  
- Set WEATHER_API_KEY to the API Key value.
- Set WEATHER_LOCATION to a location of your choice

For enabling the Football API
- Create an account at [this page](https://www.football-data.org/)  
- Set FOOTBALL_API_TOKEN to the API Key value.

All APIs are free but come with limited usage (except for the Reddit API).  
If you wish to disable any of the following APIs, set the respective API Key to None (without any quotes).  

For the stock market watchlist feature, add stock symbols (Only NSE) of your choice to the STOCKS list. 

For opening webpages,
- Set CHROME_PATH the file location of your browser.
- Add webpages of your choice to the WEBPAGE_URLS list.

# Screenshots
![s1](https://github.com/arjunhm/daily-briefing/blob/master/screenshots/s3.JPG)
![s2](https://github.com/arjunhm/daily-briefing/blob/master/screenshots/s2.JPG)
