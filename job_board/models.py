from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    employer = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    job_type = models.CharField(
        max_length=50,
        choices=[
            ('FULL_TIME', 'Full Time'),
            ('PART_TIME', 'Part Time'),
            ('CONTRACT', 'Contract'),
            ('TEMPORARY', 'Temporary'),
            ('INTERN', 'Internship'),
        ],
        default='FULL_TIME'
    )
    salary = models.IntegerField(blank=True, null=True)
    qualifications = models.TextField(blank=True)
    application_deadline = models.DateField(null=True, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    # return string representation of a model
    def __str__(self) -> str:
        return self.title
