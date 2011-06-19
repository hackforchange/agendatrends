import logging
from agendatrends.pipelines.services import ServicePipeline


class OpenCalaisIdentify(ServicePipeline):

	config = {
	
		'api_key': 'v3n6xjrsfuhg75f4ajzht2da',
		'submitter': 'AgendaTrends/Hack For Change'
	
	}
	

	def run(self, url):
		
		from calais import Calais
		c = Calais(self.config['api_key'], submitter=self.config['submitter'])
		
		object_result = c.analyze_url(url)
		
		logging.info(str(object_result))