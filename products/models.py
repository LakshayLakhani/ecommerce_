from __future__ import unicode_literals

from django.core.urlresolvers import reverse

from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=50, default=29.99)
    sale_price = models.DecimalField(decimal_places=2, max_digits=50, \
                                    default=29.99, null=True, blank=True)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('title', 'slug')

    def __unicode__(self):
        # return "this is a product"
        return self.title

    def get_price(self):
        return self.price

    def get_absolute_url(self):
        # return reverse("single_product", args=[self.slug])

        return reverse("single_product", kwargs={"slug":self.slug})
        # return "%s/" %(self.slug)

class ProductImage(models.Model):
    product = models.ForeignKey(Product)
    image = models.ImageField(upload_to='products/images/')
    featured = models.BooleanField(default=False)
    thumbnaill = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.product.title
