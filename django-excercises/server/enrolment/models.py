from django.db import models
from django.utils.timezone import utc

# Create your models here.
class student(models.Model):

	f_name = models.TextField()
	l_name = models.TextField()
	time = models.DateTimeField()
	import datetime
	time.default = datetime.datetime.now(utc)
