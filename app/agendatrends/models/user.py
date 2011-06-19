from agendatrends import models as m


class QuickLink(m.AGTModel):
	
	user = m.db.UserProperty(auto_current_user=True)
	full_link = m.db.StringProperty()
	
	
class SearchHistory(m.AGTModel):

	user = m.db.UserProperty(auto_current_user=True)
	query = m.db.StringProperty()