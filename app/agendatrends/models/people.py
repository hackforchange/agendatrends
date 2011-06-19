from agendatrends import models as m


class Person(m.AGTPolyModel):
	
	title = m.db.StringProperty()
	firstname = m.db.StringProperty()
	middlename = m.db.StringProperty()
	lastname = m.db.StringProperty()
	name_suffix = m.db.StringProperty()
	nickname = m.db.StringProperty()
	gender = m.db.StringProperty(choices=['M', 'F'])	
	birthdate = m.db.StringProperty()
	
	
class Legislator(Person):
	
	## Political stuff
	party = m.db.StringProperty()
	state = m.db.StringProperty()
	district = m.db.StringProperty()
	in_office = m.db.BooleanProperty()
	
	## Contact
	phone = m.db.PhoneNumberProperty()
	fax = m.db.PhoneNumberProperty()
	website = m.db.StringProperty()
	webform = m.db.StringProperty()
	email = m.db.StringProperty()
	congress_office = m.db.StringProperty()
	
	## External ID's
	bioguide_id = m.db.StringProperty()
	votesmart_id = m.db.StringProperty()
	fec_id = m.db.StringProperty()
	govtrack_id = m.db.StringProperty()
	crp_id = m.db.StringProperty()
	eventful_id = m.db.StringProperty()
	congresspedia = m.db.StringProperty()
	twitter_id = m.db.StringProperty()
	official_rss = m.db.StringProperty()
	youtube_url = m.db.StringProperty()