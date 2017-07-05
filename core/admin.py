# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Product, Vote


class VoteInline(admin.StackedInline):
    model = Vote
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    inlines = [VoteInline]


admin.site.register(Product, ProductAdmin)
