from django.db import models
from django.conf import settings


# Базовый класс
class ItemBase(models.Model):
    title = models.CharField(max_length=1000, null=True)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


# Регионы
class Region(ItemBase):

    class Meta:
        db_table = "regions"


# Города
class City(ItemBase):
    region = models.ForeignKey(
        Region, on_delete=models.CASCADE, related_name='cities_region')

    class Meta:
        db_table = "cities"


# Банки
class Bank(ItemBase):
    title_short = models.CharField(max_length=100, null=True)
    city = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name='cities_bank')


# Базовый абстрактный класс организации
class OrganizationBase(models.Model):
    bin = models.CharField(max_length=12, null=True)
    address = models.CharField(max_length=500, null=True)
    email = models.EmailField(max_length=254, null=True)
    phone = models.CharField(max_length=70, null=True)
    city = models.ForeignKey(
        City, on_delete=models.CASCADE,
        related_name='%(class)s_city', null=True)
    bank = models.ForeignKey(
        Bank, on_delete=models.CASCADE, null=True,
        related_name='%(class)s_bank')

    class Meta:
        abstract = True


# Больницы
class Hospital(ItemBase, OrganizationBase):

    class Meta:
        db_table = "hospitals"

# Професcии
class Profession(ItemBase):

    class Meta:
        db_table = "professions"


# Страховщики
class Insurer(ItemBase, OrganizationBase):
    profession = models.ManyToManyField(
        Profession, related_name='insurances_profession')
    hospitals = models.ManyToManyField(
        Hospital, related_name='insurer_hospitals')

    class Meta:
        db_table = "insurers"


# Страховые компании
class Insurance(ItemBase, OrganizationBase):
    insurers = models.ManyToManyField(
        Insurer, related_name='insurances_insurers')
    hospitals = models.ManyToManyField(
        Hospital, related_name='insurances_hospitals')

    class Meta:
        db_table = "insurance"


# Список работников
class Personification(models.Model):

    GENDER_CHOICES = (
        ('M', 'женщина'),
        ('F', 'мужчина')
    )

    last_name = models.CharField(max_length=180)
    first_name = models.CharField(max_length=180)
    patronymic = models.CharField(max_length=180)
    iin = models.IntegerField(null=True)
    insurer = models.ForeignKey(
        Insurer, on_delete=models.CASCADE,
        related_name='personifications_insurer')
    gender = models.CharField(choices=GENDER_CHOICES, max_length=128)
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE,
                                   related_name="profession")

    class Meta:
        db_table = "personifications"

    @property
    def full_name(self):
        return str('{} {} {}'.format(
            self.last_name, self.first_name, self.patronymic))


# Расширенный модель пользователя
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                primary_key=True,
                                related_name='profile')
    insurance = models.ForeignKey(
        Insurance, related_name='profiles_insurance',
        on_delete=models.CASCADE)

    class Meta:
        db_table = "profile"
