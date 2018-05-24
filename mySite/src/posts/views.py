from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def post_create(request):
	return HttpResponse("<h1>create</h1>")

def post_detail(request):
	return HttpResponse("abc")

def post_list(request):
	return HttpResponse("abc")

def post_update(request):
	return HttpResponse("abc")

def post_delete(request):
	return HttpResponse("abc")
