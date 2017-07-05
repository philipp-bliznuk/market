# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models import Avg
from django.core.validators import MinValueValidator, MaxValueValidator


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __unicode__(self):
        return 'Product: {self.name}'.format(self=self)

    @property
    def rating(self):
        return self.votes.aggregate(rating=Avg('value')).get('rating', 0)


class Vote(models.Model):
    product = models.ForeignKey(Product, related_name='votes')
    value = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )

    def __unicode__(self):
        return '{self.product.name}: {self.value}'.format(self=self)
