from django.db import models
from insurance.models import Profession, Insurance, Insurer


# Базовый класс
class ItemBase(models.Model):
    title = models.CharField(max_length=1000, null=True)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


# Вредности
class Harm(ItemBase):
    professions = models.ManyToManyField(
        Profession, through='ProfessionHarm', symmetrical=False)

    class Meta:
        db_table = "harms"


# Отношение профессии с вредностью
class ProfessionHarm(models.Model):
    profession = models.ForeignKey(
        Profession, related_name='profession_rel',
        on_delete=models.CASCADE)
    harm = models.ForeignKey(
        Harm, related_name='harm_rel',
        on_delete=models.CASCADE)
    insurance = models.ForeignKey(
        Insurance, related_name='insurance_rel',
        on_delete=models.CASCADE)
    insurer = models.ForeignKey(
        Insurer, related_name='insurer_rel',
        on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "profession_harm"
