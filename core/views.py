from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import HeroSection, Service, Project, TeamMember, AboutSection, ContactInfo, ContactPage

def home(request):
    context = {
        'hero': HeroSection.objects.first(),
        'services': Service.objects.all(),
        'projects': Project.objects.all(),
        'team': TeamMember.objects.all(),
        'about': AboutSection.objects.first(),
        'contact': ContactInfo.objects.first(),
    }
    return render(request, 'core/home.html', context)

def projects(request):
    context = {
        'projects': Project.objects.all()
    }
    return render(request, 'core/projects.html', context)

def services_view(request):
    context = {'services': Service.objects.all()}
    return render(request, 'core/services.html', context)

def team(request):
    context = {'team': TeamMember.objects.all()}
    return render(request, 'core/team.html', context)

def career_view(request):
    return render(request, 'core/career.html')

def pricing_view(request):
    return render(request, 'core/pricing.html')

def contact_view(request):
    context = {
        'contact': ContactInfo.objects.first(),
        'page': ContactPage.objects.first(),
    }
    return render(request, 'core/contact.html', context)

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'core/login.html', {'error': 'Invalid credentials'})

    return render(request, 'core/login.html')
