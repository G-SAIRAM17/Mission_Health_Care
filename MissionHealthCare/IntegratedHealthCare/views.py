from django.shortcuts import render, redirect
from django.contrib import messages
from .models import patientSignUp
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
import random
import string

def psignup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        password = request.POST.get('password')
        reenterpassword = request.POST.get('reenterpassword')

        if password == reenterpassword:
            if User.objects.filter(username=name).exists():
                messages.info(request, 'Username already exists')
                return redirect('psignup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('psignup')
            else:
                patientSignUp.objects.create(name=name, age=age, gender=gender, email=email, mobile=mobile, address=address, password=password, reenterpassword=reenterpassword)

                # Send email (example)
                subject = 'Welcome to Our Service'
                from_email = settings.EMAIL_HOST_USER
                recipient_list = [email]
                text_content = f'Hi {name}, thank you for registering with us.'
                html_content = f'''
                <html>
                    <body>
                        <h1 style="color:blue;">Welcome, {name}!</h1>
                        <p>Thank you for registering with us. We are excited to have you on board.</p>
                        <p style="color:green;">Enjoy our services!</p>
                        <p>Best regards,</p>
                        <p>Mission Integrated Health Care</p>
                    </body>
                </html>
                '''

                msg = EmailMultiAlternatives(subject, text_content, from_email, recipient_list)
                msg.attach_alternative(html_content, "text/html")
                try:
                    msg.send()
                    messages.success(request, 'Registration successful. Confirmation email sent.')
                    return redirect('plogin') 
                except Exception as e:
                    messages.error(request, f'Failed to send email: {str(e)}')
                    return redirect('psignup')  
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('psignup')
    else:
        return render(request, 'patient_signup.html')


def plogin(request):
    return render(request, 'patient_login.html')
