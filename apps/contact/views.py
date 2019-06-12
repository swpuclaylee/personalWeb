from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect
# Create your views here.


def contact(request):
    return render(request, 'contact-us.html', locals())


def add(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        date = request.POST.get("date")
        theme = request.POST.get("theme")
        message = request.POST.get("message")
        CommentMessageModel.objects.create(
            name=name,
            email=email,
            phone=phone,
            date=date,
            theme=theme,
            message=message
        )

    return HttpResponseRedirect('/contact/sucess/')


def sucess(request):
    return render(request, 'sucess.html')