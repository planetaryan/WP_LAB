from django.db import models

# Model for WORKS table
class Works(models.Model):
    person_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.person_name} works at {self.company_name}"

# Model for LIVES table
class Lives(models.Model):
    person_name = models.CharField(max_length=100)
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.person_name} lives in {self.city}"
