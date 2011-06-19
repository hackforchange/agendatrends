from agendatrends.handlers import WebHandler

from agendatrends.models.geo import USState

from agendatrends.pipelines.services.sunlight import SunlightLegislators


class DefaultData(WebHandler):
	
	def get(self):
		
		from agendatrends.dev.default_data import scaffolding

		msg = []
		for fn in scaffolding:
			result = fn()
			msg.append('Created '+str(len(result))+' keys with fn '+str(fn.__name__))
		
		return self.response(reduce(lambda x, y: x+y, ['<li>'+result+'</li>' for result in msg]))
		

class FillDatastore(WebHandler):
	
	def get(self):
		
		states = USState.all().fetch(55)
		
		pipelines = []
		for state in states:
			pipelines.append(SunlightLegislators(state=state.key().name()).start(queue_name='data'))
			
		return self.response(reduce(lambda x, y: x+y, ['<li>Started pipeline <b>'+str(pipeline)+'</b></li>']))