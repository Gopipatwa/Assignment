from django.db import models

# Create your models here.

class Product(models.Model):
	product_name = models.CharField(max_length=100,blank=True)
	weight = models.FloatField(blank=True)
	price = models.FloatField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.product_name