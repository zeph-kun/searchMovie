from django.shortcuts import render
import requests
import os
from .forms import SearchForm
from .models import Movie


SECRET_KEY = os.getenv('SECRET_KEY')


def index(request):
    results = None
    movies = None
    form = SearchForm()
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["search"]
            movies = Movie.objects.filter(title__icontains=title)
            if not movies.exists():
                results = get_request(title)
                if results.get('Search') is not None:
                    for result in results.get('Search'):
                        formatted_year = Movie.format_year(result['Year'])
                        Movie.objects.create(
                            title=result['Title'],
                            year=formatted_year,
                            type=result['Type']
                        )

    return render(request, "index.html", {'form': form, 'results': results, 'movies': movies})


def get_request(title):
    url = f"http://www.omdbapi.com/?apikey={SECRET_KEY}&s={title}"
    res = requests.get(url=url)
    if res.status_code == 200:
        return res.json()
    else:
        print(f"Error: {res.status_code}")