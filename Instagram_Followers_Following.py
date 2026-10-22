# - - - - - LIBRARIES - - - - - #
import json

# - - - - - READING FILES - - - - - #
# Followers
with open("followers_1.json", "r") as file:
    followers_data = json.load(file)

# Following
with open("following.json", "r") as file:
    following_data = json.load(file)

# - - - - - READING FOLLOWERS / FOLLOWING - - - - - #
followers_list = []
following_list = []

# Followers
for follower in followers_data:
    # Looping through item in string data
    for string_data in follower.get("string_list_data", []):
        followers_list.append(string_data.get("value"))

# Following
following_data = following_data.get("relationships_following", [])
for following in following_data:
    following_list.append(following.get("title"))

# - - - - - COMPARING LISTS - - - - - #
you_dont_follow_back = list(set(followers_list) - set(following_list))

dont_follow_you_back = list(set(following_list) - set(followers_list))

# - - - - - WRITING TO FILE - - - - - #
with open("you_dont_follow_back.txt", "w") as file:
    for item in you_dont_follow_back:
        file.write(f"{item}\n")

with open("dont_follow_you_back.txt", "w") as file:
    for item in dont_follow_you_back:
        file.write(f"{item}\n")