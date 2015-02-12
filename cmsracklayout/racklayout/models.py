from django.db import models

# Create your models here.
class RackLayout(models.Model):
	FUNCTIONS = ((u'srv', u'srv'), 
			(u'ru', u'ru'),
			(u'fu', u'fu'),
			(u'bu', u'bu'),
			(u'frlpc', u'frlpc'),
			(u'fmmpc', u'fmmpc'),
			(u'vmepc', u'vmepc'),
			(u'ctrl', u'ctrl'))
	rack_name = models.CharField("Rack name",max_length=20)
	u_number = models.IntegerField("Position in the rack (u number)")
	switch_port = models.IntegerField("Assigned switch port")
	function = models.CharField("Function of the server", max_length=20, choices=FUNCTIONS)
	# Some rack mounted servers have 4 motherboard
	motherboard = models.IntegerField('Embedded motherboard', default=1)
	# This field holds the machine's name built from the other fields
	# It's the primary as Django doesn't support compound primary keys.
	machine_name = models.CharField("Machine's name", max_length=40, primary_key=True)

	def __unicode__(self):
		return self.machine_name

	def save(self, *args, **kwargs):
		#Build up the machine's name
		self.machine_name = ("%s-%s-%02d-%02d" % (self.function, self.rack_name, self.u_number, self.motherboard)).lower()
		super(RackLayout, self).save(*args, **kwargs)
