# -*- coding: utf-8 -*-
import os
import json
from django import forms
from django.conf import settings
from django.utils.translation import ugettext as _
from . import models

class CreateRecipeForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Recipe Name')}))
    description = forms.CharField(widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': _('Description'),
            'rows': 4}), required=False)
    image = forms.CharField(widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Image Url')}), required=False)
    categories = forms.ModelChoiceField(queryset=models.Categories.objects.all(),
                                        widget=forms.Select(attrs={'class': 'form-control', 'onChange': 'verifyCategory(this)'}),
                                        required=False)

    new_category = forms.CharField(widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('New category name')}), required=False)
    preparation = forms.CharField(widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': _('Preparation instructions'),
            'rows': 8}), required=False)
    directions = forms.CharField(widget=forms.HiddenInput(attrs={}),required=False)
    ingredients = forms.CharField(widget=forms.HiddenInput(attrs={}),required=False)


    def __init__(self, instance=None, *args, **kwargs):
        self.instance = instance
        super(CreateRecipeForm, self).__init__(*args, **kwargs)


    def clean_name(self):
        name = self.cleaned_data.get('name')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        return description

    def clean_image(self):
        image = self.cleaned_data.get('image')
        return image

    def clean_categories(self):
        categories = self.cleaned_data.get('categories')
        return categories

    def clean_new_category(self):
        new_category = None;
        if self.cleaned_data['categories'] is None:
            if self.cleaned_data.get('new_category'):
                new_category = models.Categories.objects.create(
                         key=self.cleaned_data.get('new_category').lower(),
                         name=self.cleaned_data.get('new_category'))
            else:
                raise forms.ValidationError(_("You have forgotten Category!"))
        return new_category

    def clean_preparation(self):
        preparation = self.cleaned_data.get('preparation')
        return preparation

    def clean_directions(self):
        directions = []
        if self.cleaned_data.get('directions'):
            directions = json.loads(self.cleaned_data.get('directions'))
        return directions

    def clean_ingredients(self):
        ingredients = []
        if self.cleaned_data.get('ingredients'):
            ingredients = json.loads(self.cleaned_data.get('ingredients'))
        return ingredients


    def save(self):
        data = self.cleaned_data
        if data['categories'] is None:
            category = data['new_category']
        else:
            category = data['categories']
        recipe = models.Recipes(
                name=data['name'],
                description=data['description'],
                image=data['image'],
                locale='en',
                category=category,
                preparation=data['preparation']
                )
        recipe.save()
        recipe.create_directions(directions=data['directions'])
        recipe.create_ingredients(ingredients=data['ingredients'])
        return recipe

class UpdateRecipeForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Recipe Name')}))
    description = forms.CharField(widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': _('Description'),
            'rows': 4}), required=False)
    image = forms.CharField(widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Image Url')}), required=False)
    categories = forms.ModelChoiceField(queryset=models.Categories.objects.all(),
                                        widget=forms.Select(attrs={'class': 'form-control', 'onChange': 'verifyCategory(this)'}),
                                        required=False)

    new_category = forms.CharField(widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('New category name')}), required=False)
    preparation = forms.CharField(widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': _('Preparation instructions'),
            'rows': 8}), required=False)
    directions = forms.CharField(widget=forms.HiddenInput(attrs={}), required=False)
    ingredients = forms.CharField(widget=forms.HiddenInput(attrs={}), required=False)


    def __init__(self, instance=None, *args, **kwargs):
        self.instance = instance
        super(UpdateRecipeForm, self).__init__(*args, **kwargs)

        self.fields['name'].initial = self.instance.name
        self.fields['description'].initial = self.instance.description
        self.fields['image'].initial = self.instance.image
        self.fields['categories'].initial = self.instance.category
        self.fields['preparation'].initial = self.instance.preparation


    def clean_name(self):
        name = self.cleaned_data.get('name')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        return description

    def clean_image(self):
        image = self.cleaned_data.get('image')
        return image

    def clean_categories(self):
        categories = self.cleaned_data.get('categories')
        return categories

    def clean_new_category(self):
        new_category = None;
        if self.cleaned_data['categories'] is None:
            if self.cleaned_data.get('new_category'):
                new_category = models.Categories.objects.create(
                         key=self.cleaned_data.get('new_category').lower(),
                         name=self.cleaned_data.get('new_category'))
            else:
                raise forms.ValidationError(_("You have forgotten Category!"))
        return new_category

    def clean_preparation(self):
        preparation = self.cleaned_data.get('preparation')
        return preparation

    def clean_directions(self):
        directions = []
        if self.cleaned_data.get('directions'):
            directions = json.loads(self.cleaned_data.get('directions'))
        return directions

    def clean_ingredients(self):
        ingredients = []
        if self.cleaned_data.get('ingredients'):
            ingredients = json.loads(self.cleaned_data.get('ingredients'))
        return ingredients


    def save(self):
        data = self.cleaned_data
        recipe = self.instance
        recipe.name = data['name']
        recipe.description = data['description']
        recipe.image = data['image']
        recipe.preparation = data['preparation']

        if data['categories'] is None:
            recipe.category = data['new_category']
        else:
            recipe.category = data['categories']
        recipe.save()
        directions = models.Directions.objects.filter(recipe=self.instance).delete()
        ingredients = models.Ingredients.objects.filter(recipe=self.instance).delete()
        recipe.create_directions(directions=data['directions'])
        recipe.create_ingredients(ingredients=data['ingredients'])

        return recipe
