from django.http import HttpResponse
from django.shortcuts import render

def home(request):
  # return HttpResponse("Hello world, you are on a home page.")

  return render(request, 'website/index.html')

def about(request):
  # return HttpResponse("Hello world, you are on a about page.")

  return render(request, 'website/about.html')


def contact(request):
  # return HttpResponse("Hello world, you are on a contact page.")

  return render(request, 'website/contact.html')
