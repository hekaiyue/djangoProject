from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
	all_object = blog.objects.all()

	template="home.html"
	context={
		"all_object":all_object,
		"zero_object":all_object[0],
		"first_object":all_object[1],
	}
	return render(request,template,context)