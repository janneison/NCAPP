from datetime import *
import os
from django.conf import settings
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
import uuid
from django.utils.deconstruct import deconstructible

class functions:	

	@staticmethod
	def path_and_rename(path,prefix):
		def wrapper(instance, filename):			
			filename, file_extension = os.path.splitext(filename)			
			# get filename
			fecha=datetime.now()
			filename = '{}_{}{}{}{}{}{}{}'.format(prefix,fecha.year,fecha.month,fecha.day,fecha.hour,fecha.minute,fecha.second, file_extension)		

			return os.path.join(path, filename)
		return wrapper	


@deconstructible
class RandomFileName(object):
	def __init__(self, path):
		self.path = os.path.join(path, "%s%s")

	def __call__(self, _, filename):		
		extension = os.path.splitext(filename)[1]
		# fecha=datetime.now()
		# filename = '{}_{}{}{}{}{}{}'.format(fecha.year,fecha.month,fecha.day,fecha.hour,fecha.minute,fecha.second)		
		return self.path % (uuid.uuid4(), extension)