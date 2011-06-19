# -*- coding: utf-8 -*-

""" URL definitions. """

from tipfy.routing import Rule
from tipfy.routing import HandlerPrefix

rules = [

	HandlerPrefix('agendatrends.handlers.', [
	
		Rule('/', name='landing', handler='main.LandingHandler'),
		Rule('/topic/<path:filters>', name='topic', handler='main.TopicHandler')
	
	])
]
