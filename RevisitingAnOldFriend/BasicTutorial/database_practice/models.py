from django.db import models

# Create your models here.


class Musician (models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=50)


class Album(models.Model):
    artist = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    release_date = models.DateField()
    num_stars = models.IntegerField()


class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'SMALL'),
        ('M', 'MEDIUM'),
        ('L', 'LARGE'),
    )
    name = models.CharField(max_length=50)
    shirt_size = models.CharField(max_length=6, choices=SHIRT_SIZES)
# get_shirt_size_display() will show full length choice
# while the S, M or L will be saved in the database

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=50)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):
        return self.name


class Membership(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=256)


class Man(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    surname = models.CharField(max_length=50)

    def __str__(self):
        return self.person.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        print("Done saving..", end="hehe\n")
        self.__str__()
