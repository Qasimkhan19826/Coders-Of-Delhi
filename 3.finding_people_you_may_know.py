import json

# Step 1 Loading the data 
def load_data(filename):
    with open(filename,"r") as f:
        return json.load(f)

# Creating functions for find_people_you_may_know 
def find_people_you_may_know(user_id,data):
    user_friends={}
# Step 2 Collecting user friends 
    for user in data['users']:
        user_friends[user['id']]= set(user['friends'])

        if user_id not in user_friends:
            return[]    
# Step 3 Get the user direct friends 
        direct_friends=user_friends[user_id]
        suggestions={}
# Step 4 Find and count suggeted people
    for friend in direct_friends: # {2,3,4,5,6}
        # For all friends of friend
        for mutual in user_friends[friend]:# 2:{1,3,5,6,7} 3:{1,2,4,7,8}
            # If mutual id is not the same user and not already a direct friend of user
            if mutual != user_id and mutual not in direct_friends:
                  # Count mutual friends
                suggestions[mutual] = suggestions.get(mutual,0)+1
                #  suggestions[7]=suggestions.get(7,0) + 1 ,does 7 exist no (Because 7 appears for the first time) {7:1}
                # If 7 appears for the 2nd time than 1 + 1 = 2
                # suggestions[7]=suggestions.get(7,0) + 1
                # {7:2}
# Step 5 Sort the suggestions    
    sorted_suggestions=sorted(suggestions.items(),key=lambda x: x[1],reverse=True)
# Step 6 return the data  
    return [(user_id,mutual_count) for user_id , mutual_count in sorted_suggestions] # This will print the score also
    # return [user_id for user_id , _ in sorted_suggestions]

# Load the data

data = load_data("massive_data.json")
user_id =1
recommendations = find_people_you_may_know(user_id,data)
print(f" People You May Know For User {user_id}:{recommendations}")  
with open("people_you_may_know.json","w") as f:
    json.dump(recommendations,f)  




