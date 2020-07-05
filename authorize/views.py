import urllib
import smtplib
from django.shortcuts import render
from authorize.forms import SigninForm, SignupForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.http import JsonResponse
from xml.dom import minidom
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.conf import settings
from django.core.mail import send_mail,EmailMultiAlternatives
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.urls import reverse

def login_excluded(redirect_to):
    """ This decorator kicks authenticated users out of a view """ 
    def _method_wrapper(view_method):
        def _arguments_wrapper(request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect(redirect_to) 
            return view_method(request, *args, **kwargs)
        return _arguments_wrapper
    return _method_wrapper

def my_custom_send_email(toaddr,id):
    form_instance = User
    user_id = id
    user_name =User.objects.filter(id=user_id)
    subject = "🙌 Welcome to joint-access-programmer.com!"
    from_email = settings.EMAIL_HOST_USER
    with open(settings.BASE_DIR + "/templates/register_activate/sign_up_email.txt") as email_text:
        sign_up_message = email_text.read()
    message = EmailMultiAlternatives(subject=subject, body=sign_up_message,from_email=from_email, to=[toaddr] )
    html_template = get_template("register_activate/sign_up_email.html").render({ "user_id":user_id ,"user_name":user_name})
    message.attach_alternative(html_template, "text/html")
    message.send()


@login_excluded('/')
def login(request):
	title = "Log-in"
	template = "main/login.html"
	form = SigninForm()
	return render(request, template, {'form':form,'title':title})

def post_login(request):
    if request.method == 'POST' and request.is_ajax():
        form = SigninForm(request.POST)
        if form.is_valid():
            info = "success" 
            username = request.POST['username']
            password = request.POST['password']
            try:
                user = authenticate(username=User.objects.get(email=username), password=password)
            except:
                user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    return JsonResponse({"success":True, "info":info}, status=200)
        else:
            info = "failure"
            return JsonResponse({"success":False, "info":info}, status=400)
    return JsonResponse({"success":False}, status=400)

   

def signup(request):
    title = "Sign Up"
    template = "main/signup.html"
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST or None)
        if form.is_valid():
            info = "success" 
            user_instance = form.save()
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username,password=password)
            user.is_active = False
            user.save()
            id = user.id
            email = user.email
            try:
                my_custom_send_email(email, id)
            except TimeoutError:
                user.delete()
                network_error = "Check network, and try again"
                return render(request, template, {'form':form,'title':title, "network_error":network_error})
            except smtplib.SMTPNotSupportedError:
                user.delete()
                network_error = "Max user account reached. Try again in 24 hrs"
                return render(request, template, {'form':form,'title':title, "network_error":network_error})
            except:
                user.delete()
                network_error = "Oh gosh, something went wrong...."
                return render(request, template, {'form':form,'title':title, "network_error":network_error})
            return render(request,'register_activate/thankyou.html',{'title':'Thank You'})
        else:
            form_data = SignupForm(data=request.POST)
            def custom_return_data(field):
                 value = form_data[field].value()
                 return value
            first_name = custom_return_data("first_name")
            last_name = custom_return_data("last_name")
            username = custom_return_data("username")
            password = custom_return_data("password")
            verify_password = custom_return_data("verify_password")
            email = custom_return_data("email")
            context = {
                'form':form_data,
                'title':title,
                "first_name":first_name,
                "last_name":last_name,
                "username":username,
                "password":password,
                "verify_password":verify_password,
                "email":email
            }
            return render(request, template, context)
    return render(request, template, {'form':form,'title':title})




def activate(request):
    try:
        id = int(request.GET.get('id'))
        user = User.objects.get(id=id)
        request_username = user.username
        request_password = user.password
        user.is_active=True
        user.save()
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        auth_login(request, user)
        title = "Activate Account"
        context = {
        "title":title
        }
    except User.DoesNotExist:
       return redirect(reverse("authorize:signup")) 
    return render(request,'register_activate/activation.html',context)

