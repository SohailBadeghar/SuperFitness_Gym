from fiteness_web.settings import EMAIL_HOST_USER
from django.core.mail import EmailMultiAlternatives
import uuid



def send_account_activation_email(email,token):
   
    subject = 'Your foreget password link '
    messages = f'Hi, click on this link to reset your password http://127.0.0.1:8000/accounts/change_password/{token}/'
    recipient_list = [email]
    email_from = EMAIL_HOST_USER    
    Msg = EmailMultiAlternatives(subject,messages,email_from,recipient_list)
    Msg.send()
    return True 


