import json

# Problems:
# User ID 3 has an empty name.
# User ID 4 has a duplicate friend entry.
# User ID 5 has no connections or liked pages (inactive user).
# The pages list contains duplicate page IDs.

# Task 2: Clean the Data
# We will:
# Remove users with missing names.
# Remove duplicate friend entries.
# Remove inactive users (users with no friends and no liked pages).
# Deduplicate pages based on IDs.

def clean_data(data):
    # Remove Users with missing names 
    data["users"]=[user for user in data["users"] if user["name"].strip()]

    # Remove duplicate friends 
    for user in data["users"]:
        user["friends"]=list(set(user["friends"]))

    # Remove inactive users
        data["users"]=[user for user in data["users"] if user["friends"] or user["liked_pages"]] 

    # Remove duplicate Pages 
    unique_pages = {}
    for page in data["pages"]:
        unique_pages[page["id"]]=page
        data["pages"]=list(unique_pages.values())

    return data

# Load the data
data = json.load(open("data2.json"))
data=clean_data(data)
json.dump(data,open("Cleaned_CodeBook_data.json","w"),indent=4)
print("Data Cleaned Successfully ")

