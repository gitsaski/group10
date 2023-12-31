from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    contact_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    # relationships with employee and employer
    employee = models.OneToOneField('Employee', on_delete=models.CASCADE, null=True, blank=True)
    employer = models.OneToOneField('Employer', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.username
    
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_number = models.CharField(max_length=20)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.full_name

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.full_name
