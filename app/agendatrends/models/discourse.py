from agendatrends import models as m

from agendatrends.models.sources import DiscourseSource


class Discourse(m.AGTModel):
	pass
	
	
class NewsArticle(Discourse):

	title = m.db.StringProperty()
	snippet = m.db.TextProperty()
	url = m.db.StringProperty()
	source = m.db.ReferenceProperty(DiscourseSource, collection_name='discourse')	

	published = m.db.DateTimeProperty()
	updated = m.db.DateTimeProperty(auto_now=True)
	created = m.db.DateTimeProperty(auto_now_add=True)