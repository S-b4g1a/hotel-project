from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

import django.contrib.auth as auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from Accounts.forms import SignInForm, SignUpForm


def AccountSignUp(request):
    template = loader.get_template("account_sign_up.html")
    context = {"page_state": 0, "form": SignUpForm()}

    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if not form.is_valid():
            context["page_state"] = 2
            return HttpResponse(template.render(context, request))
        
        data = form.cleaned_data

        if User.objects.filter(username=data['username']):
            context["page_state"] = 3
            return HttpResponse(template.render(context, request))
        
        if User.objects.filter(email=data['email']):
            context["page_state"] = 4
            return HttpResponse(template.render(context, request))
        
        if data['password'] != data['repeat_password']:
            context["page_state"] = 5
            return HttpResponse(template.render(context, request))


        user = User.objects.create_user(username=data["username"],
                                        email=data["email"],
                                        first_name=data["first_name"],
                                        last_name=data["last_name"],
                                        password=data["password"])
        
        user.save()

    return HttpResponse(template.render(context, request))


def AccountSignIn(request):
    template = loader.get_template("account_sign_in.html")
    context = {"page_state": 0, "form": SignInForm()}

    if request.method == 'POST':
        form = SignInForm(request.POST)

        if not form.is_valid():
            context["page_state"] = 2
            return HttpResponse(template.render(context, request))
            
        data = form.cleaned_data
        user = auth.authenticate(username=data['username'], password=data['password'])

        if user is None:
            context["page_state"] = 3
            return HttpResponse(template.render(context, request))
        
        auth.login(request, user)
        context["page_state"] = 1
                
    return HttpResponse(template.render(context, request))


@login_required(login_url='/account/sign_in')
def AccountSignOut(request):
    template = loader.get_template("account_sign_out.html")
    context = {}
    if request.method == "POST":
        auth.logout(request)
        return redirect('/homepage')

    return HttpResponse(template.render(context, request))


@login_required(login_url='/account/sign_in')
def AccountView(request):
    template = loader.get_template("account_view.html")
    context = {}
    return HttpResponse(template.render(context, request))


@login_required(login_url='/account/sign_in')
def AccountDelete(request):
    template = loader.get_template("account_delete.html")
    context = {}
    if request.method == "POST":
        user = request.user
        User.objects.filter(id=user.id).delete()
        return redirect('/homepage')
    return HttpResponse(template.render(context, request))
