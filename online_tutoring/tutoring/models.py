from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Tutor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject)
    bio = models.TextField()

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Session(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateTimeField()
    duration = models.DurationField()
    notes = models.TextField(blank=True, null=True)
