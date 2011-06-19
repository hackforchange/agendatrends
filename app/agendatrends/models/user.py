from agendatrends import models as m


class QuickLink(m.AGTModel):
	
	user = m.db.UserProperty(auto_current_user=True)
	full_link = m.db.StringProperty()
	
	updated = m.db.DateTimeProperty(auto_now=True)
	created = m.db.DateTimeProperty(auto_now_add=True)
	
	
class SearchHistory(m.AGTModel):

	user = m.db.UserProperty(auto_current_user=True)
	query = m.db.StringProperty()
	
	updated = m.db.DateTimeProperty(auto_now=True)
	created = m.db.DateTimeProperty(auto_now_add=True)