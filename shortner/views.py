from django.shortcuts import render, redirect
from .models import ShortenedURL
from .utils import create_shortened_url


def index(request):
    if request.method == 'POST':
        long_url = request.POST.get('long_url')
        short_url = create_shortened_url()

        # Save the short URL to the database
        shortened_url = ShortenedURL(long_url=long_url, short_url=short_url)
        shortened_url.save()

        return render(request, 'shortened.html', {'short_url': short_url})
    else:
        return render(request, 'index.html')


def redirect_url(request,short_url):
    shortened_url = ShortenedURL.objects.get(short_url=short_url)
    long_url = shortened_url.long_url
    return redirect(long_url)
