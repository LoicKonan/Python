import instaloader

# Authenticate and authorize the user's Instagram account using the Instagram API
L = instaloader.Instaloader()
username = input("Enter your Instagram username: ")
password = input("Enter your Instagram password: ")
L.context.log("Logging in...")
L.load_session_from_file(username)
if not L.context.is_logged_in:
    L.context.log("Login failed.")
    exit()

# Retrieve the list of users who are following the user (followers list) and the list of users the user is following (following list)
profile = instaloader.Profile.from_username(L.context, username)
followers = set(profile.get_followers())
following = set(profile.get_followees())

# Identify users who are not following the user back
not_following_back = following - followers

# Use the Instagram API to unfollow each user in the list of users who are not following the user back
for user in not_following_back:
    L.context.log(f"Unfollowing user: {user.username}")
    L.unfollow(user)
