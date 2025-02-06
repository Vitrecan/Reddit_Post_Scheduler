from reddit_auth import reddit
from reddit_post_creator import create_reddit_post

def main():
    title = "[Recruiting] VesperGade | #8YYCGLGJ| Th1+ | Lvl 5 | Social/War | Independent"
    content = """Recruiting
# Job Description
**Position**: Member
**Location**: International
**Job Type**: Full-time, 24/7
**Responsibilities**:
* Willingness to participate in Clan Wars even if your Archer Queen is down.
* Regularly contribute to clan
* Must get 3 stars in all attacks no matter what.
* Must talk in chat no matter what time it is.
"""
    
    create_reddit_post(
        title=title,
        content=content,
        subreddit_name="ClashOfClansRecruit"  # Change to your target subreddit
    )

if __name__ == "__main__":
    main() 