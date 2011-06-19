import urllib
import logging
import datetime
import simplejson as json

from agendatrends.models.sources import DiscourseSource
from agendatrends.models.discourse import NewsArticle
from agendatrends.pipelines.services import ServicePipeline

from agendatrends.pipelines.services.calais import OpenCalaisIdentify



class NewsForQuery(ServicePipeline):
	def run(self, query):

		yql_url = "http://query.yahooapis.com/v1/public/yql?q=use%20'http%3A%2F%2Flimechile.com%2Fhacks%2Fagendatrends%2Fagendatrends.xml'%20as%20agendatrends.news%3B%20select%20*%20from%20agendatrends.news%20where%20q%20%3D%20%22"+urllib.quote(query)+"%22&format=json&diagnostics=false&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"

		logging.info('GETTING NEWS FOR QUERY: '+str(query))
		logging.info('ENCODED: '+yql_url)
		
		respObj = self.urlfetch.fetch(yql_url)

		if respObj.status_code != 200:
			raise Exception('CODE WAS NOT 200! FAILURE: '+str(respObj.status_code))

		jsonContent = json.loads(respObj.content)

		articles = []
		
		logging.info('RESULT_COUNT: '+str(jsonContent['query']['count']))
		
		for i in range(jsonContent['query']['count']):

			## Pull out results
			unescapedUrl = jsonContent['query']['results']['result']['articles'][i]['url']
			publisher = jsonContent['query']['results']['result']['articles'][i]['publisher']
			date = jsonContent['query']['results']['result']['articles'][i]['date']
			
			## Find publisher
			source = DiscourseSource.get_by_key_name(publisher)
			if source is None:
				source = DiscourseSource(key_name=publisher.replace(' ', '-').lower(), name=publisher).put()
			
			n = NewsArticle.get_by_key_name(unescapedUrl)
			if n is None:
			
				## Create news article
				a = NewsArticle(key_name=unescapedUrl)
				a.url = unescapedUrl
				a.source = source
				#a.published = datetime.datetime.strptime(date, '%a %d %b %Y %I:%M:%S %z')
				articles.append(a)
			
				logging.info('URL for article %s: %s' % (query, unescapedUrl))
			else:
				logging.info('URL ALREADY FOUND IN DB! Skipping article, it has already been analyzed')

		articles = self.db.put(articles)
		for article in articles:
			logging.info('PUT ARTICLE: '+str(article))
			

		return str(articles)