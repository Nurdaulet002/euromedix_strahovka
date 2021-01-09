from django.db import models
from insurance.models import Insurance


# Базовый класс
class ItemBase(models.Model):
    title = models.CharField(max_length=1000, null=True)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


# Список лекарственных средств
class Drug(ItemBase):
    code = models.CharField(max_length=80, null=True)
    insurance = models.ForeignKey(
        Insurance, on_delete=models.CASCADE,
        related_name='drugs_insurance', null=True)

    class Meta:
        db_table = "drugs"
