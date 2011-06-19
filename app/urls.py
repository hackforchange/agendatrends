# -*- coding: utf-8 -*-

""" URL definitions. """

from tipfy.routing import Rule
from tipfy.routing import HandlerPrefix

rules = [

	HandlerPrefix('agendatrends.handlers.', [
	
		Rule('/', name='landing', handler='main.LandingHandler'),
		Rule('/topics', name='topics', handler='site.topics.Landing'),
		Rule('/people', name='people', handler='site.people.Landing'),
		Rule('/trends', name='trends', handler='site.trends.Landing'),
		Rule('/sources', name='sources', handler='site.sources.Landing'),		
		
		Rule('/topic/<path:filters>', name='topic', handler='main.TopicHandler'),
		Rule('/api/topic/<path:filters>', name='api', handler='api.ApiTopicHandler'),
		Rule('/api/legislators', name='api', handler='api.ApiLegislatorHandler')
	
	])
]
