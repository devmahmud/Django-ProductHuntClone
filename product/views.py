from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, Voter


def index(request):
    products = Product.objects.order_by('-votes')

    return render(request, 'product/index.html', {'products': products})


@login_required
def add_product(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            product = Product()
            product.title = request.POST['title']
            product.body = request.POST['body']
            product.product_url = request.POST['url']
            product.icon = request.FILES['icon']
            product.image = request.FILES['image']
            product.hunter = request.user
            product.save()

            return redirect('/product/detail/'+str(product.id))
        else:
            return render(request, 'product/add.html', {'error_message': 'Please input all fields'})
    else:
        return render(request, 'product/add.html')


def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product/detail.html', {'product': product})


@login_required
def upvote(request, product_id):
    if request.method == 'POST':
        if Voter.objects.filter(user=request.user.id, product=product_id).exists():
            return redirect('/product/detail/'+str(product_id))
        else:
            product = get_object_or_404(Product, pk=product_id)
            product.votes += 1
            product.save()
            voter_count = Voter(product=product, user=request.user)
            voter_count.save()
            return redirect('/product/detail/'+str(product.id))

    return redirect('/product/detail/'+str(product_id))
