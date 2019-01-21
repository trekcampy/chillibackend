from django.db import models

# Create your models here.
class ChilliHeat(models.Model):
    chilli_type = models.CharField(max_length=200)
    scoville_value = models.IntegerField(default=0)

    def __str__(self):
        return self.chilli_type
        