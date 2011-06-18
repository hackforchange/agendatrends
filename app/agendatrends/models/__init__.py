## NDB
from ndb import model

## App Engine
from google.appengine.ext import db as ldb
from google.appengine.ext import blobstore

## ProvidenceClarity
from ProvidenceClarity.struct.util import DictProxy
from ProvidenceClarity.data.core.model import Model as ProvidenceClarityModel
from ProvidenceClarity.data.core.model import NDBModel as ProvidenceClarityNDBModel
from ProvidenceClarity.data.core.polymodel import PolyPro as ProvidenceClarityPolyModel


###### ====== Property Classes ====== ######

## NDB/New Style
ndb = DictProxy({
		'StringProperty' : model.StringProperty,
		'TextProperty' : model.TextProperty,
		'BlobProperty' : model.BlobProperty,
		'IntegerProperty' : model.IntegerProperty,
		'FloatProperty' : model.FloatProperty,
		'BooleanProperty': model.BooleanProperty,
		'DateTimeProperty': model.DateTimeProperty,
		'TimeProperty': model.TimeProperty,
		'GeoPtProperty': model.GeoPtProperty,
		'KeyProperty' : model.KeyProperty,
		'UserProperty': model.UserProperty,
		'StructuredProperty' : model.StructuredProperty,
		'LocalStructuredProperty' : model.LocalStructuredProperty,
		'ComputedProperty' : model.ComputedProperty,
		'GenericProperty': model.GenericProperty
})

## DB/Old Style
db = DictProxy({
		'StringProperty' : ldb.StringProperty,
		'ByteStringProperty' : ldb.ByteStringProperty,		
		'BooleanProperty' : ldb.BooleanProperty,
		'IntegerProperty' : ldb.IntegerProperty,
		'FloatProperty' : ldb.FloatProperty,
		'DateTimeProperty' : ldb.DateTimeProperty,
		'DateProperty' : ldb.DateProperty,
		'TimeProperty' : ldb.TimeProperty,
		'ListProperty' : ldb.ListProperty,
		'StringListProperty' : ldb.StringListProperty,
		'ReferenceProperty' : ldb.ReferenceProperty,
		'BlobReferenceProperty' : blobstore.BlobReferenceProperty,
		'UserProperty' : ldb.UserProperty,
		'BlobProperty' : ldb.BlobProperty,
		'TextProperty' : ldb.TextProperty,
		'CategoryProperty' : ldb.CategoryProperty,
		'LinkProperty' : ldb.LinkProperty,
		'EmailProperty' : ldb.EmailProperty,
		'GeoPtProperty' : ldb.GeoPtProperty,
		'IMProperty' : ldb.IMProperty,
		'PhoneNumberProperty' : ldb.PhoneNumberProperty,
		'PostalAddressProperty' : ldb.PostalAddressProperty,
		'RatingProperty' : ldb.RatingProperty
})


def property_classes(flatten=False):
	class_lists = [db, ndb]
	p_list = []
	for class_list in class_lists:
		for p_name, p_class in class_list.items():
			if flatten is True: p_list.append(p_name)
			if flatten is False: p_list.append((p_name, p_class))
	return p_list
			
	

###### ====== Root Models ====== ######

## DB/Old Style Model
class AGTModel(ProvidenceClarityModel):
	pass
	

## NDB/New Style Model
class NDBModel(ProvidenceClarityNDBModel):
	pass
	

## PolyModel
AGTPolyModel = ProvidenceClarityPolyModel