from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import Ingredient, MenuItem, RecipeRequirements, Purchase
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def login(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username, password)
    if user is not None:
        login(request, user)

@login_required
def home(request):
    return render(request, "inventory/home.html")

class InventoryListView(LoginRequiredMixin,ListView):
    model = Ingredient
    template_name = "inventory/inventory.html"

class InventoryCreateView(LoginRequiredMixin,CreateView):
    model = Ingredient 
    fields = "__all__" 
   
class InventoryDeleteView(LoginRequiredMixin,DeleteView):
    model = Ingredient
    template_name = "inventory/ingredient_delete.html"
    success_url = reverse_lazy("inventory")

class InventoryUpdateView(LoginRequiredMixin,UpdateView):
    model = Ingredient
    fields = ["quantity"]
    template_name = "inventory/ingredient_update.html"
    success_url = reverse_lazy("inventory")

class MenuItemListView(LoginRequiredMixin,ListView):
    model = MenuItem
    template_name = "inventory/menuitems.html"

class RecipeRequirementsDetailView(LoginRequiredMixin,DetailView):
    model = MenuItem
    template_name = "inventory/recipe_requirements.html"

class MenuItemCreateView(LoginRequiredMixin,CreateView):
    model = MenuItem
    fields = "__all__"

class RecipeRequirementsCreateView(LoginRequiredMixin,CreateView):
    model = RecipeRequirements
    fields = "__all__"

class PurchaseCreateView(LoginRequiredMixin, CreateView):
    template_name = "inventory/purchase_form.html"
    model = Purchase
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu_items"] = [x for x in MenuItem.objects.all() if x.available()]
        return context
    
    def post(self, request):
        menu_item_id = request.POST["menuitem"]
        menu_item = MenuItem.objects.get(pk=menu_item_id)
        purchase = Purchase(menu_item=menu_item)
        
        requirements = menu_item.reciperequirements_set.all()
        for requirement in requirements:
            required_ingredient = requirement.ingredient
            required_ingredient.quantity -= requirement.quantity
            required_ingredient.save()
        
        purchase.save()
        return redirect("/purchase_created")

@login_required
def purchase_created(request):
    return render(request, "inventory/purchase_created.html")
   
class ViewPurchases(LoginRequiredMixin,TemplateView):
    template_name = "inventory/view_purchases.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["purchases"] = Purchase.objects.all()
        
        total_cost = 0
        for purchase in Purchase.objects.all():
            for requirement in purchase.menu_item.reciperequirements_set.all():
                total_cost += requirement.ingredient.price
            
        total_revenue = 0
        for purchase in Purchase.objects.all():
            total_revenue += purchase.menu_item.price
            
        context["cost"] = round(total_cost, 2)
        context["revenue"] = round(total_revenue, 2)
        context["profit"] = round(total_revenue - total_cost, 2)

        return context


    

    
