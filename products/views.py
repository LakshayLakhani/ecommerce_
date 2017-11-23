# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.shortcuts import render, Http404
from django.core.urlresolvers import reverse
from .models import Product, ProductImage

def all(request):
    print "in all+++++++++++++++"
    all_products = Product.objects.all()
    context = {'products':all_products}
    template = 'products/all.html'
    return render(request, template, context)

def single(request, slug):
    try:
        print "in single+++++++++++++++"
        print slug
        product = Product.objects.get(slug=slug)
        images = product.productimage_set.all()
        # images = ProductImage.objects.filter(product=product)
        print images
        context = {'product':product, 'images':images}
        template = 'products/single.html'
        return render(request, template, context)
    except:
        raise Http404

def home(request):
    print "in lakshay+++++++++++++++"
    # if request.user.is_authenticated():
    #     username_is = "justin using context"
    #     context = {"username_is": request.user}
    # else:
    #     context = {"username_is": request.user}

    all_products = Product.objects.all()
    context = {'products':all_products}
    template = 'products/home.html'
    return render(request, template, context)
