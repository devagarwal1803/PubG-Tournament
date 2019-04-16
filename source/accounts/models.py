from django.db import models
from django.contrib.auth.models import User

class Activation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True)
    mobile = models.IntegerField(default=0)
    m1 = models.CharField(max_length=20)
    m2 = models.CharField(max_length=20)
    m3 = models.CharField(max_length=20)
    m4 = models.CharField(max_length=20)
    show=models.BooleanField(default=False)