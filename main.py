from reddit_post_creator import create_reddit_post

def test_post():
    result = create_reddit_post(
        title="Test Post",
        content="This is a test post from my Reddit scheduler!",
        subreddit_name="test"
    )
    print(f"Post success: {result}")

if __name__ == "__main__":
    test_post()