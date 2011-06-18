from agendatrends.handlers import WebHandler


class Landing(WebHandler):

    def get(self):

        return self.render('main/landing.html', topics = ['healthcare', 'babies', 'iraq'])
