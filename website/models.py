from django.db import models
import uuid


class appointment(models.Model):
	"""docstring for appointment"""
	your_name=     models.CharField(max_length=100)
	your_phone=    models.CharField(max_length=100)
	your_email=    models.EmailField(max_length=100) 
	your_address=  models.CharField(max_length=300)
	your_scheldule=models.CharField(max_length=100) 
	your_time=     models.CharField(max_length=100)
	your_message=  models.TextField(max_length=100)

	def __str__(self):
		return self.your_name
		
		
