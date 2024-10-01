from django.db import models

class Menu(models.Model):
    date = models.DateField(unique=True)  # Ensures a menu exists only for a specific date
    starter = models.CharField(max_length=255)
    main_course = models.CharField(max_length=255)
    dessert = models.CharField(max_length=255)

    def __str__(self):
        return f"Menu for {self.date}"


class Order(models.Model):
    user_id = models.CharField(max_length=255) 
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    selection = models.CharField(max_length=255) 
    timestamp = models.DateTimeField(auto_now_add=True)