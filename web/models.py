from django.db import models
import uuid

# Create your models here.
class Flan(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    image = models.URLField()
    precio = models.CharField(max_length=12)
    slug= models.SlugField()
    is_private = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f'{self.name} {self.precio}'
    
class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    customer_email = models.EmailField()
    subject = models.CharField(max_length=64)
    customer_name = models.CharField(max_length=64)
    message = models.TextField()
    
    def __str__(self) -> str:
        return f'{self.customer_name} {self.customer_email} {self.subject}'