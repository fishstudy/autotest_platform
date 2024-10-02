from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse

from blog.models import Article


def index(request):
    return HttpResponse("Hello, world. You're at the chery index.")


