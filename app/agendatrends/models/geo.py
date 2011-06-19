from agendatrends import models as m


class USState(m.AGTModel):

	name = m.db.StringListProperty()
	abbreviation = m.db.StringProperty()
	
	updated = m.db.DateTimeProperty(auto_now=True)
	created = m.db.DateTimeProperty(auto_now_add=True)	
	
	
class District(m.AGTModel):

	state = m.db.ReferenceProperty(USState, collection_name='districts')

	updated = m.db.DateTimeProperty(auto_now=True)
	created = m.db.DateTimeProperty(auto_now_add=True)	