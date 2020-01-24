from django.shortcuts import render,redirect

# Create your views here.

def main_view(request):

	return render(request,'index.html')