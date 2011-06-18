import logging
from agendatrends.pipelines.services import ServicePipeline


class SunlightLegislators(ServicePipeline):

	def run(self):
		logging.info('Sunlight legislators ran successfully!!')
	
	
class SunlightLegislator(ServicePipeline):

	def run(self):
		logging.info('Sunlight legislator ran successfully!!')
