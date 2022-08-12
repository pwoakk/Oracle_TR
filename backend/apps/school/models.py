from django.db import models


class School(models.Model):
    name = models.CharField('Школа', max_length=150, unique=True)

    class Meta:
        verbose_name = 'Школа'
        verbose_name_plural = 'Школы'

    def __str__(self):
        return self.name


class Grade(models.Model):
    name = models.CharField('Класс', max_length=10, unique=True)
    teacher = models.ForeignKey('accounts.User',
                                on_delete=models.PROTECT,
                                related_name='grades',
                                verbose_name='Преподаватель')
    school = models.ForeignKey(School,
                               on_delete=models.CASCADE,
                               related_name='grades',
                               verbose_name='Школа')

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'

    def __str__(self):
        return self.name


class Student(models.Model):
    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'
    GENDER_STATUS = (
        (GENDER_MALE, 'мужчина'),
        (GENDER_FEMALE, 'женщина'),
    )
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    middle_name = models.CharField('Отчество', max_length=50)
    email = models.EmailField('Почта', max_length=255, unique=True)
    birthdate = models.DateField(default='', blank=True, null=True)
    grade = models.ForeignKey(Grade,
                              on_delete=models.PROTECT,
                              related_name='students',
                              verbose_name='Класс')
    address = models.CharField('Адрес', max_length=255)
    gender = models.CharField('Пол', max_length=12, choices=GENDER_STATUS, default=GENDER_MALE)

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.grade.name}'


class Subject(models.Model):
    name = models.CharField(max_length=100, verbose_name='Предмет')

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

    def __str__(self):
        return self.name


class Mailing(models.Model):
    title = models.CharField('Название', max_length=250)
    text = models.TextField('Описание')
    students = models.ManyToManyField(Student, related_name='mailing', verbose_name='Студенты')

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'

    def __str__(self):
        return self.title

