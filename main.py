import praw
import webbrowser

# Custom modules
import misc_funcs
import settings

# Reddit Settings
reddit = praw.Reddit(client_id=settings.CLIENT_ID,
                     client_secret=settings.CLIENT_SECRET,
                     user_agent=settings.CLIENT_AGENT)

SUBREDDITS = settings.SUBREDDITS
CHROME_PATH = settings.CHROME_PATH

POSTS_DATA = {}


# Functions

def get_reddit_posts():
    print("\nReddit posts")
    for subreddit in SUBREDDITS:

        subreddit = reddit.subreddit(subreddit)
        print(f"----- {subreddit.title} -----")

        for post in subreddit.top(time_filter='day', limit=settings.POST_LIMIT):
            POSTS_DATA[str(post.id)] = post.url
            print(f"{post.id} | {post.title} | {post.score}")

        print()


def open_webpages(webpage_urls):
    for url in webpage_urls:
        webbrowser.get(CHROME_PATH).open(url)


def open_links():
    open_flag = False

    while open_flag == False:
        open_post_input = input("Would you like to open any post? (y/n):")

        if open_post_input.lower() == "y":
            flag = False

            while flag == False:
                post_id = input("Enter the post id:")

                if post_id in POSTS_DATA.keys():
                    flag = True

                    post_url = POSTS_DATA[post_id]
                    webbrowser.get(CHROME_PATH).open(post_url)

                else:
                    print("Invalid ID")

        elif open_post_input.lower() == "n":
            open_flag = True

        else:
            print("Invalid input. Enter either 'y' or 'n'.")



if __name__ == "__main__":
    print()
    if settings.WEATHER_API_KEY != None:
        misc_funcs.get_weather()

    open_webpages(settings.WEBPAGE_URLS)

    if settings.CLIENT_SECRET != None:
        get_reddit_posts()
        open_links()

    if settings.FOOTBALL_API_TOKEN != None:
        if input("Would you like to view the PL table? (y/n):").lower() == 'y':
            misc_funcs.get_pl_table()

    if len(settings.STOCKS) > 0:
        print("\n\n----- STOCK MARKET WATCHLIST -----")
        misc_funcs.get_stock_details()
        print()