from agendatrends import models as m


class Source(m.AGTModel):

	name = m.db.StringProperty()
	regex = m.db.StringProperty()
	homepage = m.db.StringProperty()
	
	
class DiscourseSource(Source):
	pass