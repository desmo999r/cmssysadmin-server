from django.conf.urls.defaults import *
from piston.resource import Resource
from cmsracklayout.api.handlers import RackLayoutHandler

racklayout_handler = Resource(RackLayoutHandler)

urlpatterns = patterns('',
		url(r'^racklayout/(?P<rack_name>[^/]+)/(?P<switch_port>\d+)/', racklayout_handler),
		)
