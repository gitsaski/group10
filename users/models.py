from django.db import models

class Employer(models.Model):
    full_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_number = models.CharField(max_length=20)
    company_location = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=128)  # Assuming password will be hashed before saving
    company_description = models.TextField()

    def __str__(self):
        return self.company_name
