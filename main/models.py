from django.db import models

# Create your models here.
import uuid
from django.db import models

class Products(models.Model):
    CATEGORY_CHOICES = [
        ('update', 'Update'),
        ('regional', 'Regional'),
        ('global', 'Global'),
        ('antique', 'Antique'),
        ('special', 'Special'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    stock = models.IntegerField(default=0)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='global')
    thumbnail = models.URLField(blank=True, null=True)
    product_views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    @property
    def is_product_popular(self):
        return self.product_views > 20
        
    def increment_views(self):
        self.product_views += 1
        self.save()