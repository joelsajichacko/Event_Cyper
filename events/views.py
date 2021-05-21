from django.shortcuts import render, HttpResponse
from events.models import Events

# Create your views here.


def home(request):
    return render(request, 'index.html')


def events(request):
    events= Events.objects.all()
    context = {'events': events}
    return render(request, "events.html", context)


def contact(request):
    return render(request, "contact.html")


def signup(request):
    return render(request, "signup.html")


def eventpost(request, slug):
    events = Events.objects.filter(slug=slug).first()
    context = {'events': events}
    return render(request, "eventpost.html", context)


def login(request):
    return render(request, "login.html")