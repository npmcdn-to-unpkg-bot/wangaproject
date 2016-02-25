from django.shortcuts import render,render_to_response, redirect, RequestContext, HttpResponse,HttpResponseRedirect
import json
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.template.context_processors import csrf
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from .models import UserProfile
from django.contrib.auth.decorators import login_required
# Create your views here.

def Login_page(request):
	return render(request,"conta/login.html")
"""
def Logout(request):
	return render(request,"conta/login.html")
"""
def Register(request):
	return render(request,"conta/register.html")

@login_required
def Profile(request):
	return render(request,"conta/profile.html")

@csrf_protect
def Login(request):
	errors 	 = []
	password = None
	username = None
	
	if request.user.is_authenticated():
		return redirect('conta/profile')
	
	if request.method == "POST":
		try:
			data = json.loads(request.body.decode('utf-8'))
			username = data["username"] #request.POST['email']
			password = data["password"] #request.POST['password']
		except:
			#data = json.loads(request.body.decode('utf-8'))
			username = request.POST['username']
			password = request.POST['password']

		if username is None:
			errors.append({'message': "You need to enter a username"})
			if  password is None:
				errors.append({'message': "You need to enter an email address"})
		if not errors:
			user = authenticate(username=username, password=password)
			if user is not None :
				if user.is_active:
					login(request, user)
					#log = True;
					errors.append({"success":"Your are successfully logged in"})
					resp = {"log":True, "success":errors}
					return HttpResponse(status=200, content_type='application/json', content=json.dumps({"log":True, "success":"Your are successfully logged in"}))
				else:
					errors.append({"failure": "Your account has been disabled"})
					resp = {"log":False, "errors":errors}
					return HttpResponse(status=200, content_type='application/json', content=json.dumps(resp))
			else:
				errors.append({"failure": "Unable to login with provided credentials"})
				resp = {"login":False, "errors":errors}
				return HttpResponse(status=200, content_type='application/json', content=json.dumps({"login":False, "errors":errors}))
	return render_to_response(request,"conta/Login_page.html")#,{"errors":errors})

@csrf_exempt
def Register(request):
	if request.user.is_authenticated():
		return redirect(reverse('/index'))
	errors = []
	if request.method == "POST":
		post = json.loads(request.body.decode('utf-8'))
		firstname =  post['firstname']
		lastname = post['lastname']
		password =  post['password']
		confirm =  post['confirm']
		email =  post['email']
		username =  post['email']
		print(firstname,lastname ,password,email)
		if not firstname:
			errors.append({'message': "You need to enter a firstname"})
		if not lastname:
			errors.append({'message': "You need to enter a lastname"})
		if not email:
			errors.append({'message': "You need to enter an email address"})
		if password and password != confirm:
			errors.append({'message': 'Your passwords do not match!'})
		if not errors:
			try:
				user = User.objects.create_user(username,email)
				user.save()
				user.set_password(password)
				user.first_name(firstname)
				user.last_name(lastname)
				user.save()
				profile = UserProfile.objects.get_or_create(user = user)
				profile.save()
				resp = {"registered":True, "errors":errors}
				return HttpResponse(status=200, content_type='application/json', content=json.dumps(resp))
			except Exception as ex:
				errors.append({'message': ex})
				resp = {"registered":False, "errors":errors}
				return HttpResponse(status=200, content_type='application/json', content=json.dumps(resp))
		else:
			resp = {"login":False, "errors":errors}
			return HttpResponse(status=200, content_type='application/json', content=json.dumps(resp))
	return render_to_response("conta/register.html", {'errors': errors}, RequestContext(request))

def Logout(request):
	logout(request)
	# Take the user back to the homepage.
	return HttpResponseRedirect('/index')
