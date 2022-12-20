from django.shortcuts import render


def index(request):

    return render(request, 'main/index.html')

def lazy(request):

    return render(request, 'main/lazy.html')

def about(request):

    return render(request, 'main/about.html')

def connect(request):

    return render(request, 'main/connect.html')

def products(request):

    return render(request, 'main/products.html')

def support(request):

    return render(request, 'main/support.html')