from agendatrends.pipelines import AgendaTrendsPipeline


class ServicePipeline(AgendaTrendsPipeline):
	
	config = {}
	service = None

	def __init__(self, *args, **kwargs):
		
		if hasattr(self, 'service') and self.service is not None:
			if hasattr(self, 'config') and isinstance(self.config, dict) and len(self.config) > 0:
				for c in self.config:
					args = []
					kwargs = {}
					if isinstance(c, tuple):
						kwargs[c[0]] = c[1]
					else:
						args.append(c)
				self.service = self.service(*args, **kwargs)
			else:
				self.service = self.service()
				
		super(ServicePipeline, self).__init__(*args, **kwargs)