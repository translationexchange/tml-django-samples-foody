"""foody URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views, forms, models
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^$', views.IndexView.as_view(template_name='foody/index.html'), name="index"),
    url(r'^recipe/show/(?P<pk>\d+)/$', views.ShowRecipeView.as_view(template_name='foody/show_recipe.html'), name='show_recipe'),
    url(r'^recipe/create/$',views.CreateRecipeView.as_view(template_name='foody/create.html', form_class=forms.CreateRecipeForm), name='create_recipe'),
    url(r'^recipe/update/(?P<pk>\d+)/$',views.UpdateRecipeView.as_view(template_name='foody/update.html', form_class=forms.UpdateRecipeForm, model=models.Recipes), name='update_recipe'),
    url(r'^recipe/delete/(?P<pk>\d+)/$', views.DeleteRecipeView.as_view(), name='delete_recipe')
]
