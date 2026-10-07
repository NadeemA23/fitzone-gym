from django.db import models


class GymClass(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    instructor = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.name