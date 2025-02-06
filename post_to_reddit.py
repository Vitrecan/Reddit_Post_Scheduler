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
* Regularly contribute to clan donations, because sharing is caring, and we care a lot.
* Must get 3 stars in all attacks no matter what.
* Must talk in chat no matter what time it is.
* Must do Clan Games even if you accidentally kicked your phone off the bridge.
**Qualifications**:
* Minimum of 0 trophies (we're elite, but we're not snobs).
* Experience in always winning in every attack.
* A sense of humor that can withstand the worst Dad jokes from our dead chat.
* Must not be afraid of several Clan War losses.
**Perks**:
* Be paid in troop donations (such as Goblins).
* Clan War League Bonuses offered to our top 5 employees of the event.
* An opportunity to be promoted to Elder.
**How to Apply**:
Send us your resume on the "I like to join your clan" message (our clan is invite only) or just drop down the word "Reddit" if you're looking for an unpaid position in our clan! Make sure to be fully maxed.
~~The above was a joke plz join our clan we dont care if ur a rushed th1 if thats even a thing :)~~"""
    
    # Make the post
    success = create_reddit_post(
        title=title,
        content=content,
        subreddit_name="ClashOfClansRecruit"  # Change to your target subreddit
    )
    
    # GitHub Actions will show this in the run log
    if not success:
        raise Exception("Failed to create Reddit post")

if __name__ == "__main__":
    main() 