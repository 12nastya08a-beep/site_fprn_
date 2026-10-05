from django.db import models

class HomePage(models.Model):
    title = models.CharField("Заголовок", max_length=255, default="Факультет природничих наук НаУКМА")
    description = models.TextField("Опис факультету")
    contacts = models.TextField("Контакти")

    class Meta:
        verbose_name = "Текст головної сторінки"
        verbose_name_plural = "Текст головної сторінки"

    def __str__(self):
        return self.title

class Department(models.Model):
    name = models.CharField("Назва кафедри", max_length=255)
    head = models.CharField("Завідувач кафедри", max_length=255)
    description = models.TextField("Опис / Секції", blank=True, null=True)

    class Meta:
        verbose_name = "Кафедра"
        verbose_name_plural = "Кафедри"

    def __str__(self):
        return self.name

class Specialty(models.Model):
    name = models.CharField("Назва спеціальності", max_length=255)
    code = models.CharField("Код спеціальності", max_length=20)
    description = models.TextField("Опис")
    coordinator_name = models.CharField("Ім'я координатора набору", max_length=255)
    coordinator_contact = models.CharField("Контакт координатора набору", max_length=255)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="specialties",
        verbose_name="Випускова кафедра"
    )
    disciplines = models.TextField("Список дисциплін (по роках/триместрах)")

    class Meta:
        verbose_name = "Спеціальність"
        verbose_name_plural = "Спеціальності"

    def __str__(self):
        return f"{self.code} {self.name}"

class Teacher(models.Model):
    name = models.CharField("Ім'я (ПІБ)", max_length=255)
    position = models.CharField("Посада", max_length=255)
    degree = models.CharField("Науковий ступінь / Вчене звання", max_length=255)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="teachers",
        verbose_name="Кафедра"
    )

    class Meta:
        verbose_name = "Викладач"
        verbose_name_plural = "Викладачі"

    def __str__(self):
        return f"{self.name} ({self.position})"
from django.db import models

class ExchangeProgram(models.Model):
    university_name = models.CharField(max_length=255, verbose_name="Назва університету", blank=True, null=True)
    country = models.CharField(max_length=100, verbose_name="Країна", blank=True, null=True)
    languages = models.TextField(verbose_name="Мови навчання")
    slots = models.IntegerField(verbose_name="Кількість місць", default=1)
    deadline = models.DateField(verbose_name="Дедлайн")
    description = models.TextField(verbose_name="Опис")

    class Meta:
        verbose_name = "Програма обміну"
        verbose_name_plural = "Програми обміну"

    def __str__(self):
        return f"{self.university_name}, {self.country}"