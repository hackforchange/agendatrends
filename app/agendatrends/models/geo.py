from agendatrends import models as m


class USState(m.AGTModel):

	name = m.db.StringListProperty()
	abbreviation = m.db.StringProperty()
	
	
class District(m.AGTModel):
	pass