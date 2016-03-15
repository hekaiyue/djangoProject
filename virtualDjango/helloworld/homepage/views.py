from django.shortcuts import render
from .models import *
from .forms import *

############AUTHENTICATION IMPORTS#############
from django.contrib.auth import authenticate,login,logout
from helloworld import settings
from django.contrib.auth.models import User
#########################

# Create your views here.
def home(request):
	all_object = blog.objects.all()

	form = BlogPost(request.POST or None) #this is our form

	###SAVE code begins
	if form.is_valid():
		poop = form.save(commit='false')
		poop.save()
	###SAVE code ends

	template="home.html"
	context={
		"form": form,
		"all_object":all_object,
		"zero_object":all_object[0],
		"first_object":all_object[1],
	}
	return render(request,template,context)