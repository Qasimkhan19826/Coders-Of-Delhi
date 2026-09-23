import json
#  Lets write a function to load the data
def load_data(filename):
    with open(filename,"r") as f:
        data = json.load(f) # Why load method because we are giving file object 
        # not strings
    return data      

data = load_data("data.json")
# print(data)

# Write a function to display users and their connections
def display_users(data):
    print("Users and their connections")
    for user in data['users']:
        print(f"ID:{user['id']} - {user['name']} is friends with: {user['friends']} and liked pages are {user['liked_pages']} ")
    print("\n Pages Information")
    for page in data['pages']:
            print(f"{page['id']} {page['name']}")

display_users(data)