from django.urls import path, include 
from . import views

urlpatterns=[
    path("", views.home, name="home"),
    path("inventory", views.InventoryListView.as_view(), name="inventory"), 
    path("inventorycreate", views.InventoryCreateView.as_view(), name="inventory_create"),
    path("inventory_delete/<pk>", views.InventoryDeleteView.as_view(), name="inventory_delete"),
    path("inventory_update/<pk>", views.InventoryUpdateView.as_view(), name="inventory_update"),
    path("menuitems", views.MenuItemListView.as_view(), name="menu_items"),
    path("recipe_requirements/<pk>", views.RecipeRequirementsDetailView.as_view(), name="recipe_requirements"),
    path("menu_item_create", views.MenuItemCreateView.as_view(), name="menu_item_create"),
    path("recipe_requirements_create", views.RecipeRequirementsCreateView.as_view(), name="recipe_requirements_create"),
    path("purchase_create", views.PurchaseCreateView.as_view(), name="purchase_create"),
    path("purchase_created", views.purchase_created, name="purchase_created"),
    path("view_purchases", views.ViewPurchases.as_view(), name="view_purchases"),
    path("accounts/", include("django.contrib.auth.urls")),
]
