import os
from dotenv import load_dotenv
import praw

# Load environment variables from the .env file
load_dotenv()

# Retrieve credentials from environment variables
REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USERNAME = os.getenv("REDDIT_USERNAME")
REDDIT_PASSWORD = os.getenv("REDDIT_PASSWORD")

# Validate that all credentials are available
if not all([REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USERNAME, REDDIT_PASSWORD]):
    raise ValueError("Missing one or more Reddit API credentials.")

# Initialize the PRAW Reddit instance
reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    username=REDDIT_USERNAME,
    password=REDDIT_PASSWORD,
    user_agent="MyRedditPostScheduler/0.1"
)

# Example: Print the name of the authenticated user
print(f"Logged in as: {reddit.user.me()}")
