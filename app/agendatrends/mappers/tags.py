from mapreduce import operation as op


def CountOccurrences(entity):
    yield op.counters.Increment(entity.topic.key().name() + "|" + entity.discourse.key().name())
    yield op.counters.Increment(entity.topic.key().name() + "|" + entity.discourse.published.year)
    yield op.counters.Increment(entity.topic.key().name() + "|" + entity.discourse.published.year + "-" + entity.discourse.published.day)
    yield op.counters.Increment(entity.topic.key().name() + "|" + entity.discourse.published.year + "-" + entity.discourse.published.day + "-" + entity.discourse.published.hour)

