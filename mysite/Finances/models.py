from django.db import models

# Create your models here.


class Expense(models.Model):
    date = models.DateField()
    category = models.CharField(max_length=15)
    description = models.CharField(max_length=40)
    value = models.DecimalField(decimal_places=2, max_digits=8)

    def __str__(self):
        return " ".join([str(self.date), self.category, str(self.value)])


class Income(models.Model):
    date = models.DateField()
    category = models.CharField(max_length=15)
    description = models.CharField(max_length=40)
    value = models.DecimalField(decimal_places=2, max_digits=8)

    def __str__(self):
        return " ".join([str(self.date), self.category, str(self.value)])