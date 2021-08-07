from django.db import models

# Create your models here.
STATUS = (
    ('PENDING', 'PENDING'),
    ('BOUGHT', 'BOUGHT'),
    ('NOT AVAILABLE', 'NOT AVAILABLE'),
    )
class Groce(models.Model):
    

    item_name = models.CharField(max_length=200)
    item_quantity = models.CharField(max_length=200)
    date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    item_status = models.CharField(max_length=200, null=True, choices=STATUS)
    
    def __str__(self):
        return self.item_name