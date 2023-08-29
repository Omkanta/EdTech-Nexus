from django.db import models

class Instructor(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    department = models.CharField(max_length=50)
    email = models.EmailField()
    contact_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name
