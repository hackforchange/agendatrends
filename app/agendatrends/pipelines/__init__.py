import sys

if 'lib' not in sys.path:
	sys.path.insert(1, 'lib')

import config
import logging

from pipeline import common
from pipeline import pipeline

from google.appengine.ext import db
from google.appengine.api import xmpp
from google.appengine.api import channel
from google.appengine.api import memcache
from google.appengine.api import taskqueue

from agendatrends import models as m


#### ============== Pipeline Framework ============== ####
class AgendaTrendsPipeline(pipeline.Pipeline):

	m = m
	db = db
	_opts = {}
	memcache = memcache
	taskqueue = taskqueue
	pipeline = pipeline
	common = common

	def __init__(self, *args, **kwargs):
		
		import ndb
		
		## Reload NDB
		reload(ndb)
		self.ndb = ndb

		## Add Pipeline Config
		self.pipeline_config = config.config.get('momentum.fatcatmap.pipelines')

		super(AgendaTrendsPipeline, self).__init__(*args, **kwargs)
		
		
	def finalized(self):
		logging.info('Finalized pipeline '+str(self.root_pipeline_id)+' of class '+str(self.__class__.__name__))