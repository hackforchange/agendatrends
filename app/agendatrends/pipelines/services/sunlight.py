import logging

from agendatrends.models.people import Legislator

from sunlightapi import sunlight, SunlightApiError
from agendatrends.pipelines.services import ServicePipeline



class SunlightPipeline(ServicePipeline):
	
	config = {
	
		'api_key': '5716fd8eb1ce418095fe402c7489281e'
	
	}
		

	
class SunlightLegislator(SunlightPipeline):

	def run(self, legislator=False, **kwargs):
		
		if legislator is False:
		
			sunlight.apikey = self.config['api_key']
		
			## Get legislator
			legislator = sunlight.legislators.get(**kwargs)
		
			logging.info('Getting legislator by ID: '+str(legislator.fec_id))
		
		l = Legislator(key_name=legislator.fec_id)
		
		## Map legislator properties
		for key, value in legislator.__dict__.items():
			if hasattr(l, key):
				setattr(l, key, value)
				
		l_key = l.put()
		logging.info('Put legislator: '+str(legislator.fec_id)+' at key '+str(l_key))
		
		return str(l_key)
		
		
class SunlightLegislators(SunlightPipeline):

	def run(self, **kwargs):
		sunlight.apikey = self.config['api_key']

		## Get legislators
		legislators = sunlight.legislators.getList(**kwargs)

		## Spawn legislator pipelines
		for legislator in legislators:
			yield SunlightLegislator(legislator=legislator.__dict__)