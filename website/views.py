from django.shortcuts import render
from django.core.mail import send_mail
from website import models


def home(request):
	return render(request , 'home.html' , {})

def contact(request):
	if request.method == "POST":
		message_name = request.POST['message-name']
		message_email =request.POST['message-email']
		message = request.POST['message']

		send_mail(
			'massage from ' + message_name , #subject
			 message , #message
			 message_email , #email form
			 ['mojtabanorouzi1378mn@gmail.com'] ,  


			)

		return render(request , 'contact.html' , {'message_name': message_name , })

	else:
		return render(request , 'contact.html' , {})
def about(request):
	return render(request , 'about.html' , {})

def pricing(request):
	return render(request , 'pricing.html' , {})

def service(request):
	return render(request , 'service.html' , {})


def apointment(request):
	if request.method == "POST":
		your_name=     request.POST['your-name'] 
		your_phone=    request.POST['your-phone'] 
		your_email=    request.POST['your-email'] 
		your_address=  request.POST['your-address'] 
		your_scheldule=request.POST['your-scheldule'] 
		your_time=     request.POST['your-time'] 
		your_message=  request.POST['your-message'] 

		appointment = "Name :  " + your_name + "         " +  " Phone:  " + your_phone + "              " +  " Email:  " + your_email + "             "+  " Address:   "+ your_address + "              " +  " Scheldule:  " + your_scheldule  + "            "+ " Time:   " + your_time  + "                               "+ "message:  "+ your_message
		
		send_mail(
			' Appointment Request', 
			 appointment , #message
			 your_message , #email form
			 ['mojtabanorouzi1378mn@gmail.com'] ,  


			)
		models.appointment(your_name=your_name,
							your_phone= your_phone,
							your_email= your_email,
							your_address=your_address,
							your_scheldule=your_scheldule,
							your_time=your_time,
							your_message=your_message).save()
		

		return render(request , 'apointment.html' , {'your_name': your_name ,
			'your_phone': your_phone ,
			'your_email': your_email ,
			'your_address': your_address ,
			'your_scheldule': your_scheldule ,
			'your_time': your_time ,
			'your_message': your_message ,


		 })

	else:
		return render(request , 'home.html' , {})