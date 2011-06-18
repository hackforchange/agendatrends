# -*- coding: utf-8 -*-
"""URL definitions."""
from tipfy.routing import Rule

rules = [
    Rule('/', name='hello-world', handler='agendatrends.handlers.HelloWorldHandler'),
    Rule('/pretty', name='hello-world-pretty', handler='agendatrends.handlers.PrettyHelloWorldHandler'),
]
