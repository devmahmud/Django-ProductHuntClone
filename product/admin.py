from django.contrib import admin
from .models import Product, Voter


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'pub_date', 'votes', 'hunter']
    search_fields = ['title', 'body']
    list_filter = ['pub_date', 'hunter']


@admin.register(Voter)
class VoterAdmin(admin.ModelAdmin):
    list_display = ['product', 'user']
