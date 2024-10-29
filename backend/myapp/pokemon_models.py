from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    moves = models.JSONField()
    abilities = models.JSONField()
    types = models.JSONField()
    staff_id = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name
      