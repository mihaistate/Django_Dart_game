from django.db import models
from django.contrib.auth.models import User
#from django.apps import apps

class HelpRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pokemon = models.ForeignKey('myapp.Pokemon', on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user} - {self.pokemon}'
    