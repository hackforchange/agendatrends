import re
import urllib
import httplib
import logging
import simplejson as json

from StringIO import StringIO

from agendatrends.models.tags import Tag
from agendatrends.models.topics import Topic
from agendatrends.models.discourse import NewsArticle

from agendatrends.pipelines.services import ServicePipeline


## === Analyze URL or blob with OpenCalais === ##
class OpenCalaisIdentify(ServicePipeline):

	config = {
	
		'api_key': 'v3n6xjrsfuhg75f4ajzht2da',
		'submitter': 'AgendaTrends/Hack For Change'
	
	}
	
	def run(self, article_key):
		
		from calaislib import Calais
		c = Calais(self.config['api_key'], submitter=self.config['submitter'])
		
		article = NewsArticle.get(self.db.Key(article_key))
		
		object_result = c.analyze_url(article.url)
		
		str_topics = {}
		for topic in object_result.socialTag:
			str_topics[topic['name'].replace(' ', '-')] = topic
			
		tags = []
		topics = Topic.get_by_key_name(str_topics.keys())

		i = 0
		for slug, topicname in str_topics.items():
			
			if topics[i] is None:
				t = Topic(key_name=slug, name=topicname)
				topic_key = t.put()
			else:
				topic_key = topics[i].key()
				
			tags.append(Tag(article, key_name=str(topic_key), topic=topic_key, discourse=article))
			i = i+1
			
		return [str(key) for key in self.db.put(tags)]