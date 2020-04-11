from django.contrib import admin
from website import models
# Register your models here.
class appointment_admin(admin.ModelAdmin):
	"""docstring for appointment_admin"""
	list_display=('your_name' , 'your_phone', 'your_email' , 'your_scheldule' , 'your_time')
	
		
admin.site.register(models.appointment , appointment_admin)
