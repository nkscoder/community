from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from pprint import pprint
# Create your views here.

def index(request):
    return HttpResponse("Hello, You are at the core index.")


def CreateUser(request):
    if request.method == 'GET':
        all_form = AllForm()

    if request.method == 'POST':
        # pprint(request.POST['password'])

        user = User.objects.create_user(username=request.POST['email'],
                                        email=request.POST['email'],
                                        password=request.POST['password'])

        up = UserProfile()
        up.user = user
        up.gender = request.POST['gender']
        up.save()
        return  HttpResponse('chal rha hai')

    return render(request, 'register.html', { "all_form":all_form})