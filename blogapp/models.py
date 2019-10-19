from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now



# Create your models here.
class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=30)
	text  = models.TextField()
	image = models.FileField(upload_to='images/',blank=True,null=True)
	date = models.DateTimeField(default=now, editable=False)

	def __str__(self):
		return self.name,self.logo
