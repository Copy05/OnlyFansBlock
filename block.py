from TwitterAPI import TwitterAPI
api = TwitterAPI(consumer_key='redacted', consumer_secret='redacted', access_token_key='redacted', access_token_secret='redacted')
blockedUsers = list(set(user['screen_name'] for user in api.request('blocks/list', {'include_entities': 'false', 'skip_status':'true'})))

with open('Twitter.txt', 'r') as file:
    users = file.readlines()
    print(len(users))
    for i in range(len(users)):
        for user in list(set(post['user']['screen_name'] for post in api.request('search/tweets', {'q': str(i), 'count':'100', 'include_entities':'false'}))):
            try:
                if user in blockedUsers:
                    print(f"user: {i} is already blocked")
                    continue
                else:
                    block = api.request('blocks/create', {'screen_name': i})
                if block:
                    print(f"user: {i} has been blocked")
            except Exception:
                print("Something went wrong")
