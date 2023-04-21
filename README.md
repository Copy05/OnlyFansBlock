# OnlyFans Blocklist

Twitter accounts of onlyfans models to block.

# Usage

First Install `TwitterAPI`:
```sh
$ pip install TwitterAPI
```
Then open `block.py` and configurate your API keys you can find them [here: https://apps.twitter.com/](https://apps.twitter.com/):
```py
api = TwitterAPI(consumer_key='redacted', consumer_secret='redacted', access_token_key='redacted', access_token_secret='redacted')
```
and then you can run the script to automatically block these accounts inside `Twitter.txt`
```sh
$ python3 block.py
```