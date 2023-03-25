from django.db import models


# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    quantity = models.FloatField()
    price = models.FloatField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return "inventory"

class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()

    def available(self):
        return all(x.enough() for x in self.reciperequirements_set.all())

    def __str__(self):
        return self.name

class RecipeRequirements(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)

    def enough(self):
        return self.quantity <= self.ingredient.quantity

    def __str__(self):
        return f"{self.menu_item} requires {self.ingredient}"

class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.menu_item.name + " created at: " + str(self.timestamp)

   
    
    
