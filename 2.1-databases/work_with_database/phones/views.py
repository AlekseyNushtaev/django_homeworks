from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phone_list = list(Phone.objects.all())
    if request.GET:
        if request.GET.get('sort') == 'name':
            phone_list.sort(key=lambda x: x.name)
        if request.GET.get('sort') == 'min_price':
            phone_list.sort(key=lambda x: x.price)
        if request.GET.get('sort') == 'max_price':
            phone_list.sort(key=lambda x: x.price, reverse=True)
    context = {'phones': phone_list}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = list(Phone.objects.filter(slug=slug))[0]
    context = {'phone': phone}
    return render(request, template, context)
