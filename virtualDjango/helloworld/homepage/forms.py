from django import forms 
from django.forms import ModelForm


################# Django imports abov

from .models import blog

################# model imports above


class BlogPost(ModelForm):
	class Meta:
		model = blog
		#fields = ['title','context']
		exclude = ['']
