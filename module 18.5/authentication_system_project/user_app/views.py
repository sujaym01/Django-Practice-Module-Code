from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.forms import  AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login , update_session_auth_hash, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method == 'POST':
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Account Created Successfully')
            return redirect('homepage')
    else:
        register_form = forms.RegistrationForm()
    return render(request, 'user_app/register.html', {'form' : register_form, 'type' : 'Sign Up'})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username=user_name, password=user_pass)
            if user is not None:
                messages.success(request, 'Logged in Successfully')
                login(request, user)
                return redirect('profile')
            else:
                messages.warning(request, 'Login informtion incorrect')
                return redirect('register')
    else:
        form = AuthenticationForm()
    return render(request, 'user_app/register.html', {'form' : form, 'type' : 'Login'})

@login_required
def profile(request):
    return render(request, 'user_app/profile.html')


@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = forms.ChangeUserForm(request.POST, instance = request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('profile')
    else:
        profile_form = forms.ChangeUserForm(instance = request.user)
    return render(request, 'user_app/update_profile.html', {'form' : profile_form})


def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password Updated Successfully')
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'user_app/pass_change.html', {'form' : form})

@login_required
def pass_change2(request):
    if request.method == 'POST':
        form = SetPasswordForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password Updated Successfully')
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    else:
        form = SetPasswordForm(user=request.user)
    return render(request, 'user_app/pass_change.html', {'form' : form})



def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out  Successfully')
    return redirect('homepage')