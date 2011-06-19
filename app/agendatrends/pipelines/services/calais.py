import re
import urllib
import httplib
import logging
import simplejson as json

from StringIO import StringIO

from agendatrends.pipelines.services import ServicePipeline

## === Analyze URL or blob with OpenCalais === ##
class OpenCalaisIdentify(ServicePipeline):

	config = {
	
		'api_key': 'v3n6xjrsfuhg75f4ajzht2da',
		'submitter': 'AgendaTrends/Hack For Change'
	
	}
	
	def run(self, url):
		
		from calaislib import Calais
		c = Calais(self.config['api_key'], submitter=self.config['submitter'])
		
		object_result = c.analyze_url(url)
		
		self.memcache.set('object_result', object_result)