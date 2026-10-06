from django.shortcuts import render
from .models import Main_banner, Movie


def base(request):
    return render(request, "base.html")


def navigation(request):
    return render(request, "navigation.html")


def home(request):
    main_banners = Main_banner.objects.all()
    movies = Movie.objects.all()
    context = {
        'main_banners': main_banners,
        'movies': movies,
    }
    return render(request, "home.html", context)


def footer(request):
    return render(request, "footer.html")