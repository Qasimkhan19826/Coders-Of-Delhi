import json

def load_data(filename):
    with open(filename,"r") as f:
        return json.load(f)

def find_pages_you_might_like(user_id,data):

# Step 1 : Collecting all liked pages 
    user_pages={}
    # store each user's liked pages
    for user in data['users']: 
        user_pages[user['id']]=set(user['liked_pages'])

    # unique_pages={
    #     1:{10,20}
    # }   2:{20,30,40}

    if user_id not in user_pages:
        return[] # If user not available it will return empty list

# Step 2 Get User 1's pages
    user_liked_pages=user_pages[user_id] # It will store id 1 liked pages {10,20}
    page_suggestions={} # Store suggestions score  E.g : {10:1}

# Step 3 Compare User 1 with every OTHER user
    for other_user,pages in user_pages.items(): # It will return tuple   
        # Don't compare user 1 with himself
        if other_user != user_id:
            # Find common pages
# Step 4 Find common pages using intersection()            
            shared_pages = user_liked_pages.intersection(pages)# len(shared_pages) len(2) because 2 are common

            # Eg: user1 {10,20} n user2 {20,10,30}
            # shared_pages= {20,10}
# Step 5 Check the other user's pages one by one
            for page in pages: # user 2 {20,10,30}
                # It will check pages one by one 
                # 20
                # 10
                # 30
# Step 6 Ignore pages User 1 already likes                
                if page not in user_liked_pages: # This will check the new pages for user 1
                    # Eg:20
                    # 20 not in {10,20} false ignore 20
                    # 10 not in {10,20} false ignore 10
                    # 30 not in {10,20} True (This will be recommendation)
# Step 7 Give NEW pages a score
# Step 8 Score = number of shared pages
                    page_suggestions[page] = (page_suggestions.get(page,0)+len(shared_pages))
                    # Therefore for page 30 will be
                    # page_suggestions[30]=(page_suggestions.get(30,0)+2)
                    # final answer {30,2}
# Step 9 If the same page appears again,add its new score to its old score
# Step 10 Sort highest score → lowest score
    sorted_pages=sorted(page_suggestions.items(),key= lambda x:x[1],reverse=True)
    # It will store value in this manner
    # [
    #     (103,2),
    #     (105,1)
    # ] Alist of tuples 
# Step 11 Return (page_id, score) 
    return [(page_id ,score) for page_id ,score in sorted_pages]

data = load_data('massive_data.json')
user_id = 1
page_recommendations = find_pages_you_might_like(user_id,data)
print(f"Pages You Might Like For User {user_id}:{page_recommendations}")





   
