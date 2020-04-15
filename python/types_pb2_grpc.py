# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import types_pb2 as types__pb2


class MessagesProxyStub(object):
  """*
  Service for entries streaming
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SubscribeBaseArticle = channel.unary_stream(
        '/MessagesProxy/SubscribeBaseArticle',
        request_serializer=types__pb2.AssetsFilter.SerializeToString,
        response_deserializer=types__pb2.PublicModel.FromString,
        )
    self.SubscribeArticle = channel.unary_stream(
        '/MessagesProxy/SubscribeArticle',
        request_serializer=types__pb2.AssetsFilter.SerializeToString,
        response_deserializer=types__pb2.Article.FromString,
        )


class MessagesProxyServicer(object):
  """*
  Service for entries streaming
  """

  def SubscribeBaseArticle(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SubscribeArticle(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MessagesProxyServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SubscribeBaseArticle': grpc.unary_stream_rpc_method_handler(
          servicer.SubscribeBaseArticle,
          request_deserializer=types__pb2.AssetsFilter.FromString,
          response_serializer=types__pb2.PublicModel.SerializeToString,
      ),
      'SubscribeArticle': grpc.unary_stream_rpc_method_handler(
          servicer.SubscribeArticle,
          request_deserializer=types__pb2.AssetsFilter.FromString,
          response_serializer=types__pb2.Article.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'MessagesProxy', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class DatasetStub(object):
  """*
  Service for requesting data from dataset
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Assets = channel.unary_unary(
        '/Dataset/Assets',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=types__pb2.AssetItems.FromString,
        )


class DatasetServicer(object):
  """*
  Service for requesting data from dataset
  """

  def Assets(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DatasetServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Assets': grpc.unary_unary_rpc_method_handler(
          servicer.Assets,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=types__pb2.AssetItems.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Dataset', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class HistoricDataStub(object):
  """*
  Service for requesting historic data
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.HistoricBaseArticles = channel.unary_stream(
        '/HistoricData/HistoricBaseArticles',
        request_serializer=types__pb2.HistoricRequest.SerializeToString,
        response_deserializer=types__pb2.PublicModel.FromString,
        )
    self.HistoricArticles = channel.unary_stream(
        '/HistoricData/HistoricArticles',
        request_serializer=types__pb2.HistoricRequest.SerializeToString,
        response_deserializer=types__pb2.Article.FromString,
        )


class HistoricDataServicer(object):
  """*
  Service for requesting historic data
  """

  def HistoricBaseArticles(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def HistoricArticles(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_HistoricDataServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'HistoricBaseArticles': grpc.unary_stream_rpc_method_handler(
          servicer.HistoricBaseArticles,
          request_deserializer=types__pb2.HistoricRequest.FromString,
          response_serializer=types__pb2.PublicModel.SerializeToString,
      ),
      'HistoricArticles': grpc.unary_stream_rpc_method_handler(
          servicer.HistoricArticles,
          request_deserializer=types__pb2.HistoricRequest.FromString,
          response_serializer=types__pb2.Article.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'HistoricData', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class SentimentsStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.HistoricSocialSentiment = channel.unary_stream(
        '/Sentiments/HistoricSocialSentiment',
        request_serializer=types__pb2.SentimentHistoricRequest.SerializeToString,
        response_deserializer=types__pb2.AggregationCandle.FromString,
        )
    self.HistoricNewsSentiment = channel.unary_stream(
        '/Sentiments/HistoricNewsSentiment',
        request_serializer=types__pb2.SentimentHistoricRequest.SerializeToString,
        response_deserializer=types__pb2.AggregationCandle.FromString,
        )
    self.SubscribeSocialSentiment = channel.unary_stream(
        '/Sentiments/SubscribeSocialSentiment',
        request_serializer=types__pb2.AggregationCandleFilter.SerializeToString,
        response_deserializer=types__pb2.AggregationCandle.FromString,
        )
    self.SubscribeNewsSentiment = channel.unary_stream(
        '/Sentiments/SubscribeNewsSentiment',
        request_serializer=types__pb2.AggregationCandleFilter.SerializeToString,
        response_deserializer=types__pb2.AggregationCandle.FromString,
        )


class SentimentsServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def HistoricSocialSentiment(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def HistoricNewsSentiment(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SubscribeSocialSentiment(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SubscribeNewsSentiment(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SentimentsServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'HistoricSocialSentiment': grpc.unary_stream_rpc_method_handler(
          servicer.HistoricSocialSentiment,
          request_deserializer=types__pb2.SentimentHistoricRequest.FromString,
          response_serializer=types__pb2.AggregationCandle.SerializeToString,
      ),
      'HistoricNewsSentiment': grpc.unary_stream_rpc_method_handler(
          servicer.HistoricNewsSentiment,
          request_deserializer=types__pb2.SentimentHistoricRequest.FromString,
          response_serializer=types__pb2.AggregationCandle.SerializeToString,
      ),
      'SubscribeSocialSentiment': grpc.unary_stream_rpc_method_handler(
          servicer.SubscribeSocialSentiment,
          request_deserializer=types__pb2.AggregationCandleFilter.FromString,
          response_serializer=types__pb2.AggregationCandle.SerializeToString,
      ),
      'SubscribeNewsSentiment': grpc.unary_stream_rpc_method_handler(
          servicer.SubscribeNewsSentiment,
          request_deserializer=types__pb2.AggregationCandleFilter.FromString,
          response_serializer=types__pb2.AggregationCandle.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Sentiments', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
