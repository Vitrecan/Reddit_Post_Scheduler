import schedule
import time
from datetime import datetime
from reddit_post_creator import create_reddit_post

class RedditScheduler:
    def __init__(self):
        self.scheduled_posts = []

    def add_post(self, title: str, content: str, subreddit: str, post_time: str):
        """
        Schedule a new post
        post_time format: "HH:MM" (24-hour format)
        Example: "14:30" for 2:30 PM
        """
        try:
            # Validate time format
            datetime.strptime(post_time, "%H:%M")
            
            # Create job
            schedule.every().day.at(post_time).do(
                create_reddit_post,
                title=title,
                content=content,
                subreddit_name=subreddit
            )
            
            # Store post details
            self.scheduled_posts.append({
                "title": title,
                "content": content,
                "subreddit": subreddit,
                "time": post_time
            })
            
            print(f"Post scheduled for {post_time}")
            return True
            
        except ValueError as e:
            print(f"Error scheduling post: {str(e)}")
            return False

    def run(self):
        """Run the scheduler"""
        print("Scheduler started. Running...")
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute 