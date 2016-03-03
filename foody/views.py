from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView, UpdateView, RedirectView
from . import models
from django.core.urlresolvers import reverse

class IndexView(TemplateView):
    template_name = 'foody/index.html'
    context_object_name = 'latest_question_list'

    def get_context_data(self, * args, ** kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['ran'] = range(1,19)

        context['categories'] = models.Categories.objects.all()

        return context

class ShowRecipeView(TemplateView):
    def get_context_data(self, * args, ** kwargs):
        context = super(ShowRecipeView, self).get_context_data(**kwargs)
        context['ran'] = range(1,19)
        context['recipe'] = models.Recipes.objects.get(id=self.kwargs.get('pk', None))
        return context

class CreateRecipeView(CreateView):
    def get_success_url(self):
        return reverse('show_recipe', kwargs={'pk':self.object.id})

class UpdateRecipeView(UpdateView):
    def get_context_data(self, * args, ** kwargs):
        context = super(UpdateRecipeView, self).get_context_data(**kwargs)
        context['directions'] = models.Directions.objects.filter(recipe=self.object)
        context['ingredients'] = models.Ingredients.objects.filter(recipe=self.object)
        return context

    def get_success_url(self):
        return reverse('show_recipe', kwargs={'pk':self.object.id})


class DeleteRecipeView(RedirectView):
    def get_redirect_url(self, *a, **kw):
        return reverse('index')

    def get(self, request, *a, **kw):
        recipe_id = kw.get('pk')
        models.Recipes.objects.get(id=recipe_id).delete()
        return super(DeleteRecipeView, self).get(request, *a, **kw)

