from django.db import models

class Rating(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])  
    experience = models.TextField()

    def __str__(self):
        return f"Rating from {self.name}"
