import agendatrends.models as m

from agendatrends.models.topics import Topic
from agendatrends.models.discourse import Discourse


class Tag(m.AGTModel):
	
	topic = m.db.ReferenceProperty(Topic, collection_name='tags')
	discourse = m.db.ReferenceProperty(Discourse, collection_name='tags')