# Reddit_Post_Scheduler

Documentation:
Changes Made:
Updated the cron schedule in reddit_post.yml to trigger every Monday at 9:00 AM UTC.
Added a comment to clarify the timezone used in the schedule.
Ensured the workflow remains manually triggerable for testing purposes.
Impact:
The workflow will now run at the correct time (9:00 AM UTC) every Monday.
The added comment improves code readability and reduces potential confusion about the timezone.
The manual trigger capability is preserved for testing and debugging.
Usage:
The workflow will automatically run every Monday at 9:00 AM UTC.
To manually trigger the workflow, navigate to the GitHub Actions page and use the "Run workflow" button.