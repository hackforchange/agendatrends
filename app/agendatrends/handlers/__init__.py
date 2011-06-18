import os
import config
import simplejson

# Tipfy Imports
from tipfy.app import Response
from tipfy.handler import RequestHandler
from tipfyext.jinja2 import Jinja2Mixin

# ProtoRPC Imports
from protorpc import remote

# App Engine Imports
from google.appengine.api import oauth
from google.appengine.api import users
from google.appengine.api import backends
from google.appengine.api import namespace_manager


class WebHandler(RequestHandler, Jinja2Mixin):
	
	response = Response
	
	def render(self, template, content_type='text/html', **context):
		
		## Merge specific render context with base context
		template_context = self.generateBaseContext()
		for key, value in context.items():
			template_context[key] = value
		
		output_filter = unicode
		if self._outputConfig()['minify'] is True:
			import slimmer
			if content_type == 'text/html':
				output_filter = slimmer.html_slimmer
			elif content_type == 'text/javascript':
				from slimmer.js_function_slimmer import slim as slimjs
				output_filter = slimjs
			elif content_type == 'text/css':
				output_filter = slimmer.css_slimmer		
		
		return self.response(output_filter(self.render_template(template, **context)))
		

	def generateBaseContext(self):
		
		params = {}
		
		# Bind Tipfy & util functions
		params['link'] = self.url_for
		params['config'] = config.config.get
		params['environ'] = os.environ.get		
		
		# Bind App Engine functions
		params['api'] = {
			'oauth': oauth,
			'users': {
				'is_user_admin': users.is_current_user_admin,
				'current_user': users.get_current_user,
				'create_login_url': users.create_login_url,				
				'create_logout_url': users.create_logout_url,
			},
			'backends': backends,
			'multitenancy': namespace_manager
		}
		
		return params


	def _outputConfig(self):
		return config.config.get('agendatrends.output')