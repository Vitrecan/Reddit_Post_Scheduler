from scheduler import RedditScheduler

def main():
    scheduler = RedditScheduler()
    
    # Schedule a test post for a specific time
    scheduler.add_post(
        title="Scheduled Test Post",
        content="This post was automatically scheduled!",
        subreddit="test",
        post_time="01:07"  # Will post at 1:05 AM
    )
    
    # Run the scheduler
    scheduler.run()

if __name__ == "__main__":
    main()