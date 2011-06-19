from agendatrends.handlers import WebHandler


class Landing(WebHandler):
	
	def get(self):
		return self.response('<b>people</b>')