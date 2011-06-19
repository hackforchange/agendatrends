from google.appengine.ext import db
from agendatrends import models as m


def add_political_parties():

	from agendatrends.models.politics import PoliticalParty

	models = []
	models.append(PoliticalParty(key_name='D', name='Democratic Party', plural='Democrats', singular='Democrat'))
	models.append(PoliticalParty(key_name='R', name='Republican Party', plural='Republicans', singular='Republican'))
	models.append(PoliticalParty(key_name='I', name='Independent Party', plural='Independents', singular='Independent'))

	return db.put(models)
	
	
def add_states():
	
	from agendatrends.models.geo import USState
	
	models = []
	models.append(USState(key_name="AL",abbreviation="AL",fullname="Alabama",primary_name="Alabama",name=["AL","Alabama"]))
	models.append(USState(key_name="AK",abbreviation="AK",fullname="Alaska",primary_name="Alaska",name=["AK","Alaska"]))
	models.append(USState(key_name="AZ",abbreviation="AZ",fullname="Arizona",primary_name="Arizona",name=["AZ","Arizona"]))
	models.append(USState(key_name="AR",abbreviation="AR",fullname="Arkansas",primary_name="Arkansas",name=["AR","Arkansas"]))
	models.append(USState(key_name="CA",abbreviation="CA",fullname="California",primary_name="California",name=["CA","California"]))
	models.append(USState(key_name="CO",abbreviation="CO",fullname="Colorado",primary_name="Colorado",name=["CO","Colorado"]))
	models.append(USState(key_name="CT",abbreviation="CT",fullname="Connecticut",primary_name="Connecticut",name=["CT","Connecticut"]))
	models.append(USState(key_name="DE",abbreviation="DE",fullname="Delaware",primary_name="Delaware",name=["DE","Delaware"]))
	models.append(USState(key_name="FL",abbreviation="FL",fullname="Florida",primary_name="Florida",name=["FL","Florida"]))
	models.append(USState(key_name="GA",abbreviation="GA",fullname="Georgia",primary_name="Georgia",name=["GA","Georgia"]))
	models.append(USState(key_name="HI",abbreviation="HI",fullname="Hawaii",primary_name="Hawaii",name=["HI","Hawaii"]))
	models.append(USState(key_name="ID",abbreviation="ID",fullname="Idaho",primary_name="Idaho",name=["ID","Idaho"]))
	models.append(USState(key_name="IL",abbreviation="IL",fullname="Illinois",primary_name="Illinois",name=["IL","Illinois"]))
	models.append(USState(key_name="IN",abbreviation="IN",fullname="Indiana",primary_name="Indiana",name=["IN","Indiana"]))
	models.append(USState(key_name="IA",abbreviation="IA",fullname="Iowa",primary_name="Iowa",name=["IA","Iowa"]))
	models.append(USState(key_name="KS",abbreviation="KS",fullname="Kansas",primary_name="Kansas",name=["KS","Kansas"]))
	models.append(USState(key_name="KY",abbreviation="KY",fullname="Kentucky",primary_name="Kentucky",name=["KY","Kentucky"]))
	models.append(USState(key_name="LA",abbreviation="LA",fullname="Louisiana",primary_name="Louisiana",name=["LA","Louisiana"]))
	models.append(USState(key_name="ME",abbreviation="ME",fullname="Maine",primary_name="Maine",name=["ME","Maine"]))
	models.append(USState(key_name="MD",abbreviation="MD",fullname="Maryland",primary_name="Maryland",name=["MD","Maryland"]))
	models.append(USState(key_name="MA",abbreviation="MA",fullname="Massachusetts",primary_name="Massachusetts",name=["MA","Massachusetts"]))
	models.append(USState(key_name="MI",abbreviation="MI",fullname="Michigan",primary_name="Michigan",name=["MI","Michigan"]))
	models.append(USState(key_name="MN",abbreviation="MN",fullname="Minnesota",primary_name="Minnesota",name=["MN","Minnesota"]))
	models.append(USState(key_name="MS",abbreviation="MS",fullname="Mississippi",primary_name="Mississippi",name=["MS","Mississippi"]))
	models.append(USState(key_name="MO",abbreviation="MO",fullname="Missouri",primary_name="Missouri",name=["MO","Missouri"]))
	models.append(USState(key_name="MT",abbreviation="MT",fullname="Montana",primary_name="Montana",name=["MT","Montana"]))
	models.append(USState(key_name="NE",abbreviation="NE",fullname="Nebraska",primary_name="Nebraska",name=["NE","Nebraska"]))
	models.append(USState(key_name="NV",abbreviation="NV",fullname="Nevada",primary_name="Nevada",name=["NV","Nevada"]))
	models.append(USState(key_name="NH",abbreviation="NH",fullname="New Hampshire",primary_name="New Hampshire",name=["NH","New Hampshire"]))
	models.append(USState(key_name="NJ",abbreviation="NJ",fullname="New Jersey",primary_name="New Jersey",name=["NJ","New Jersey"]))
	models.append(USState(key_name="NM",abbreviation="NM",fullname="New Mexico",primary_name="New Mexico",name=["NM","New Mexico"]))
	models.append(USState(key_name="NY",abbreviation="NY",fullname="New York",primary_name="New York",name=["NY","New York"]))
	models.append(USState(key_name="NC",abbreviation="NC",fullname="North Carolina",primary_name="North Carolina",name=["NC","North Carolina"]))
	models.append(USState(key_name="ND",abbreviation="ND",fullname="North Dakota",primary_name="North Dakota",name=["ND","North Dakota"]))
	models.append(USState(key_name="OH",abbreviation="OH",fullname="Ohio",primary_name="Ohio",name=["OH","Ohio"]))
	models.append(USState(key_name="OK",abbreviation="OK",fullname="Oklahoma",primary_name="Oklahoma",name=["OK","Oklahoma"]))
	models.append(USState(key_name="OR",abbreviation="OR",fullname="Oregon",primary_name="Oregon",name=["OR","Oregon"]))
	models.append(USState(key_name="PA",abbreviation="PA",fullname="Pennsylvania",primary_name="Pennsylvania",name=["PA","Pennsylvania"]))
	models.append(USState(key_name="RI",abbreviation="RI",fullname="Rhode Island",primary_name="Rhode Island",name=["RI","Rhode Island"]))
	models.append(USState(key_name="SC",abbreviation="SC",fullname="South Carolina",primary_name="South Carolina",name=["SC","South Carolina"]))
	models.append(USState(key_name="SD",abbreviation="SD",fullname="South Dakota",primary_name="South Dakota",name=["SD","South Dakota"]))
	models.append(USState(key_name="TN",abbreviation="TN",fullname="Tennessee",primary_name="Tennessee",name=["TN","Tennessee"]))
	models.append(USState(key_name="TX",abbreviation="TX",fullname="Texas",primary_name="Texas",name=["TX","Texas"]))
	models.append(USState(key_name="UT",abbreviation="UT",fullname="Utah",primary_name="Utah",name=["UT","Utah"]))
	models.append(USState(key_name="VT",abbreviation="VT",fullname="Vermont",primary_name="Vermont",name=["VT","Vermont"]))
	models.append(USState(key_name="VA",abbreviation="VA",fullname="Virginia",primary_name="Virginia",name=["VA","Virginia"]))
	models.append(USState(key_name="WA",abbreviation="WA",fullname="Washington",primary_name="Washington",name=["WA","Washington"]))
	models.append(USState(key_name="WV",abbreviation="WV",fullname="West Virginia",primary_name="West Virginia",name=["WV","West Virginia"]))
	models.append(USState(key_name="WI",abbreviation="WI",fullname="Wisconsin",primary_name="Wisconsin",name=["WI","Wisconsin"]))
	models.append(USState(key_name="WY",abbreviation="WY",fullname="Wyoming",primary_name="Wyoming",name=["WY","Wyoming"]))

	return db.put(models)
	

def discourse_sources():
	
	from agendatrends.models.sources import DiscourseSource
	
	models = []
	models.append(DiscourseSource(key_name='cnn', name='CNN'))
	models.append(DiscourseSource(key_name='msnbc', name='MSNBC'))
	models.append(DiscourseSource(key_name='npr', name='NPR'))
	models.append(DiscourseSource(key_name='fox', name='Fox News'))
	models.append(DiscourseSource(key_name='nyt', name='New York Times'))
	
	return db.put(models)
	
	
scaffolding = [add_political_parties, add_states, discourse_sources]