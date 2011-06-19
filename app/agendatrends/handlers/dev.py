from agendatrends.handlers import WebHandler


class DefaultData(WebHandler):
	
	def get(self):
		
		from agendatrends.dev.default_data import scaffolding

		msg = []
		for fn in scaffolding:
			result = fn()
			msg.append('Created '+str(len(result))+' keys with fn '+str(fn.__name__))
		
		return self.response(reduce(lambda x, y: x+y, ['<li>'+result+'</li>' for result in msg]))