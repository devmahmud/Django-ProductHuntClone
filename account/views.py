from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from product.models import Product
from django.http import Http404


@login_required
def index(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        products = Product.objects.filter(hunter=user_id)
        return render(request, 'account/index.html', {'products': products})


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'account/signup.html', {'error_message': "Username is already taken !"})

            except User.DoesNotExist:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('account:index')
        else:
            return render(request, 'account/signup.html', {'error_message': "Password doesn\'t matched"})

    else:
        return render(request, 'account/signup.html')


def signin(request):
    if request.method == 'POST':
        user = auth.authenticate(
            username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('account:index')
        else:
            return render(request, 'account/signin.html', {'error_message': "username or password is incorrect"})
    else:
        return render(request, 'account/signin.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('product:index')


@login_required
def delete(request, p_id):
    if request.user.is_authenticated:
        user_id = request.user.id
        try:
            product = get_object_or_404(Product, pk=p_id, hunter=user_id)
        except Http404:
            return redirect('account:index')
        else:
            product.delete()
            return redirect('account:index')
    return redirect('account:index')
