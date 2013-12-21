from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader, RequestContext
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from models import Note, NoteForm


class LoginForm(forms.Form):
	username = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput())

@login_required(login_url="/notes/index/")		
def dashboard(request):
	if request.method=="POST":
		d=request.POST.copy()
		d.update({'owner':request.user.id})
		form = NoteForm(d)
		if not form.is_valid():
			template=loader.get_template("dashboard.html")
			rc=RequestContext(request,{'form':NoteForm()})
			return HttpResponse(template.render(rc))	
		# save note to database
		note = form.save(commit=False)
		note.owner=request.user
		note.save()
		return redirect("dashboard")
	else:
		template=loader.get_template("dashboard.html")
		rc=RequestContext(request,{'form':NoteForm()})
		return HttpResponse(template.render(rc))

def index(request):
	#return HttpResponse("Hello, Notes")
	if request.method=="POST":
		form = LoginForm(request.POST)
		print "Received POST request!"
		if form.is_valid():
			print "FORM is valid."
			# register user
			username = request.POST['username']
			pwd = request.POST['password']
			user = authenticate(username=username,password=pwd)
			if user is not None:
				if user.is_active:
					login(request,user)
					return redirect("dashboard")
				else:
					return HttpResponse("account is inactive")
			else:
				user = User.objects.create_user(username, username, pwd)
				user = authenticate(username=username,password=pwd)
				login(request,user)
				return redirect("dashboard")
		else:
			print "FORM is invalid."
			template=loader.get_template("index.html")
			rc=RequestContext(request,{'username':'Mike', 'form':form})
			return HttpResponse(template.render(rc))
	else:
		template=loader.get_template("index.html")
		rc=RequestContext(request,{'username':'Mike', 'form':LoginForm()})
		return HttpResponse(template.render(rc))

def logmeout(request):
	logout(request)
	return redirect("index")

def example(request):
	#return HttpResponse("Hello, Notes")
	template=loader.get_template("example.html")
	temp=60
	rc=RequestContext(request,{
		'fruits':["banana","apples","berries","kiwis"],
		'username':'Mike',
		'temp':temp
		})
	return HttpResponse(template.render(rc))
