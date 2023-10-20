from django.db import models

# job class
class Job(models.Model):
    text = models.CharField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)
    
    # return string representation of a model
    def __str__(self) -> str:
        return self.text

