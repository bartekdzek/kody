**Instagram Follower Bot**

This project is an automated bot designed to log into an Instagram account, find followers from a specified account, and automatically follow those followers. It leverages the selenium library to perform browser automation.

**Project Overview**

The Instagram Follower Bot is a simple yet powerful tool to help you grow your Instagram network by automating the following process. The bot navigates through Instagram, logs in with your credentials, locates followers of a specified account, and follows them. This approach can save you a significant amount of time and effort compared to manual following.

**Features**
- Automated Login: Logs into your Instagram account using your provided username and password.
- Followers Discovery: Navigates to the specified account and retrieves a list of its followers.
- Auto-Follow: Automatically follows the users from the retrieved list of followers.
- 
*Requirements*

To run this project, you need the following:
- Python 3.12
- Selenium library
- ChromeDriver

**Code Structure**

The project consists of a single class, InstaFollower, which includes methods for logging in, finding followers, and following them.

**Initialization:**

Sets up the Chrome browser with options to prevent it from closing after the script completes.
login(): Automates the login process, including handling pop-ups for cookies, saving login info, and notifications.
find_followers(): Navigates to the specified account profile, clicks the followers link, and scrolls through the followers list to load more users.
follow(): Finds and clicks the "Follow" buttons to follow users, handling any pop-ups that might block the button.
