from django.db import models

# Create your models here.


class wallets(models.Model) :
    balance = models.IntegerField(blank=True, null=True)
    income = models.IntegerField(blank=True, null=True)
    expense = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
        return self.name


class transactions(models.Model) :
    amount = models.IntegerField(blank=True)
    label = models.CharField( 
        max_length = 20, 
        choices = (('1','Income'),('2','Expense')), 
        default = '1',
        blank=True,
        )

    category = models.CharField(max_length=50,blank=True)
    wallet = models.ForeignKey("wallets", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.label} --> {self.amount}"
