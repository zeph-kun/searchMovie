from django.shortcuts import render
import requests
import os
SECRET_KEY = os.getenv('SECRET_KEY')


def index(request):
    return render(request, "index.html")


def get_request():
    url = f"http://www.omdbapi.com/?apikey={SECRET_KEY}&"
    res = requests.get(url=url)
    print(res.status_code)