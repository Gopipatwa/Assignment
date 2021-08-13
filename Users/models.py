from django.db import models

# Create your models here.

class User(models.Model):
	first_name = models.CharField(max_length=50,blank=True)
	last_name = models.CharField(max_length=50,blank=True)
	email = models.EmailField()
	password = models.CharField(max_length=50,blank=True)
	username = models.CharField(primary_key=True,max_length=50)

	def __str__(self):
		return self.username+" "+self.email

class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True)
	text = models.TextField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.user)+"  "+self.text
