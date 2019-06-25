import sys; sys.path.append('../') # for correct types inclusion,

import grpc

import types_pb2
import types_pb2_grpc
from google.protobuf import timestamp_pb2

import time
import pandas as pd

SERVER_ADDRESS = 'SERVER'
PATH_TO_CERT_FILE = 'PATH'


def main():
    # Create credentials for use with an secured channel
    creds = grpc.ssl_channel_credentials(open(PATH_TO_CERT_FILE, 'rb').read())

    # Initialize GRPC channel
    channel = grpc.secure_channel(SERVER_ADDRESS, creds)

    # create stub
    stub = types_pb2_grpc.HistoricDataStub(channel)

    now = time.time()
    seconds = int(now)
    to_time = timestamp_pb2.Timestamp(seconds=seconds)
    from_time = timestamp_pb2.Timestamp(seconds=to_time.seconds - int(86400 / 2))  # last 12 hours

    # in our case we have to use kwarg because `from` is
    # is recognized as python keyword so there would syntax be error
    # if you want get value you have to use getattr()
    historic_request_kwargs = {'from': from_time, 'to': to_time}
    req = types_pb2.HistoricRequest(**historic_request_kwargs)
    tweet_items = stub.HistoricTweets(req)

    # dataframe inputs
    inputs = []
    for tweet in tweet_items.items:
        # tweet attributes are defined in proto file
        author_name = tweet.extended_tweet.author_name
        content = tweet.base.content
        sentiment = tweet.sentiment.sentiment
        inputs.append([author_name, content, sentiment])

    df = pd.DataFrame(inputs, columns=['User', 'Content', 'Sentiment'])

    print(df)


if __name__ == '__main__':
    main()