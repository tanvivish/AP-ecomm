from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def layout(request):
	return render(request,'layout.html')
