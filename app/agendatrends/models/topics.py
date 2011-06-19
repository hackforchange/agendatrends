from agendatrends import models as m


class Topic(m.AGTPolyModel):

	value = m.db.StringListProperty()
	calais_id = m.db.StringProperty()

	updated = m.db.DateTimeProperty(auto_now=True)
	created = m.db.DateTimeProperty(auto_now_add=True)	
	

class SubjectTopic(Topic):
	pass
	
	
class PersonTopic(Topic):
	pass