from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.student_id} - {self.name}"