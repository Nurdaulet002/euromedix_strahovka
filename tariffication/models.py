from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from insurance.models import Insurance, Insurer, Profession, Hospital


# Базовый класс
class ItemBase(models.Model):
    title = models.CharField(max_length=1000, null=True)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


# Список услуг
class Service(ItemBase):
    code = models.CharField(max_length=80, null=True)
    insurance = models.ForeignKey(
        Insurance, on_delete=models.CASCADE,
        related_name='services', null=True)

    class Meta:
        db_table = "services"


# Группировка услуг пакет
class ServiceGroup(ItemBase):

    class Meta:
        db_table = "service_groups"


# Тарификация услуг
class Tariffication(models.Model):
    TYPE_CHOICES = [
        (1, 'обычный'),
        (2, 'ОМО'),
        (3, 'ОПМО')
    ]
    insurance = models.ForeignKey(
        Insurance, related_name='tariffications_insurance',
        on_delete=models.CASCADE, null=True, blank=True)
    insurer = models.ForeignKey(
        Insurer, on_delete=models.CASCADE,
        related_name='tariffications_insurer', null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE,
                               related_name="children", null=True, blank=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    base_object = GenericForeignKey('content_type', 'object_id')
    price = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    copied = models.ForeignKey('self', on_delete=models.SET_NULL,
                               related_name="children_copy",
                               null=True, blank=True)
    type = models.IntegerField(choices=TYPE_CHOICES, default=1)
    hospital = models.ForeignKey(
        Hospital, on_delete=models.CASCADE,
        related_name='tariffications_hospital', null=True, blank=True)
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE,
        related_name='service_search', null=True, blank=True)

    class Meta:
        db_table = "tariffication"

    def get_all_children(self):
        children = [self]
        try:
            child_list = self.children.all()
        except AttributeError:
            return children
        for child in child_list:
            children.extend(child.get_all_children())
        return children

    def get_all_parents(self):
        parents = [self]
        if self.parent is not None:
            parent = self.parent
            parents.extend(parent.get_all_parents())
        return parents

    def clean(self):
        if self.parent in self.get_all_children():
            raise ValidationError("A user cannot have itself \
                    or one of its' children as parent.")


# Вредности
class Harm(ItemBase):
    professions = models.ManyToManyField(
        Profession, through='ProfessionHarm', symmetrical=False)
    services = models.ManyToManyField(
        Service, through='ServiceHarm', symmetrical=False)

    class Meta:
        db_table = "harms"


# Отношение услуги с вредностью
class ServiceHarm(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    harm = models.ForeignKey(Harm, on_delete=models.CASCADE)
    insurance = models.ForeignKey(
        Insurance, related_name='service_harm_insurances',
        on_delete=models.CASCADE)
    insurer = models.ForeignKey(
        Insurer, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "service_harm"


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


# Группировка профессии ОМО
class Regiment(ItemBase):
    services = models.ManyToManyField(
        Service, through='ServiceRegiment', symmetrical=False)


# Отношение группировки профессии с услугой
class ServiceRegiment(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    regiment = models.ForeignKey(Regiment, on_delete=models.CASCADE)
    insurance = models.ForeignKey(
        Insurance, related_name='service_regiment_insurances',
        on_delete=models.CASCADE)
    insurer = models.ForeignKey(Insurer, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "service_regiment"
