from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	is_guardia = models.BooleanField(default=False)
	is_admin = models.BooleanField(default=False)
	telefono = models.CharField(max_length=32, null=True, blank=True)

	def __str__(self):
		return self.user.first_name