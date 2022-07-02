from django.shortcuts import render
from myApp.forms import UserForm, UserProfileInfoForm

## Login Imports
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

def index(request):
    return render(request, 'myApp/index.html')

## This decorator makes sure that a user is logged in
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered = False

    if request.method == 'POST':
        userForm = UserForm(data = request.POST)
        profileForm = UserProfileInfoForm(data = request.POST)

        if userForm.is_valid() and profileForm.is_valid():

            user = userForm.save() # Save User
            user.set_password(user.password) # Hash Password
            user.save() # Saves it

            # This is needed for the one to one relationship with User model
            profile = profileForm.save(commit=False)
            profile.user = user 

            # For files such as images, csv's, etc. you need to find these through REQUEST.FILES
            if 'profilePic' in request.FILES:
                profile.profilePic = request.FILES['profilePic']
            
            profile.save()

            registered = True
        else:
            print(userForm.errors, profileForm.errors)
    else:
        userForm, profileForm = UserForm(), UserProfileInfoForm()

        
    return render(request, 'myApp/registration.html', context = {'userForm': userForm, 
                                                                 'profileForm':profileForm, 
                                                                 'registered': registered
                                                                 })
        

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Your account has been deactivated')
        else:
            print('Failed Login')
            print('Username: ', username)
            return HttpResponse('Invalid Login Details Supplied')
    else:
        return render(request, 'myApp/login.html')

