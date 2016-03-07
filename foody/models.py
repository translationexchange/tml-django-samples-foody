# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Categories(models.Model):
    #id = models.IntegerField(primary_key=True)  # AutoField?
    key = models.TextField(blank=True, null=True)  # This field type is a guess.
    name = models.TextField(blank=True, null=True)  # This field type is a guess.
    locale = models.TextField(blank=True, null=True)  # This field type is a guess.
    featured_index = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        managed = False
        db_table = 'categories'

    def __str__(self):
        return self.name.encode('utf-8')


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Recipes(models.Model):
    #id = models.IntegerField(primary_key=True)  # AutoField?
    category =  models.ForeignKey(Categories, on_delete=models.CASCADE)#models.IntegerField(blank=True, null=True)
    key = models.TextField(blank=True, null=True)  # This field type is a guess.
    name = models.TextField(blank=True, null=True)  # This field type is a guess.
    locale = models.TextField(blank=True, null=True)  # This field type is a guess.
    description = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)  # This field type is a guess.
    preparation = models.TextField(blank=True, null=True)
    featured_index = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        managed = False
        db_table = 'recipes'

    def create_directions(self, directions):
        for item in directions:
            if item:
                direction = Directions.objects.create(
                        recipe=self,
                        description=item,
                        index=directions.index(item)+1
                        )

    def create_ingredients(self, ingredients):
        for item in ingredients:
            if item['name']:
                ingredient = Ingredients.objects.create(
                        recipe=self,
                        quantity=item['quantity'],
                        name=item['name'],
                        measurements=item['measurements'],
                        index=ingredients.index(item)
                        )

class Ingredients(models.Model):
    #id = models.IntegerField(primary_key=True)  # AutoField?
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    quantity = models.TextField(blank=True, null=True)  # This field type is a guess.
    name = models.TextField(blank=True, null=True)  # This field type is a guess.
    measurements = models.TextField(blank=True, null=True)  # This field type is a guess.
    index = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        managed = False
        db_table = 'ingredients'

class Directions(models.Model):
    #id = models.IntegerField(primary_key=True)  # AutoField?
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        managed = False
        db_table = 'directions'


class SchemaMigrations(models.Model):
    version = models.TextField(unique=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'schema_migrations'
