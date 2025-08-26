from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

# needs to be at top 
class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('toys_detail', kwargs={'pk': self.id})
# 

class Cat(models.Model):
    name = models.CharField(max_length=100) # Input textbox
    breed = models.CharField(max_length=100) # Input textbox
    description = models.TextField(max_length=250) # Input Text Area
    age = models.IntegerField() # Input Number
    image = models.ImageField(upload_to='main_app/static/uploads/', default='')
    toys = models.ManyToManyField(Toy)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'cat_id': self.id})

    def __str__(self):
        return self.name
    
    def number_of_meals(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)


class Feeding(models.Model):
    date = models.DateField()
    meal = models.CharField(max_length=1,choices=MEALS, default=MEALS[0][0])
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'cat_id': self.id})

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"


