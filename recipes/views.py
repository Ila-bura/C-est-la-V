from django.views.generic import (
    CreateView, ListView, DetailView, DeleteView, UpdateView)

from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)

from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Recipe
from .forms import RecipeForm

from django.contrib import messages


class Recipes(ListView):
    # Display all the recipes
    # Class used from Dee Mc YouTube tutorial

    template_name = "recipes/recipes.html"
    model = Recipe
    context_object_name = "recipes"

    def get_queryset(self, **kwargs):
        query = self.request.GET.get('q')
        recipes = self.model.objects.all()

        if not query:
            # Display a warning message only when users submit an empty search
            if 'q' in self.request.GET:
                messages.info(self.request, "Please type something.")

            return recipes

        recipes = self.model.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(method__icontains=query) |
            Q(dish_type__icontains=query)
        )

        if not recipes:
            messages.info(
                self.request, "Sorry, no recipes found for your search!")

        return recipes


class RecipeDetail(DetailView):
    # View one single recipe
    # Class used from Dee Mc YouTube tutorial

    template_name = "recipes/recipe_detail.html"
    model = Recipe
    context_object_name = "recipe"


class AddRecipe(LoginRequiredMixin, CreateView):
    # Check if user is logged in
    # Add recipe view
    # Class used from Dee Mc YouTube tutorial

    template_name = "recipes/add_recipe.html"
    model = Recipe
    form_class = RecipeForm
    success_url = "/recipes/"

    # Update with the logged in user name

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Recipe added successfully.')
        return super(AddRecipe, self).form_valid(form)


class DeleteRecipe(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    # Signed in users can delete their recipes
    # Class used from Dee Mc YouTube tutorial
    model = Recipe
    success_url = '/recipes/'

    def test_func(self):
        return self.request.user == self.get_object().user

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Recipe deleted successfully!')
        return super(DeleteRecipe, self).delete(request, *args, **kwargs)


class EditRecipe(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    # Signed in users can edit their recipes
    # Class used from Dee Mc YouTube tutorial
    template_name = "recipes/edit_recipe.html"
    model = Recipe
    form_class = RecipeForm
    success_url = '/recipes/'

    def test_func(self):
        return self.request.user == self.get_object().user

    def form_valid(self, form):
        messages.success(self.request, 'Recipe updated successfully!')
        return super(EditRecipe, self).form_valid(form)
