# FUCKING TWITTER API PRICES!!!!

from TwitterAPI import TwitterAPI
api = TwitterAPI(consumer_key='redacted', consumer_secret='redacted', access_token_key='redacted', access_token_secret='redacted')
blockedUsers = list(set(user['screen_name'] for user in api.request('blocks/list', {'include_entities': 'false', 'skip_status':'true'})))

with open('Twitter.txt', 'r') as file:
    users = file.readlines()
    users = [i[1:] for i in users]
    print(len(users))
    for i in range(len(users)):
        for user in list(set(post['user']['screen_name'] for post in api.request('search/tweets', {'q': str(i), 'count':'100', 'include_entities':'false'}))):
            try:
                if user in blockedUsers:
                    print(f"user: {users[i]} is already blocked")
                    continue
                else:
                    block = api.request('blocks/create', {'screen_name': users[i]})
                if block:
                    print(f"user: {users[i]} has been blocked")
            except Exception:
                print("Something went wrong")
