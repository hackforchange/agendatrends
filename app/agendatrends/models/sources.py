from agendatrends import models as m


class Source(m.AGTModel):

	name = m.db.StringProperty()
	regex = m.db.StringProperty()
	homepage = m.db.StringProperty()
	
	updated = m.db.DateTimeProperty(auto_now=True)
	created = m.db.DateTimeProperty(auto_now_add=True)	
	
	
class DiscourseSource(Source):
	pass