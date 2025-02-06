import schedule
import time
from reddit_post_creator import create_reddit_post

class RedditScheduler:
    def __init__(self):
        self.scheduled_posts = []

    def add_monday_post(self, title: str, content: str, subreddit: str, time: str):
        """
        Schedule a post for every Monday
        time format: "HH:MM" (24-hour format)
        Example: "14:30" for 2:30 PM
        """
        try:
            # Create job for every Monday
            schedule.every().monday.at(time).do(
                create_reddit_post,
                title=title,
                content=content,
                subreddit_name=subreddit
            )
            
            print(f"Post scheduled for every Monday at {time}")
            return True
            
        except ValueError as e:
            print(f"Error scheduling post: {str(e)}")
            return False

    def run(self):
        """Run the scheduler"""
        print("Scheduler started. Running...")
        print("Press Ctrl+C to stop")
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute 