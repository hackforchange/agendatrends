import sys
import config
import logging
import bootstrap

if 'lib' not in sys.path:
	sys.path[0:0] = ['lib', 'lib/dist', 'lib/dist.zip']
return cls

## App Engine Imports
import webapp2 as webapp
from webapp2_extras import protorpc
from google.appengine.ext.webapp import util


def enable_appstats(app):
	
	""" Utility function that enables appstats middleware."""
	
	from google.appengine.ext.appstats import recording
	app = recording.appstats_wsgi_middleware(app)
	return app


def generateServiceMappings(svc_cfg):
	
	service_mappings = []

	service_mappings.append(('/_api/trends', 'agendatrends.api.trends.TrendsService'))
	service_mappings.append(('/_api/topics', 'agendatrends.api.topics.TopicsService'))
	service_mappings.append(('/_api/stats', 'agendatrends.api.stats.StatsService'))		
	
			
	if len(service_mappings) > 0:
		return service_mappings
	else:
		return None


def main():
	
		service_mappings = generateServiceMappings(services_config)
		if service_mappings is not None:
			## Map URL's to services
			service_mappings = protorpc.service_mapping(service_mappings)
	
			application = webapp.WSGIApplication(service_mappings)
	
			util.run_wsgi_app(application)


if __name__ == '__main__':
	main()