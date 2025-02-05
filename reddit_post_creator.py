from reddit_auth import reddit

def create_reddit_post(
    title: str,
    content: str,
    subreddit_name: str
) -> bool:
    """
    Create a text post on Reddit.
    
    Args:
        title (str): The title of the post
        content (str): The content/body of the post
        subreddit_name (str): Name of the subreddit to post to
        
    Returns:
        bool: True if post was successful, False otherwise
    """
    try:
        # Get the subreddit instance
        subreddit = reddit.subreddit(subreddit_name)
        
        # Create the text post
        post = subreddit.submit(
            title=title,
            selftext=content
        )
            
        print(f"Successfully created post: {post.url}")
        return True
        
    except Exception as e:
        print(f"Error creating post: {str(e)}")
        return False 