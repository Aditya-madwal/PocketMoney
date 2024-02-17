from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .models import *
# Create your views here.

# -------------------AUTHENTICATION-----------------------

def loginview(request) :
    if request.user.is_authenticated :
        return redirect(homeview)

    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)

        if user is not None :
            login(request, user)
            return redirect(homeview)
        else :
            messages.error(request, "username or password is incorrect")
            pass
    return render(request, 'login.html', {})

def signupview(request) :

    if request.user.is_authenticated :
        return redirect(homeview)

    if request.method == 'POST' :
        email = request.POST['email']
        username = request.POST['name']
        password = request.POST['password']
        if email and username and password :
            user = User.objects.create_user(username=username, password=password, email = email)
            user.save()
            return redirect(loginview)
        return redirect(signupview)
    return render(request, 'signup.html', {})
    

def logoutview(request) :
    logout(request)
    return redirect(loginview)


# -------------------PRODUCTION-----------------------

@login_required(login_url=loginview)
def homeview(request) :
    wallets_list = wallets.objects.filter(owner = request.user)

    context = {
        'wallets' : wallets_list,
    }

    if request.method == 'POST' :
        walletname = request.POST['walletname']
        if walletname :
            newwallet = wallets.objects.create(name = walletname, owner = request.user, balance = 0, income = 0, expense = 0)
            newwallet.save()
        return redirect(homeview)
    return render(request, 'home.html', context=context)
    
@login_required(login_url=loginview)
def walletview(request,pk) :
    w = wallets.objects.get(id = pk)
    transactions_list = transactions.objects.filter(wallet = w)
    context = {
        'wallet' : w,
        'transactions' : transactions_list,
    }

    if request.method == "POST" :
        category = request.POST['category']
        amount = request.POST['amount']
        label = request.POST['label']
        if category and amount and label :
            if label == 'Income' :
                w.balance += int(amount)
                w.income += int(amount)
                w.save()
                t = transactions.objects.create(category = category, label = '1', amount = amount, wallet = w)
                t.save()
                return redirect(f"/wallet/{pk}")
            else :
                w.balance -= int(amount)
                w.expense += int(amount)
                w.save()
                t = transactions.objects.create(category = category, label = '2', amount = amount, wallet = w)
                t.save()
                return redirect(f"/wallet/{pk}")
        return redirect(f"/wallet/{pk}")
    return render(request, 'wallet.html', context=context)


@login_required(login_url=loginview)
def deleteview(request, pk) :
    w = wallets.objects.get(id = pk)

    if request.user != w.owner :
        return redirect(f"/wallet/{w.id}")

    w.delete()
    return redirect(homeview)


@login_required(login_url=loginview)
def delete_tview(request, pk) :
    t = transactions.objects.get(id = pk)

    if request.user != t.wallet.owner :
        return redirect(f"/wallet/{t.wallet.id}")

    wallet = t.wallet
    if t.label == '1' :
        wallet.income -= t.amount
        wallet.balance -= t.amount
        wallet.save()
    else :
        wallet.balance += t.amount
        wallet.expense -= t.amount
        wallet.save()
    t.delete()
    return redirect(f'/wallet/{wallet.id}')

@login_required(login_url=loginview)
def resetview(request, pk) :
    w = wallets.objects.get(id = pk)

    if request.user != w.owner :
        return redirect(f"/wallet/{w.id}")

    w.balance = 0
    w.income = 0
    w.expense = 0

    transactions.objects.filter(wallet = w).delete()

    w.save()
    return redirect(f'/wallet/{pk}')