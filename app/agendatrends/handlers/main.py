from agendatrends.handlers import WebHandler
import logging


class Topic(object):

	@classmethod
	def all(cls):
		return ['libya', 'taxes', 'unemployment']


class TopicFilters(object):

	def __init__(self, filters):
		self.all_filters = filters.split('/')
		self.topic = self.all_filters[0]




class LandingHandler(WebHandler):

    def get(self):

        return self.render('main/landing.html', topics = Topic.all())


class TopicHandler(WebHandler):

	def get(self, filters):
		logging.info(str(filters))
		if len(filters) == 0:
			self.abort(400, "Must supply at least a topic filter")

					
		tf = TopicFilters(filters)

		if tf.topic not in Topic.all():
			self.abort(400, "Invalid topic %s" % (tf.topic))
		

		return self.render('main/topic.html', topic = tf.topic)

