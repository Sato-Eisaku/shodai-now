import requests
import os
import json
from TwitterAPI import TwitterAPI

# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = os.environ.get("BEARER_TOKEN")


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2FilteredStreamPython"
    return r


def get_rules():
    response = requests.get(
        "https://api.twitter.com/2/tweets/search/stream/rules", auth=bearer_oauth
    )
    if response.status_code != 200:
        raise Exception(
            "Cannot get rules (HTTP {}): {}".format(response.status_code, response.text)
        )
    print(json.dumps(response.json()))
    return response.json()


def delete_all_rules(rules):
    if rules is None or "data" not in rules:
        return None

    ids = list(map(lambda rule: rule["id"], rules["data"]))
    payload = {"delete": {"ids": ids}}
    response = requests.post(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        auth=bearer_oauth,
        json=payload
    )
    if response.status_code != 200:
        raise Exception(
            "Cannot delete rules (HTTP {}): {}".format(
                response.status_code, response.text
            )
        )
    print(json.dumps(response.json()))


def set_rules(delete):
    with open("collectionTable.json", mode="r", encoding="utf-8") as f:
        config_json = json.load(f)
    rules = [{"value": f"#商大なう #{config['hashtag']} -is:retweet", "tag": f"{config['hashtag']}"} for config in config_json]
    payload = {"add": rules}
    response = requests.post(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        auth=bearer_oauth,
        json=payload,
    )
    if response.status_code != 201:
        raise Exception(
            "Cannot add rules (HTTP {}): {}".format(response.status_code, response.text)
        )
    print(json.dumps(response.json()))


def get_stream(set):
    with open("collectionTable.json", mode="r", encoding="utf-8") as f:
        config_json = json.load(f)
    response = requests.get(
        "https://api.twitter.com/2/tweets/search/stream", auth=bearer_oauth, stream=True,
    )
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Cannot get stream (HTTP {}): {}".format(
                response.status_code, response.text
            )
        )
    for response_line in response.iter_lines():
        if response_line:
            json_response = json.loads(response_line)
            print(json.dumps(json_response, indent=4, sort_keys=True))
            filtered_collection_id = filter(lambda x: x["hashtag"] == json_response["matching_rules"][0]["tag"], config_json)
            filtered_collection_id = list(filtered_collection_id)
            if len(filtered_collection_id) == 0:
                return
            collection_id = filtered_collection_id[0]["collection"]
            curate_collection(collection_id, [json_response["data"]])


def curate_collection(collection_id, tweets):
    consumer_key = os.environ.get("CONSUMER_KEY")
    consumer_secret = os.environ.get("CONSUMER_SECRET")
    access_token_key = os.environ.get("ACCESS_TOKEN_KEY")
    access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")
    api = TwitterAPI(
        consumer_key,
        consumer_secret,
        access_token_key,
        access_token_secret
      )
    change_list = [{"op": "add", "tweet_id": tweet["id"]} for tweet in tweets]
    payload = {
        "id": f"custom-{collection_id}",
        "changes": change_list
    }
    collection = api.request('collections/entries/curate', json.dumps(payload))
    print(collection.text)


def main():
    rules = get_rules()
    delete = delete_all_rules(rules)
    set = set_rules(delete)
    get_stream(set)
    # curate_collection([{"id": "1539946268541489152"}])


if __name__ == "__main__":
    main()