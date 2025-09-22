from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # Link each note to a user
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
     
       return self.title
class MenuCategory(model.Model):
    name = models.CharField(max_length =100,unique=True)

    def __str_(self):
        return self.name
