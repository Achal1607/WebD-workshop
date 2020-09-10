from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm

from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.contrib.auth.models import User

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm, UserInfoForm
from .models import UserInfo


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('users:home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('users:login')

        context = {'form': form}
        return render(request, 'basic_app/registration.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('users:home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('users:home')
            else:
                messages.info(request, 'Username OR password is incorrect')
        return render(request, 'basic_app/login.html')


def updatePage(request):
    if not request.user.is_authenticated:
        return redirect('users:login')
    else:
        user_info = request.user
        form = UserInfoForm()
        u=''
        if UserInfo.objects.filter(user=User.objects.get(username=user_info.username)).first():
            u=UserInfo.objects.get(user=User.objects.get(username=user_info.username))
        
        if request.method == 'POST':  
            form = UserInfoForm(data=request.POST)
            if form.is_valid():
                if UserInfo.objects.filter(user=User.objects.get(username=user_info.username)).first():
                    u=UserInfo.objects.get(user=User.objects.get(username=user_info.username))
                    u.delete()
                userdetail=form.save(commit=False)
                userdetail.user=User.objects.get(username=user_info.username)
                userdetail.save()
                return redirect('users:home')
            else:
                messages.info(request, "Error Updating Your Information...")
                return redirect('users:home')
        else:
            context={'form':form}
            if u:
                context['u']=u
            return render(request, 'basic_app/update.html', context)

def logoutUser(request):
    logout(request)
    return redirect('users:login')


def home(request):
    return render(request, 'base.html', {})
