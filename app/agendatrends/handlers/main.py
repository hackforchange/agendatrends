from agendatrends.handlers import WebHandler
import logging


class Topic(object):

	@classmethod
	def all(cls):
		return ['libya', 'taxes', 'unemployment']


	@classmethod
	def filterWith(cls, topic_filters):
		result = "/%s%s" % (topic_filters.topic, topic_filters.filteredUrl())
		logging.info(result)
		return result




class TopicFilters(object):

	def __init__(self, filters):
		self.all_filters = filters.split('/')
		self.topic = self.all_filters[0]

		self.applied_filters = {}
		for i in range(1, len(self.all_filters), 2):
			topic = self.all_filters[i]
			topic_value = self.all_filters[i+1]
			self.applied_filters.setdefault(topic, []).append(topic_value)

	
	def __get__(self, key):
		return self.applied_filters[key]


	def keys(self):
		return self.applied_filters.keys()

	def filteredUrl(self):
		baseUrl = "/"

		for key in self.applied_filters.keys():
			baseUrl = "/" + key + "/"
			baseUrl += ("/" + key + "/").join(self.applied_filters[key])
		
		return baseUrl






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

