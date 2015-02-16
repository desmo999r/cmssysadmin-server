from django.core.exceptions import ObjectDoesNotExist
from piston.handler import BaseHandler
from piston.utils import rc
from cmsracklayout.racklayout.models import RackLayout

class RackLayoutHandler(BaseHandler):
	allowed_methods = ('GET',)
	model = RackLayout

	def read(self, request, rack_name, switch_port, motherboard=1):
		base = RackLayout.objects
		try:
			machine = base.filter(rack_name__exact=rack_name.lower()) \
					.get(switch_port__exact=switch_port)
			return machine
		except ObjectDoesNotExist as err:
			print err
			resp = rc.NOT_FOUND
			resp.write("No layout information for rack %s on switch port %s" % (rack_name, switch_port))
			return resp
