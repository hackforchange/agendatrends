from agendatrends import models as m

from agendatrends.models.tags import Tag
from agendatrends.models.topics import Topic


class TagOccurenceCount(m.AGTPolyModel):

	total = m.db.IntegerProperty(default=0)
	tag = m.db.ReferenceProperty(Tag, collection_name='occurrences')
	topic = m.db.ReferenceProperty(Topic, collection_name='occurrences')	

	updated = m.db.DateTimeProperty(auto_now=True)
	created = m.db.DateTimeProperty(auto_now_add=True)
	

class YearCount(OccurrenceCount):

	plural = 'years'
	singular = 'year'
	subunit = 'month'

	number = db.IntegerProperty()


class MonthCount(OccurenceCount):

	plural = 'months'
	singular = 'month'
	subunit = 'day'
	
	year = db.ReferenceProperty(Month, collection_name='months')

	
class DayCount(OccurenceCount):

	plural = 'days'
	singular = 'day'
	subunit = 'hour'
	
	month = db.ReferenceProperty(Month, collection_name='days')