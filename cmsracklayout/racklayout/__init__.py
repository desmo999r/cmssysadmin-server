from cmsracklayout.racklayout.models import RackLayout
from django.db.utils import DatabaseError
import csv
import os

path = os.path.dirname(__file__)

try:
	RackLayout.objects.all().delete()

	with open('%s/racklayout.csv' % path, 'rb') as csvfile:
		layoutreader = csv.reader(csvfile)
		for row in layoutreader:
			print row
			if len(row) < 4 or row[0].startswith('#'):
				continue
			entry = RackLayout(rack_name=row[0], u_number=int(row[1]), function=row[2])
			if row[3].strip():
				entry.switch_port = int(row[3])
			else:
				entry.switch_port = 0
			entry.save()
			print entry
except DatabaseError as err:
	print err
