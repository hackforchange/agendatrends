from agendatrends import models as m


class PoliticalParty(m.AGTModel):
	
	name = m.db.StringProperty()
	plural = m.db.StringProperty()
	singular = m.db.StringProperty()