from agendatrends.pipelines import AgendaTrendsPipeline


class ServicePipeline(AgendaTrendsPipeline):
	
	config = {}
	service = None

	def __init__(self, *args, **kwargs):
		
		if hasattr(self, 'service') and self.service is not None:
			if hasattr(self, 'config') and isinstance(self.config, dict) and len(self.config) > 0:
				self.service = self.service(**self.config)
			else:
				self.service = self.service()
				
		super(ServicePipeline, self).__init__(*args, **kwargs)